from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).parent / 'hasil'
OUT.mkdir(exist_ok=True)

def segitiga(x, a, b, c):
    x = np.asarray(x, dtype=float)
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def trapesium(x, a, b, c, d):
    x = np.asarray(x, dtype=float)
    naik = np.ones_like(x) if a == b else (x-a)/(b-a)
    turun = np.ones_like(x) if c == d else (d-x)/(d-c)
    return np.maximum(0, np.minimum(1, np.minimum(naik, turun)))

MODEL = {
    'CPU': {'satuan': '%', 'semesta': (0, 100), 'label': {
        'Rendah': ('trap', (0, 0, 20, 40)),
        'Normal': ('tri', (30, 50, 70)),
        'Tinggi': ('trap', (60, 80, 100, 100))}},
    'RAM': {'satuan': '%', 'semesta': (0, 100), 'label': {
        'Rendah': ('trap', (0, 0, 30, 50)),
        'Normal': ('tri', (40, 60, 80)),
        'Tinggi': ('trap', (70, 90, 100, 100))}},
    'Risiko': {'satuan': 'poin', 'semesta': (0, 100), 'label': {
        'Rendah': ('trap', (0, 0, 25, 45)),
        'Sedang': ('tri', (35, 55, 75)),
        'Tinggi': ('trap', (65, 85, 100, 100))}}
}

def hitung(x, bentuk, parameter):
    fungsi = segitiga if bentuk == 'tri' else trapesium
    return fungsi(x, *parameter)

def fuzzifikasi(input_dict):
    if set(input_dict) != {'CPU', 'RAM'}:
        raise ValueError('Input wajib berisi CPU dan RAM')
    hasil = {}
    for nama, x in input_dict.items():
        var = MODEL[nama]
        lo, hi = var['semesta']
        if not np.isfinite(x) or not lo <= x <= hi:
            raise ValueError(f'{nama} di luar semesta')
        hasil[nama] = {
            label: float(hitung(x, bentuk, parameter))
            for label, (bentuk, parameter) in var['label'].items()
        }
    return hasil

def plot_variabel():
    for nama, var in MODEL.items():
        x = np.linspace(*var['semesta'], 1001)
        fig, ax = plt.subplots(figsize=(9, 4))
        for label, (bentuk, param) in var['label'].items():
            ax.plot(x, hitung(x, bentuk, param), label=label)
        ax.set(title=f'Model variabel {nama}',
               xlabel=f"{nama} ({var['satuan']})",
               ylabel='Derajat keanggotaan', ylim=(-.05, 1.05))
        ax.legend()
        ax.grid(alpha=.3)
        fig.tight_layout()
        fig.savefig(OUT / f'p5_{nama.lower()}.png', dpi=200)
        plt.close(fig)

# Data berikut adalah simulasi, bukan pengukuran server nyata.
DATA_SIMULASI = [
    ('Ekstrem bawah', 0, 0),
    ('Beban ringan', 20, 30),
    ('Transisi rendah-normal', 35, 45),
    ('Beban menengah', 50, 60),
    ('Transisi normal-tinggi', 65, 75),
    ('Beban tinggi', 85, 90),
    ('Ekstrem atas', 100, 100)
]

def uji_data(data):
    rows = []
    for kasus, cpu, ram in data:
        h = fuzzifikasi({'CPU': cpu, 'RAM': ram})
        print(f'{kasus}: CPU={cpu}%, RAM={ram}%')
        print(h)
        rows.append([cpu, ram, *h['CPU'].values(), *h['RAM'].values()])
    return np.array(rows)

if __name__ == '__main__':
    plot_variabel()
    rows = uji_data(DATA_SIMULASI)
    np.savetxt(OUT / 'p5_simulasi.csv', rows, delimiter=',',
        header='CPU,RAM,CPU_Rendah,CPU_Normal,CPU_Tinggi,'
               'RAM_Rendah,RAM_Normal,RAM_Tinggi', comments='')
    file_nyata = OUT / 'p5_data_nyata.csv'
    if file_nyata.exists():
        with file_nyata.open(newline='', encoding='utf-8-sig') as f:
            data_nyata = [
                (r['kondisi'], float(r['CPU']), float(r['RAM']))
                for r in csv.DictReader(f)
            ]
        print('\nHASIL FUZZIFIKASI DATA PENGUKURAN NYATA')
        hasil_nyata = uji_data(data_nyata)
        np.savetxt(OUT / 'p5_fuzzifikasi_nyata.csv', hasil_nyata,
            delimiter=',',
            header='CPU,RAM,CPU_Rendah,CPU_Normal,CPU_Tinggi,'
                   'RAM_Rendah,RAM_Normal,RAM_Tinggi', comments='')
