from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_report(dilemma_text, analysis_results, debate_log, risk_score, recommendations):
    filename = "Ethical_Report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Ethical Dilemma Analysis Report")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Risk Score: {risk_score:.2f}%")
    
    c.drawString(50, height - 110, "Dilemma Summary:")
    # Simple text wrap logic for demonstration (production should use Paragraph/Platypus)
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, height - 125, dilemma_text[:80] + "...")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, "Key Insights:")
    c.setFont("Helvetica", 10)
    y = height - 180
    for entity in analysis_results.get('entities', [])[:5]:
        c.drawString(60, y, f"- Entity: {entity[0]} ({entity[1]})")
        y -= 15
        
    c.drawString(50, y - 20, "Debate Highlights:")
    y -= 40
    for log in debate_log[:5]:
        c.drawString(60, y, f"- {log}")
        y -= 15
        
    c.drawString(50, y - 20, "Recommended Actions:")
    y -= 40
    for rec in recommendations:
        c.drawString(60, y, f"-> {rec}")
        y -= 15
        
    c.save()
    return filename
