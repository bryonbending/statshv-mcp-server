import asyncio
import json
import logging
import os
from typing import Any

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
    ListToolsResult,
)
from dotenv import load_dotenv

from src.db.connection import DatabaseManager
from src.db.statshv_queries import StatshvQueries
from src.llm.veolia_gpt import VeoliaSecureGPT

# Load .env from the project root regardless of working directory
_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
load_dotenv(_env_path, override=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ─── MCP Server Setup ─────────────────────────────────────────────────────────
app = Server("statshv-mcp-server")
veolia_gpt = VeoliaSecureGPT()


def format_results(results: list[dict], max_rows: int = 50) -> str:
    """Format query results as readable text."""
    if not results:
        return "No results found."
    truncated = results[:max_rows]
    lines = [json.dumps(row, default=str) for row in truncated]
    output = "\n".join(lines)
    if len(results) > max_rows:
        output += f"\n... (showing {max_rows} of {len(results)} rows)"
    return output


# ─── Tool Definitions ─────────────────────────────────────────────────────────
@app.list_tools()
async def list_tools() -> ListToolsResult:
    return ListToolsResult(tools=[

        Tool(
            name="ask_statshv_assistant",
            description=(
                "Ask the VeoliaSecureGPT assistant a natural language question about the "
                "statshv instrument test & calibration database. It can answer questions "
                "about bay status, calibration results, repair history, test times, FPY, "
                "and more."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "Your question in plain English."
                    }
                },
                "required": ["question"]
            }
        ),

        Tool(
            name="get_bay_status",
            description=(
                "Get the current status of all test & calibration bays, including the "
                "instrument on each bay, current protocol, step progress, and estimated "
                "finish time. Optionally filter by station name."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "station": {
                        "type": "string",
                        "description": "Optional workstation name to filter results."
                    }
                }
            }
        ),

        Tool(
            name="get_active_instruments",
            description="Get all instruments currently active on test & calibration bays.",
            inputSchema={"type": "object", "properties": {}}
        ),

        Tool(
            name="get_startup_by_serial",
            description=(
                "Look up startup/initialization records for an instrument by serial number. "
                "Returns AQC number, series, model, firmware version, cell IDs, shop order, "
                "and wizard start time."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial instrument serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_recent_startups",
            description="Get instruments that have recently started the T&C process.",
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Number of past days to include (default 7).",
                        "default": 7
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max records to return (default 50).",
                        "default": 50
                    }
                }
            }
        ),

        Tool(
            name="get_instrument_summary",
            description=(
                "Get a full summary for a single instrument serial number: startup details, "
                "repair count, calibration test counts, and key identifiers."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Exact instrument serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_condaz_by_serial",
            description=(
                "Get conductivity auto-zero (condaz) calibration results for an instrument. "
                "Includes reference conductivity, IC/TC pass results, and temperature pass."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_condaz_pass_rate",
            description="Get the conductivity auto-zero pass rate statistics over a rolling period.",
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 90).",
                        "default": 90
                    }
                }
            }
        ),

        Tool(
            name="get_condcalver_by_serial",
            description=(
                "Get conductivity calibration & verification results for an instrument. "
                "Includes Cal Pass, Ver Pass, gain, RSD, and accuracy metrics."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_condcalver_pass_rate",
            description="Get conductivity calibration & verification pass rate statistics.",
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 90).",
                        "default": 90
                    }
                }
            }
        ),

        Tool(
            name="get_spcal_by_serial",
            description=(
                "Get TOC single-point calibration results for an instrument. "
                "Includes slope ratios, peak values, TOC accuracy, RSD, and pass/fail."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_spcal_pass_rate",
            description="Get TOC single-point calibration pass rate statistics.",
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 90).",
                        "default": 90
                    }
                }
            }
        ),

        Tool(
            name="get_speccal_by_serial",
            description="Get specificity calibration results for an instrument.",
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_iotests_by_serial",
            description="Get I/O test results (analog output, alarm relay) for an instrument.",
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_iotests_pass_rate",
            description="Get I/O test pass rate statistics over a rolling period.",
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 90).",
                        "default": 90
                    }
                }
            }
        ),

        Tool(
            name="get_llrinse_by_serial",
            description=(
                "Get low-level rinse test results for an instrument. "
                "Includes conductivity, temperature, flow rate, and IC/TC/TOC readings."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_fluidics_by_serial",
            description=(
                "Get fluidics calibration data for an instrument. "
                "Includes cell averages, flow rate, prime/rinse times, and pass results."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_fluidics_repairs_by_serial",
            description="Get fluidics repair records for an instrument.",
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_repair_history",
            description=(
                "Get the full repair history for an instrument from the repairdat2 table. "
                "Includes assembly, component, failure type, and operator notes."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_top_failures",
            description=(
                "Get the most common failures and components from the repair log "
                "over a rolling period."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 90).",
                        "default": 90
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of top failures to return (default 10).",
                        "default": 10
                    }
                }
            }
        ),

        Tool(
            name="get_fpy_stats",
            description=(
                "Calculate First Pass Yield (FPY) statistics: total instruments started, "
                "instruments with repair records, and FPY percentage."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 30).",
                        "default": 30
                    }
                }
            }
        ),

        Tool(
            name="get_oba_notes",
            description="Get OBA (Out-of-Box Audit) notes for an instrument.",
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_oba_summary",
            description="Get a count summary of OBA results (Pass/Fail/etc.) over a rolling period.",
            inputSchema={
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": "Rolling window in days (default 30).",
                        "default": 30
                    }
                }
            }
        ),

        Tool(
            name="get_preship_by_serial",
            description="Get pre-ship checklist records for an instrument.",
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_constants_by_serial",
            description=(
                "Get the system constants (cell constants, TOC slope, cond slope, etc.) "
                "recorded for an instrument."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Full or partial serial number."
                    }
                },
                "required": ["serial_no"]
            }
        ),

        Tool(
            name="get_actual_protocol_test_times",
            description=(
                "Get actual vs expected protocol test times from the "
                "actual_protocol_testtime_view. Optionally filter by serial number."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "serial_no": {
                        "type": "string",
                        "description": "Optional: full or partial serial number to filter."
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max records to return (default 50).",
                        "default": 50
                    }
                }
            }
        ),

        Tool(
            name="get_expected_test_times",
            description=(
                "Get expected protocol test times by instrument series and model. "
                "Optionally filter by series (e.g. M500, M500e) and model."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "series": {
                        "type": "string",
                        "description": "Instrument series (e.g. M500, M500e)."
                    },
                    "model": {
                        "type": "string",
                        "description": "Instrument model (e.g. STD, SUPER, BASE, SS)."
                    }
                }
            }
        ),

        Tool(
            name="get_test_time_90day_summary",
            description=(
                "Get a 90-day rolling average of actual protocol test times, "
                "grouped by instrument series, model, and options."
            ),
            inputSchema={"type": "object", "properties": {}}
        ),

        Tool(
            name="run_custom_sql",
            description=(
                "Run a custom read-only SQL SELECT query against the statshv database. "
                "Only SELECT statements are permitted."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "A valid MySQL SELECT statement."
                    }
                },
                "required": ["sql"]
            }
        ),

        Tool(
            name="generate_sql_from_natural_language",
            description=(
                "Use VeoliaSecureGPT to convert a natural language request into a SQL query "
                "and execute it against the statshv database."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "request": {
                        "type": "string",
                        "description": "Plain English description of the data you need."
                    },
                    "schema_hint": {
                        "type": "string",
                        "description": "Optional: table/column hints to guide SQL generation."
                    }
                },
                "required": ["request"]
            }
        ),
    ])


# ─── Tool Handlers ────────────────────────────────────────────────────────────
@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> CallToolResult:

    try:
        # ── 1. Ask statshv Assistant (LLM only) ───────────────────────────────
        if name == "ask_statshv_assistant":
            question = arguments["question"]
            response = await veolia_gpt.chat(question)
            return CallToolResult(content=[TextContent(type="text", text=response)])

        # ── 2. Bay Status ─────────────────────────────────────────────────────
        elif name == "get_bay_status":
            station = arguments.get("station")
            results = StatshvQueries.get_bay_status(station)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                "Summarize the current T&C bay status:", context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Bay Status:**\n{text}\n\n**AI Summary:**\n{llm_summary}")
            ])

        # ── 3. Active Instruments ─────────────────────────────────────────────
        elif name == "get_active_instruments":
            results = StatshvQueries.get_active_instruments()
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 4. Startup by Serial ──────────────────────────────────────────────
        elif name == "get_startup_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_startup_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 5. Recent Startups ────────────────────────────────────────────────
        elif name == "get_recent_startups":
            days = arguments.get("days", 7)
            limit = arguments.get("limit", 50)
            results = StatshvQueries.get_recent_startups(days, limit)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 6. Instrument Summary ─────────────────────────────────────────────
        elif name == "get_instrument_summary":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_instrument_summary(serial_no)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Summarize the T&C history for instrument {serial_no}:", context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Instrument Summary:**\n{text}\n\n**AI Summary:**\n{llm_summary}")
            ])

        # ── 7. Condaz by Serial ───────────────────────────────────────────────
        elif name == "get_condaz_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_condaz_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 8. Condaz Pass Rate ───────────────────────────────────────────────
        elif name == "get_condaz_pass_rate":
            days = arguments.get("days", 90)
            results = StatshvQueries.get_condaz_pass_rate(days)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Analyze the conductivity auto-zero pass rates over the last {days} days:",
                context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Condaz Pass Rate ({days}d):**\n{text}\n\n**AI Analysis:**\n{llm_summary}")
            ])

        # ── 9. Condcalver by Serial ───────────────────────────────────────────
        elif name == "get_condcalver_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_condcalver_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 10. Condcalver Pass Rate ──────────────────────────────────────────
        elif name == "get_condcalver_pass_rate":
            days = arguments.get("days", 90)
            results = StatshvQueries.get_condcalver_pass_rate(days)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Analyze the conductivity cal/ver pass rates over the last {days} days:",
                context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Condcalver Pass Rate ({days}d):**\n{text}\n\n**AI Analysis:**\n{llm_summary}")
            ])

        # ── 11. SPcal by Serial ───────────────────────────────────────────────
        elif name == "get_spcal_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_spcal_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 12. SPcal Pass Rate ───────────────────────────────────────────────
        elif name == "get_spcal_pass_rate":
            days = arguments.get("days", 90)
            results = StatshvQueries.get_spcal_pass_rate(days)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Analyze the TOC single-point calibration pass rates over the last {days} days:",
                context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**SPcal Pass Rate ({days}d):**\n{text}\n\n**AI Analysis:**\n{llm_summary}")
            ])

        # ── 13. Speccal by Serial ─────────────────────────────────────────────
        elif name == "get_speccal_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_speccal_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 14. I/O Tests by Serial ───────────────────────────────────────────
        elif name == "get_iotests_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_iotests_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 15. I/O Tests Pass Rate ───────────────────────────────────────────
        elif name == "get_iotests_pass_rate":
            days = arguments.get("days", 90)
            results = StatshvQueries.get_iotests_pass_rate(days)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Analyze the I/O test pass rates over the last {days} days:",
                context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**I/O Test Pass Rate ({days}d):**\n{text}\n\n**AI Analysis:**\n{llm_summary}")
            ])

        # ── 16. LLRinse by Serial ─────────────────────────────────────────────
        elif name == "get_llrinse_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_llrinse_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 17. Fluidics by Serial ────────────────────────────────────────────
        elif name == "get_fluidics_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_fluidics_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 18. Fluidics Repairs by Serial ────────────────────────────────────
        elif name == "get_fluidics_repairs_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_fluidics_repairs_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 19. Repair History ────────────────────────────────────────────────
        elif name == "get_repair_history":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_repair_history(serial_no)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Summarize the repair history for instrument {serial_no}:", context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Repair History:**\n{text}\n\n**AI Summary:**\n{llm_summary}")
            ])

        # ── 20. Top Failures ──────────────────────────────────────────────────
        elif name == "get_top_failures":
            days = arguments.get("days", 90)
            limit = arguments.get("limit", 10)
            results = StatshvQueries.get_top_failures(days, limit)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Analyze the top failures over the last {days} days:", context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Top Failures ({days}d):**\n{text}\n\n**AI Analysis:**\n{llm_summary}")
            ])

        # ── 21. FPY Stats ─────────────────────────────────────────────────────
        elif name == "get_fpy_stats":
            days = arguments.get("days", 30)
            results = StatshvQueries.get_fpy_stats(days)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Summarize the First Pass Yield results over the last {days} days:",
                context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**FPY ({days}d):**\n{text}\n\n**AI Summary:**\n{llm_summary}")
            ])

        # ── 22. OBA Notes ─────────────────────────────────────────────────────
        elif name == "get_oba_notes":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_oba_notes(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 23. OBA Summary ───────────────────────────────────────────────────
        elif name == "get_oba_summary":
            days = arguments.get("days", 30)
            results = StatshvQueries.get_oba_summary(days)
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                f"Summarize OBA results over the last {days} days:", context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**OBA Summary ({days}d):**\n{text}\n\n**AI Summary:**\n{llm_summary}")
            ])

        # ── 24. Pre-Ship by Serial ────────────────────────────────────────────
        elif name == "get_preship_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_preship_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 25. Constants by Serial ───────────────────────────────────────────
        elif name == "get_constants_by_serial":
            serial_no = arguments["serial_no"]
            results = StatshvQueries.get_constants_by_serial(serial_no)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 26. Actual Protocol Test Times ────────────────────────────────────
        elif name == "get_actual_protocol_test_times":
            serial_no = arguments.get("serial_no")
            limit = arguments.get("limit", 50)
            results = StatshvQueries.get_actual_protocol_test_times(serial_no, limit)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 27. Expected Test Times ───────────────────────────────────────────
        elif name == "get_expected_test_times":
            series = arguments.get("series")
            model = arguments.get("model")
            results = StatshvQueries.get_expected_test_times(series, model)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 28. Test Time 90-Day Summary ──────────────────────────────────────
        elif name == "get_test_time_90day_summary":
            results = StatshvQueries.get_test_time_90day_summary()
            text = format_results(results)
            llm_summary = await veolia_gpt.chat(
                "Analyze the 90-day average protocol test times by series and model:",
                context=text
            )
            return CallToolResult(content=[
                TextContent(type="text", text=f"**Test Time Summary (90d):**\n{text}\n\n**AI Analysis:**\n{llm_summary}")
            ])

        # ── 29. Custom SQL ────────────────────────────────────────────────────
        elif name == "run_custom_sql":
            sql = arguments["sql"]
            results = StatshvQueries.run_custom_query(sql)
            text = format_results(results)
            return CallToolResult(content=[TextContent(type="text", text=text)])

        # ── 30. Natural Language → SQL → Execute ──────────────────────────────
        elif name == "generate_sql_from_natural_language":
            request = arguments["request"]
            schema_hint = arguments.get("schema_hint", "")
            sql = await veolia_gpt.generate_sql(request, schema_hint)
            sql = sql.strip().strip("```sql").strip("```").strip()
            logger.info(f"Generated SQL: {sql}")
            results = StatshvQueries.run_custom_query(sql)
            text = format_results(results)
            llm_answer = await veolia_gpt.chat(
                f"Answer this question: {request}",
                context=f"SQL used: {sql}\n\nResults:\n{text}"
            )
            return CallToolResult(content=[
                TextContent(type="text", text=(
                    f"**Generated SQL:**\n```sql\n{sql}\n```\n\n"
                    f"**Raw Results:**\n{text}\n\n"
                    f"**AI Answer:**\n{llm_answer}"
                ))
            ])

        else:
            raise ValueError(f"Unknown tool: {name}")

    except PermissionError as e:
        return CallToolResult(
            content=[TextContent(type="text", text=f"❌ Permission denied: {e}")],
            isError=True
        )
    except Exception as e:
        logger.error(f"Tool '{name}' error: {e}", exc_info=True)
        return CallToolResult(
            content=[TextContent(type="text", text=f"❌ Error: {e}")],
            isError=True
        )


# ─── Entry Point ──────────────────────────────────────────────────────────────
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="statshv-mcp-server",
                server_version="1.0.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(tools_changed=False),
                    experimental_capabilities={}
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
