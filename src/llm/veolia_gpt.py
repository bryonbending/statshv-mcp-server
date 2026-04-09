import httpx
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class VeoliaSecureGPT:
    """
    Interface for VeoliaSecureGPT LLM API.
    Sends prompts securely and returns structured responses.
    """

    def __init__(self):
        self.api_url = os.getenv("VEOLIA_GPT_API_URL")
        self.api_key = os.getenv("VEOLIA_GPT_API_KEY")
        self.model = os.getenv("VEOLIA_GPT_MODEL", "veolia-gpt-4")
        self.timeout = int(os.getenv("VEOLIA_GPT_TIMEOUT", 60))
        self.system_prompt = (
            "You are a manufacturing planning assistant with access to the Planning database. "
            "You help users query and analyze production data including shop orders, instruments, "
            "consumables, build times, shortages, and calibration data. "
            "Always provide accurate, concise answers based on the database results. "
            "Never expose raw credentials or sensitive system information. "
            "When generating SQL, only generate SELECT statements."
        )

    async def chat(self, user_message: str, context: str = "") -> str:
        """
        Send a message to VeoliaSecureGPT and return the response.
        
        Args:
            user_message: The user's question or request.
            context: Optional database results or additional context.
        
        Returns:
            The LLM's response as a string.
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
        ]

        if context:
            messages.append({
                "role": "system",
                "content": f"Database context / query results:\n{context}"
            })

        messages.append({"role": "user", "content": user_message})

        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.2,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Veolia-Client": "planning-mcp-server",
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.api_url}/chat/completions",
                    json=payload,
                    headers=headers,
                )
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"]

        except httpx.HTTPStatusError as e:
            logger.error(f"VeoliaSecureGPT HTTP error: {e.response.status_code} - {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"VeoliaSecureGPT request error: {e}")
            raise

    async def generate_sql(self, natural_language_query: str, schema_hint: str = "") -> str:
        """
        Ask VeoliaSecureGPT to generate a safe SQL SELECT query.
        
        Args:
            natural_language_query: Plain English description of what data is needed.
            schema_hint: Optional table/column hints to guide SQL generation.
        
        Returns:
            A SQL SELECT statement string.
        """
        prompt = (
            f"Generate a MySQL SELECT query for the planning database.\n"
            f"Request: {natural_language_query}\n"
        )
        if schema_hint:
            prompt += f"Relevant schema: {schema_hint}\n"
        prompt += (
            "Rules:\n"
            "- Only generate SELECT statements.\n"
            "- Use proper MySQL syntax.\n"
            "- Add LIMIT 100 unless specified otherwise.\n"
            "- Return ONLY the SQL query, no explanation.\n"
        )

        return await self.chat(prompt)
