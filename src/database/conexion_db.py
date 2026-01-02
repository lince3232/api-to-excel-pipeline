import os
import logging
import mysql.connector
from mysql.connector import Error

logging.basicConfig(level=logging.INFO)


def insert_products(records: list[tuple]) -> int:
    """
    Insert product records into MySQL database.

    Args:
        records (list[tuple]): List of product tuples (id, title, price, rate)

    Returns:
        int: Number of inserted rows
    """
    connection = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306))
        )

        cursor = connection.cursor()

        query = """
            INSERT INTO tienda (id, title, price, rate)
            VALUES (%s, %s, %s, %s)
        """

        cursor.executemany(query, records)
        connection.commit()

        logging.info(f"{cursor.rowcount} records inserted successfully")
        return cursor.rowcount

    except Error as e:
        logging.error(f"Database error: {e}")
        return 0

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            logging.info("Database connection closed")
