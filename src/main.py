import os
import pandas as pd

from processing.data_processing import procesar_productos
from processing.kpis import generar_kpis
from utils.helpers import exportar_a_pdf
from database.conexion_db import conexion_y_insert
from config.logger import logger


def main() -> None:
    logger.info("Pipeline started")

    # ---------------- CONFIG ----------------
    API_URL = "https://fakestoreapi.com/products"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    REPORTS_DIR = os.path.join(BASE_DIR, "reports")
    EXCEL_DIR = os.path.join(REPORTS_DIR, "excel")
    PDF_DIR = os.path.join(REPORTS_DIR, "pdf")

    EXCEL_PATH = os.path.join(EXCEL_DIR, "productos.xlsx")
    PDF_PATH = os.path.join(PDF_DIR, "reporte_productos.pdf")

    os.makedirs(EXCEL_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)

    # ---------------- DATA ----------------
    logger.info("Fetching and cleaning data from API")
    cleaned_df = procesar_productos(API_URL)

    if cleaned_df.empty:
        logger.error("No data retrieved from API. Pipeline stopped.")
        return

    logger.info(f"Data retrieved successfully: {len(cleaned_df)} records")

    # ---------------- KPIs ----------------
    logger.info("Generating KPIs")
    kpis_df = generar_kpis(API_URL)

    # ---------------- EXCEL ----------------
    logger.info("Exporting Excel report")
    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        cleaned_df.to_excel(writer, sheet_name="Products", index=False)
        kpis_df.to_excel(writer, sheet_name="KPIs", index=False)

    logger.info(f"Excel generated at {EXCEL_PATH}")

    # ---------------- PDF ----------------
    logger.info("Generating PDF report")
    exportar_a_pdf(cleaned_df, kpis_df, PDF_PATH)
    logger.info(f"PDF generated at {PDF_PATH}")

    # ---------------- DATABASE ----------------
    logger.info("Preparing data for MySQL insertion")
    sql_columns = ["id", "title", "price", "rate"]
    records = list(cleaned_df[sql_columns].itertuples(index=False, name=None))

    logger.info(f"Records to insert: {len(records)}")
    conexion_y_insert(records)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()
