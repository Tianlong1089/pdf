import glob
from fpdf import FPDF


def open_read(file_name):
    with open(file_name) as f:
        list = f.readlines()
    return list


paths = glob.glob('/media/tianlong55/BLOCK II/Data/Text+Files/*.txt')

pdf = FPDF(orientation="P", unit="mm", format="A4")

for path in paths:
    header = path.split('/')[-1].replace('.txt','').capitalize()
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{header}")

    pdf.set_font(family="Times", size=11)
    text = open_read(path)[0]
    pdf.multi_cell(w=55, h=5, txt=f"{text}",align="L")

    open_read(path)

pdf.output(f'/home/tianlong55/Downloads/PyCharm_Projects/Excel_to_Pdf/PDF/animals.pdf')