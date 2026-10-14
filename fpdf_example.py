from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hola Mundo con fpdf!')
pdf.output('sample_fpdf.pdf')
print('PDF creado: sample_fpdf.pdf')
