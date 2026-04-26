from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf(data, score, risk, recommendations, filename="mind_balance_report.pdf"):

    # Create a PDF canvas
    c = canvas.Canvas(filename)
    # TITLE
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 800, "Mind Balance - Personal Report")

    # METADATA
    c.setFont("Helvetica", 11)
    c.drawString(50, 770, f"Generated: {datetime.now()}")

    c.drawString(50, 740, f"Health Score: {score}/100")
    c.drawString(50, 720, f"Risk Level: {risk}")
    
    # LIFESTYLE DATA
    y = 680
    c.drawString(50, y, "Lifestyle Data:")
    y -= 20

    for k, v in data.items():
        c.drawString(60, y, f"{k}: {v}")
        y -= 18
        
    # RECOMMENDATIONS
    y -= 10
    c.drawString(50, y, "Recommendations:")
    y -= 20

    for r in recommendations:
        c.drawString(60, y, f"- {r[:90]}")
        y -= 18

    # FINALISE PDF
    c.save()
    return filename