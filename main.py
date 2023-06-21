from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv('/home/tianlong55/Downloads/PyCharm_Projects/app4_pdf_templete/topics.csv')
pdf.set_auto_page_break(auto=False , margin=0)
for index, row in df.iterrows():
    pdf.add_page()
    texto = row['Topic']
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12, txt= texto, align="L", ln=1)
    pdf.line(x1=10,y1=21,x2=200,y2=21)


    ## SET FOOTER FIRST PAGE
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row['Topic'],align="R")
    for i in range(21,277,10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)

    for i in range(row['Pages']-1):
        pdf.add_page()
        ## SET FOOTER FIRST PAGE
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
        for i in range(21,277,8):
            pdf.line(x1=10, y1=i, x2=200, y2=i)

pdf.output("output.pdf")




