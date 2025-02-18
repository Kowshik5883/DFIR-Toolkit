from fpdf import FPDF

def generate_pdf_report(threats, report_file="threat_report.pdf"):
    """Generates a PDF report of detected threats."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Threat Hunting Report", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(50, 10, "Process Name", border=1)
    pdf.cell(30, 10, "PID", border=1)
    pdf.cell(110, 10, "Threat Description", border=1, ln=True)
    pdf.set_font("Arial", size=10)
    
    for name, pid, description in threats:
        pdf.cell(50, 10, name, border=1)
        pdf.cell(30, 10, str(pid), border=1)
        pdf.cell(110, 10, description, border=1, ln=True)
    
    pdf.output(report_file)
    print(f"Report generated: {report_file}")

if __name__ == "__main__":
    test_threats = [
        ("malware.exe", 1234, "Detected as Trojan"),
        ("keylogger.exe", 5678, "Detected as Keylogger")
    ]
    generate_pdf_report(test_threats)
