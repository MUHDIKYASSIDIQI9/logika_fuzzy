from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).parent / 'hasil'
OUT.mkdir(exist_ok=True)

def segitiga(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def trapesium(x, a, b, c, d):
    return np.maximum(0, np.minimum(1,
        np.minimum((x-a)/(b-a), (d-x)/(d-c))))

def operasi(a, b):
    return {
        'Min': np.minimum(a, b),
        'Product': a*b,
        'Bounded Diff': np.maximum(0, a+b-1),
        'Max': np.maximum(a, b),
        'Alg. Sum': a+b-a*b,
        'Bounded Sum': np.minimum(1, a+b),
        'NOT A': 1-a
    }

def plot_operasi(x, a, b, nama, judul):
    h = operasi(a, b)
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0, 0].plot(x, a, label='A')
    axes[0, 0].plot(x, b, label='B')
    axes[0, 0].plot(x, h['NOT A'], '--', label='NOT A')
    for label in ['Min', 'Product', 'Bounded Diff']:
        axes[0, 1].plot(x, h[label], label=label)
    for label in ['Max', 'Alg. Sum', 'Bounded Sum']:
        axes[1, 0].plot(x, h[label], label=label)
    axes[1, 1].fill_between(x, h['Min'], alpha=.4,
                            label='Irisan Min')
    axes[1, 1].plot(x, h['Max'], label='Gabungan Max')
    for ax, title in zip(axes.flat, ['Himpunan dasar dan komplemen',
            'Irisan AND', 'Gabungan OR', 'Irisan dan gabungan']):
        ax.set(title=title, xlabel='x', ylabel='Keanggotaan',
               ylim=(-.05, 1.05))
        ax.grid(alpha=.3)
        ax.legend(fontsize=8)
    fig.suptitle(judul)
    fig.tight_layout()
    fig.savefig(OUT / f'{nama}.png', dpi=200)
    plt.close(fig)

if __name__ == '__main__':
    x = np.linspace(0, 10, 1001)
    plot_operasi(x, segitiga(x, 1, 3, 6), segitiga(x, 4, 7, 9),
                 'p4_contoh', 'Operasi himpunan fuzzy')
    print('A | B | Min | Product | Bounded Diff | '
          'Max | Alg. Sum | Bounded Sum')
    for a, b in [(.9,.9), (.7,.4), (.5,.5), (.3,.2), (0,.85)]:
        h = operasi(a, b)
        print(f'{a:.2f} | {b:.2f} | ' + ' | '.join(
            f'{h[k]:.2f}' for k in list(h)[:-1]))
    x = np.linspace(0, 100, 1001)
    a, b = segitiga(x, 30, 60, 90), trapesium(x, 40, 55, 75, 95)
    plot_operasi(x, a, b, 'p4_bandwidth',
                 'Evaluasi bandwidth jaringan kampus')
    data = np.array([35., 50., 65., 80.])
    a = segitiga(data, 30, 60, 90)
    b = trapesium(data, 40, 55, 75, 95)
    h = operasi(a, b)
    keys = ['Min', 'Product', 'Max', 'Alg. Sum', 'NOT A']
    rows = np.c_[data, a, b, *[h[k] for k in keys]]
    np.savetxt(OUT / 'p4_bandwidth.csv', rows, delimiter=',',
               header='Mbps,A,B,Min,Product,Max,AlgSum,NotA', comments='')
    print('Mbps | A | B | Min | Product | Max | Alg. Sum | NOT A')
    for row in rows:
        print(' | '.join(f'{v:.4f}' for v in row))
