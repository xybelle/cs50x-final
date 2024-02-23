from fpdf import FPDF


def main():
    name = get_name()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=30)
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.cell(border=0, align="C", text="CS50 Shirtificate")
    pdf.output("shirtificate.pdf")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
