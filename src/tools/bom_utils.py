import os
import pandas as pd
from dotenv import load_dotenv

from src.db.connection import DatabaseManager

_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env")
load_dotenv(_env_path, override=True)


def get_bom_dataframe(part_no: str) -> pd.DataFrame:
    """Return the full Bill of Materials for *part_no* as a pandas DataFrame.

    Performs an exact match on PartNo in the partbom table.  If you want all
    dash-suffix variants (e.g. every 'AQC 78200-xx'), pass a LIKE-style wildcard
    by appending '%' to the part number: ``get_bom_dataframe('AQC 78200%')``.

    Columns returned:
        PartNo, SubPart, Description, ItemNo, Qty, UMEA, EffDate, TermDate

    Returns an empty DataFrame (with the expected columns) when no rows match.
    """
    if "%" in part_no or "_" in part_no:
        query = """
            SELECT PartNo, SubPart, Description, ItemNo, Qty, UMEA, EffDate, TermDate
            FROM partbom
            WHERE PartNo LIKE %s
            ORDER BY PartNo, ItemNo ASC
        """
        params = (part_no,)
    else:
        query = """
            SELECT PartNo, SubPart, Description, ItemNo, Qty, UMEA, EffDate, TermDate
            FROM partbom
            WHERE PartNo = %s
            ORDER BY ItemNo ASC
        """
        params = (part_no,)

    rows = DatabaseManager.execute_safe_query(query, params)

    columns = ["PartNo", "SubPart", "Description", "ItemNo", "Qty", "UMEA", "EffDate", "TermDate"]
    if not rows:
        return pd.DataFrame(columns=columns)

    df = pd.DataFrame(rows, columns=columns)
    df["EffDate"] = pd.to_datetime(df["EffDate"], errors="coerce")
    df["TermDate"] = pd.to_datetime(df["TermDate"], errors="coerce")
    return df
