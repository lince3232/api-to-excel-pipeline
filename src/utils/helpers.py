import os
import pandas as pd
from fpdf import FPDF, XPos, YPos


def export_to_pdf(
    df: pd.DataFrame,
    kpis_df: pd.DataFrame,
    output_path: str
) -> None:
    """
    Export product data and KPI summary to a formatted PDF report.

    Args:
        df (pd.DataFrame): Cleaned product data
        kpis_df (pd.DataFrame): KPI metrics
        output_path (str): Destination PDF file path
    """
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    # Try loading Unicode fonts (Windows-friendly, safe fallback)
    font_dir = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")
    regular_font = os.path.join(font_dir, "arial.ttf")
    bold_font = os.path.join(font_dir, "arialbd.ttf")

    if os.path.exists(regular_font):
        pdf.add_font("ArialUnicode", "", regular_font)
        if os.path.exists(bold_font):
            pdf.add_font("ArialUnicode", "B", bold_font)
        main_font = "ArialUnicode"
    else:
        main_font = "Helvetica"

    # -------- PAGE 1: PRODUCT TABLE --------
    pdf.add_page()

    pdf.set_font(main_font, size=16)
    pdf.cell(
        0, 10,
        "Product Report - FakeStore API",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="C"
    )
    pdf.ln(5)

    pdf.set_font(main_font, size=8)
    columns = ["id", "title", "price", "rate"]
    table_df = df[columns].head(20).copy()

    with pdf.table(col_widths=(10, 60, 15, 15), text_align="LEFT") as table:
        header = table.row()
        for col in columns:
            header.cell(col.upper())

        for _, row_data in table_df.iterrows():
            row = table.row()
            for value in row_data:
                row.cell(str(value))

    # -------- PAGE 2: KPI SUMMARY --------
    pdf.add_page()

    pdf.set_font(main_font, "B", size=16)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(
        0, 10,
        "KPI Summary",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="L"
    )

    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    pdf.set_font(main_font, size=12)

    for i in range(len(kpis_df)):
        metric = str(kpis_df.iloc[i, 0])
        value = str(kpis_df.iloc[i, 1])

        pdf.cell(60, 10, f"{metric}:", border=0)
        pdf.set_font(main_font, "B", size=12)
        pdf.cell(0, 10, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font(main_font, size=12)

    pdf.output(output_path)
