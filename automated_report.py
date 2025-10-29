import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# Step 1: Read data
data = pd.read_csv("data.csv")
summary = data.describe()

# Step 2: Create PDF document
pdf_filename = "Automated_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Step 3: Add Title and Date
title = Paragraph("<b><font size=18>Automated Data Report</font></b>", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 12))
date = Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"])
elements.append(date)
elements.append(Spacer(1, 20))

# Step 4: Add Summary Table
elements.append(Paragraph("<b>Summary Statistics:</b>", styles["Heading2"]))
elements.append(Spacer(1, 8))
table = Table([["Metric"] + summary.columns.tolist()] + summary.round(2).reset_index().values.tolist())
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
]))
elements.append(table)
elements.append(Spacer(1, 20))

# Step 5: Add Conclusion
elements.append(Paragraph("<b>Conclusion:</b>", styles["Heading2"]))
elements.append(Paragraph(
    "This automated report provides quick insights into the dataset. "
    "It includes summary statistics such as mean, minimum, and maximum values for each column.",
    styles["Normal"]
))

# Step 6: Build PDF
doc.build(elements)
print(f"✅ Report generated successfully: {pdf_filename}")
