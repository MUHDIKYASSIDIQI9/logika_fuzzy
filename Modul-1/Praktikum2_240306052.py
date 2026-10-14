from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).parent / 'hasil'
OUT.mkdir(exist_ok=True)

def bahu_kiri(x, penuh, nol):
    return np.clip((nol - np.asarray(x)) / (nol - penuh), 0, 1)

def segitiga(x, a, b, c):
    x = np.asarray(x)
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def bahu_kanan(x, nol, penuh):
    return np.clip((np.asarray(x) - nol) / (penuh - nol), 0, 1)

waktu = {
    'nama': 'Waktu respons server', 'satuan': 'detik',
    'semesta': (0, 10),
    'label': {
        'Cepat': lambda x: bahu_kiri(x, 2, 4),
        'Sedang': lambda x: segitiga(x, 3, 5, 7),
        'Lambat': lambda x: bahu_kanan(x, 6, 8)
    }
}
cpu = {
    'nama': 'Penggunaan CPU server', 'satuan': '%',
    'semesta': (0, 100),
    'label': {
        'Rendah': lambda x: bahu_kiri(x, 20, 40),
        'Normal': lambda x: segitiga(x, 30, 50, 70),
        'Tinggi': lambda x: bahu_kanan(x, 60, 80)
    }
}

def fuzzifikasi(x, variabel):
    lo, hi = variabel['semesta']
    if not np.isfinite(x) or not lo <= x <= hi:
        raise ValueError('Input di luar semesta')
    return {label: float(f(x))
            for label, f in variabel['label'].items()}

def uji(variabel, data, nama):
    labels = list(variabel['label'])
    print(variabel['nama'])
    print('Input | ' + ' | '.join(labels) + ' | Dominan')
    rows = []
    for x in data:
        h = fuzzifikasi(x, variabel)
        dominan = '/'.join(k for k, v in h.items()
                           if np.isclose(v, max(h.values())))
        print(f'{x:g} | ' + ' | '.join(f'{v:.3f}' for v in h.values())
              + ' | ' + dominan)
        rows.append([x, *h.values()])
    np.savetxt(OUT / f'{nama}.csv', rows, delimiter=',',
               header='input,' + ','.join(labels), comments='')
    x = np.linspace(*variabel['semesta'], 1001)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for label, f in variabel['label'].items():
        ax.plot(x, f(x), label=label)
    ax.set(xlabel=f"{variabel['nama']} ({variabel['satuan']})",
           ylabel='Derajat keanggotaan', title=variabel['nama'],
           ylim=(-.05, 1.05))
    ax.grid(alpha=.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / f'{nama}.png', dpi=200)
    plt.close(fig)

if __name__ == '__main__':
    uji(waktu, [1, 2.5, 3.5, 5, 6.5, 7.5, 9], 'p2_waktu')
    uji(cpu, [10, 35, 50, 65, 75, 95], 'p2_cpu')
