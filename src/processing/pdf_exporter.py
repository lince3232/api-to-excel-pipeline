import os
import pandas as pd
from fpdf import FPDF, XPos, YPos


def export_to_pdf(df: pd.DataFrame, output_path: str) -> None:
    """
    Export a DataFrame to a formatted PDF report.

    Args:
        df (pd.DataFrame): Cleaned product data
        output_path (str): Destination PDF file path
    """
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    # Try loading a Unicode font (Windows-friendly, fallback safe)
    font_path = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "arial.ttf")

    if os.path.exists(font_path):
        pdf.add_font("ArialUnicode", "", font_path)
        main_font = "ArialUnicode"
    else:
        main_font = "Helvetica"

    pdf.add_page()

    # Title
    pdf.set_font(main_font, size=16)
    pdf.cell(
        0, 10,
        "Product Report - FakeStore API",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="C"
    )
    pdf.ln(5)

    # Table configuration
    columns = ["id", "title", "price", "rate"]
    filtered_df = df[columns].copy()

    # Clean text defensively
    filtered_df["title"] = filtered_df["title"].apply(
        lambda x: str(x).encode("utf-8", "ignore").decode("utf-8")
    )

    pdf.set_font(main_font, size=8)

    with pdf.table(col_widths=(10, 60, 15, 15), text_align="LEFT") as table:
        header = table.row()
        for col in columns:
            header.cell(col.upper())

        for _, row_data in filtered_df.iterrows():
            row = table.row()
            for value in row_data:
                row.cell(str(value))

    pdf.output(output_path)
