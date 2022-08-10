# from fpdf import FPDF

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('helvetica', size=12)
# pdf.cell(txt="hello world")
# pdf.output("hello_world.pdf")

"""tuto1.pdf"""
# from fpdf import FPDF

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("helvetica", "B", 16)
# # pdf.cell(-1, 10, "Jhon Havard took CS50")
# pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')
# pdf.output("tuto1.pdf")


"""tuto2.pdf"""
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", x = 10, y = 50, h = 3*pdf.eph/4, w = pdf.epw)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 30, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)



# Instantiation of inherited class
pdf = PDF()
pdf.add_page()

name = input("Name: ")
pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(r = 255, g = 255, b = 255)
pdf.cell(60)
pdf.cell(80,140, f"{name.capitalize()} took CS50", align="C")
pdf.set_margin(0)
pdf.output("shirtificate.pdf")


# from fpdf import FPDF

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Times", size=36)
# pdf.set_text_color(r = 255, g = 0, b = 255)
# pdf.cell(txt="This")
# pdf.set_font(style="B")
# pdf.cell(txt="is")
# pdf.set_font(style="I")
# pdf.cell(txt="a")
# pdf.set_font(style="U")
# pdf.cell(txt="PDF")
# pdf.output("style.pdf")




