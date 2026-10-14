# Python Library Examples Repository

Este repositorio contiene ejemplos sencillos de uso de varias librerías populares de Python. Cada ejemplo está en su propio archivo `.py` y está pensado para ser ejecutado tal cual (requerirá instalar las dependencias correspondientes).

## Contenidos

| Archivo | Librería | Descripción |
|---|---|---|
| `math_example.py` | `math` | Operaciones matemáticas básicas y funciones trigonométricas. |
| `random_example.py` | `random` | Generación de números aleatorios y selección aleatoria de elementos. |
| `datetime_example.py` | `datetime` | Manipulación de fechas y horas, formateo y cálculo de diferencias. |
| `csv_example.py` | `csv` | Lectura y escritura de archivos CSV. |
| `fpdf_example.py` | `fpdf` | Generación sencilla de PDFs. |
| `reportlab_example.py` | `reportlab` | Creación de PDFs más avanzados con tablas y estilos. |
| `numpy_example.py` | `NumPy` | Operaciones con arrays, álgebra lineal y estadísticas básicas. |
| `pandas_example.py` | `pandas` | Manipulación de DataFrames, filtrado y agrupamiento. |
| `matplotlib_example.py` | `Matplotlib` | Graficado de datos con diagramas de línea y barras. |
| `requests_example.py` | `requests` | Realizar peticiones HTTP GET y POST. |
| `flask_example.py` | `Flask` | Aplicación web mínima con una ruta sencilla. |
| `sklearn_example.py` | `scikit‑learn` | Entrenamiento de un modelo de clasificación simple (k‑NN) y evaluación. |

## Requisitos

Instale las dependencias con:

```bash
pip install fpdf2 reportlab numpy pandas matplotlib requests flask scikit-learn
```

> **Nota:** `math`, `random` y `datetime` forman parte de la biblioteca estándar y no requieren instalación.

## Uso

Ejecute cada archivo con Python:

```bash
python math_example.py
python random_example.py
# ... etc.
```

Los ejemplos imprimen resultados en la consola y, en algunos casos, generan archivos (`output.csv`, `sample.pdf`).

---

### Detalle de cada ejemplo

#### `math_example.py`
```python
import math

print("π (pi) =", math.pi)
print("Raíz cuadrada de 2 =", math.sqrt(2))
print("Seno de 45° =", math.sin(math.radians(45)))
```

#### `random_example.py`
```python
import random

print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Elemento aleatorio de una lista:", random.choice(['a', 'b', 'c']))
print("Muestra de 3 elementos sin reemplazo:", random.sample(range(100), 3))
```

#### `datetime_example.py`
```python
from datetime import datetime, timedelta

ahora = datetime.now()
print("Fecha y hora actual:", ahora)

mañana = ahora + timedelta(days=1)
print("Mañana será:", mañana)

formato = ahora.strftime("%Y-%m-%d %H:%M:%S")
print("Formato legible:", formato)
```

#### `csv_example.py`
```python
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
```

#### `fpdf_example.py`
```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hola Mundo con fpdf!')
pdf.output('sample_fpdf.pdf')
print('PDF creado: sample_fpdf.pdf')
```

#### `reportlab_example.py`
```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas('sample_reportlab.pdf', pagesize=letter)
width, height = letter
c.drawString(100, height - 100, "Hola Mundo con ReportLab!")

# Dibujar una tabla simple
data = [['Nombre', 'Edad'], ['Ana', '30'], ['Luis', '25']]

table_y = height - 150
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        c.drawString(100 + j*100, table_y - i*20, cell)

c.save()
print('PDF creado: sample_reportlab.pdf')
```

#### `numpy_example.py`
```python
import numpy as np

# Creación de array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('Array:\n', arr)

# Operaciones vectorizadas
print('Suma de columnas:', arr.sum(axis=0))
print('Media de filas:', arr.mean(axis=1))
```

#### `pandas_example.py`
```python
import pandas as pd

# DataFrame de ejemplo
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Maria'],
    'Edad': [30, 25, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']
})
print('DataFrame completo:\n', df)

# Filtrado
mayores_26 = df[df['Edad'] > 26]
print('Personas mayores de 26:\n', mayores_26)

# Agrupamiento
agrupado = df.groupby('Ciudad')['Edad'].mean()
print('Edad media por ciudad:\n', agrupado)
```

#### `matplotlib_example.py`
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.title('Gráfico de seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.savefig('sine_plot.png')
plt.show()
```

#### `requests_example.py`
```python
import requests

# GET simple
resp = requests.get('https://api.github.com')
print('Estado:', resp.status_code)
print('Encabezados:', resp.headers['Content-Type'])

# POST a httpbin (eco)
payload = {'key': 'value'}
resp = requests.post('https://httpbin.org/post', json=payload)
print('Respuesta POST JSON:', resp.json())
```

#### `flask_example.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

> Ejecutar este script iniciará un servidor web en `http://127.0.0.1:5000/`.

#### `sklearn_example.py`
```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Cargar dataset iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# División entrenamiento / prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo k‑NN
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Predicción y evaluación
y_pred = clf.predict(X_test)
print('Exactitud del modelo:', accuracy_score(y_test, y_pred))
```

---

**¡Listo!**

Puede clonar este repositorio, explorar los ejemplos y adaptarlos a sus necesidades.
