from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas('sample_reportlab.pdf', pagesize=letter)
width, height = letter
c.drawString(100, height - 100, "Hola Mundo con ReportLab!")

data = [['Nombre', 'Edad'], ['Ana', '30'], ['Luis', '25']]

table_y = height - 150
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        c.drawString(100 + j*100, table_y - i*20, cell)

c.save()
print('PDF creado: sample_reportlab.pdf')
