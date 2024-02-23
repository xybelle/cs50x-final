from fpdf import FPDF


def main():
    name = get_name()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", size=30)
    pdf.image("shirtificate.png", x="Align.C")
    pdf.cell(text="CS50 Shirtificate", border=0, align="C", center=True)
    pdf.output("shirtificate.pdf")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
