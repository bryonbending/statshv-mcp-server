import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Manages MySQL connection pool for the planning database."""

    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            cls._pool = pooling.MySQLConnectionPool(
                pool_name="planning_pool",
                pool_size=int(os.getenv("DB_POOL_SIZE", 5)),
                host=os.getenv("DB_HOST", "10.173.202.12"),
                port=int(os.getenv("DB_PORT", 3306)),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME", "statshv"),
                charset="utf8mb4",
                autocommit=True,
            )
            logger.info("MySQL connection pool created.")
        return cls._pool

    @classmethod
    def get_connection(cls):
        return cls.get_pool().get_connection()

    @classmethod
    def execute_query(cls, query: str, params: tuple = None) -> list[dict]:
        """Execute a SELECT query and return results as list of dicts."""
        conn = cls.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            results = cursor.fetchall()
            cursor.close()
            return results
        except mysql.connector.Error as e:
            logger.error(f"Database error: {e}")
            raise
        finally:
            conn.close()

    @classmethod
    def execute_safe_query(cls, query: str, params: tuple = None) -> list[dict]:
        """Execute only SELECT queries (read-only enforcement)."""
        stripped = query.strip().upper()
        forbidden = ["INSERT", "UPDATE", "DELETE", "DROP", "TRUNCATE", "ALTER", "CREATE", "REPLACE"]
        for keyword in forbidden:
            if stripped.startswith(keyword):
                raise PermissionError(f"Write operation '{keyword}' is not allowed in read-only mode.")
        return cls.execute_query(query, params)
