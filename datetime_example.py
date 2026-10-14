from datetime import datetime, timedelta

ahora = datetime.now()
print('Fecha y hora actual:', ahora)

mañana = ahora + timedelta(days=1)
print('Mañana será:', mañana)

formato = ahora.strftime('%Y-%m-%d %H:%M:%S')
print('Formato legible:', formato)
