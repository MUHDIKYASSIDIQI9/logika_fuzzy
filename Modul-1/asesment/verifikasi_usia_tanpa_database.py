from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

PARAM = {
    'bayi': (0, 0, 2, 5), 'anak': (6, 8, 9, 11),
    'remaja': (10, 12, 17, 19), 'pemuda': (15, 17, 22, 24),
    'dewasa': (20, 22, 63, 65), 'lansia': (65, 70, 95, 100)
}
UJI = {
    'bayi': [1, 4], 'anak': [7, 10], 'remaja': [11, 18],
    'pemuda': [16, 23], 'dewasa': [21, 64], 'lansia': [68, 96]
}

def trapesium(x, a, b, c, d):
    x = np.asarray(x, dtype=float)
    naik = np.ones_like(x) if a == b else (x-a)/(b-a)
    turun = (d-x)/(d-c)
    return np.maximum(0, np.minimum(1, np.minimum(naik, turun)))

if __name__ == '__main__':
    print('Acuan Python; bukan bukti pengujian integrasi MySQL.')
    fig, axes = plt.subplots(3, 2, figsize=(10, 8))
    for ax, (label, param) in zip(axes.flat, PARAM.items()):
        a, b, c, d = param
        for x in UJI[label]:
            print(f'{label} | {x} | {trapesium(x, *param):.4f}')
        x = np.linspace(max(0, a-2), d+2, 801)
        ax.plot(x, trapesium(x, *param), linewidth=2)
        ax.scatter(UJI[label],
                   [trapesium(z, *param) for z in UJI[label]])
        ax.set(title=label.capitalize(), xlabel='Usia (tahun)',
               ylabel='Keanggotaan', ylim=(-.05, 1.05))
        ax.grid(alpha=.3)
    fig.tight_layout()
    out = Path(__file__).parent / 'hasil'
    out.mkdir(exist_ok=True)
    fig.savefig(out / 'p3_usia.png', dpi=200)
    plt.close(fig)
