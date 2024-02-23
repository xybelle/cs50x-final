from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.image("shirtificate.png", x=20, y=60)
pdf.cell(text="hello world")
pdf.output("shirtificate.pdf")
