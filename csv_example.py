import csv

# Escritura
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Nombre', 'Edad'])
    writer.writerow(['Ana', 30])
    writer.writerow(['Luis', 25])

# Lectura
with open('output.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
