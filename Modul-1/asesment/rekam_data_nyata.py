import csv
from pathlib import Path
import psutil
from Praktikum5_240306052 import uji_data

# Ukur pada komputer/server yang menjadi objek penelitian.
# Pengukuran laptop harus dilaporkan sebagai pengukuran laptop.
data = []
for i in range(5):
    kondisi = input(f'Keterangan kondisi ke-{i+1}: ')
    input('Siapkan kondisi tersebut, lalu tekan Enter untuk mengukur. ')
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    data.append((kondisi, cpu, ram))
    print(f'CPU={cpu}%, RAM={ram}%')
out = Path(__file__).parent / 'hasil'
out.mkdir(exist_ok=True)
file = out / 'p5_data_nyata.csv'
with file.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['kondisi', 'CPU', 'RAM'])
    writer.writerows(data)
uji_data(data)
