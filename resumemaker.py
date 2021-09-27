from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

name = input("Enter Your name")
address = input("Type Address")

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(200, 10, txt = name,
		ln = 1, align = 'C')

# add another cell
pdf.cell(200, 10, txt = address,
		ln = 2, align = 'C')

# save the pdf with name .pdf
pdf.output("resume.pdf")
