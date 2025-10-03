#!/usr/bin/env python

from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=50)
pdf.text(40, 60, "CS50 Shirtificate")
pdf.image("./shirtificate.png", 10, 70, 190)
pdf.set_font("helvetica", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(190, 250, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
