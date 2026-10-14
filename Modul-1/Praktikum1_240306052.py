from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).parent / 'hasil'
OUT.mkdir(exist_ok=True)

def crisp(x, ambang):
    return np.where(np.asarray(x) >= ambang, 1.0, 0.0)

def linear_naik(x, a, b):
    if b <= a:
        raise ValueError('Parameter harus memenuhi a < b')
    return np.clip((np.asarray(x) - a) / (b - a), 0, 1)

def sigmoid(x, k=2.0, pusat=3.5):
    return 1 / (1 + np.exp(-k * (np.asarray(x) - pusat)))

def gambar_rating():
    x = np.linspace(1, 5, 801)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.step(x, crisp(x, 4), where='post', label='Crisp: ambang 4')
    ax.plot(x, linear_naik(x, 2.5, 4.5),
            label='Linear: 2.5 sampai 4.5')
    ax.plot(x, sigmoid(x), label='Sigmoid: k=2; pusat=3.5')
    ax.set(xlabel='Rating layanan', ylabel='Derajat keanggotaan',
           title='Perbandingan crisp, linear, dan sigmoid', ylim=(-.05, 1.05))
    ax.grid(alpha=.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / 'p1_rating.png', dpi=200)
    plt.close(fig)

def tugas_helpdesk():
    data = np.array([2, 4, 6, 7.9, 8, 8.1, 10, 12, 16, 24])
    c, f = crisp(data, 8), linear_naik(data, 4, 12)
    print('Jam | Crisp | Fuzzy kritis')
    for x, a, b in zip(data, c, f):
        print(f'{x:4.1f} | {a:.0f} | {b:.4f}')
    np.savetxt(OUT / 'p1_helpdesk.csv', np.c_[data, c, f],
               delimiter=',', header='jam,crisp,fuzzy', comments='')
    x = np.linspace(0, 24, 1201)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.step(x, crisp(x, 8), where='post', label='Crisp: ambang 8 jam')
    ax.plot(x, linear_naik(x, 4, 12), label='Fuzzy: transisi 4–12 jam')
    ax.scatter(data, f, s=25)
    ax.set(xlabel='Waktu tunggu (jam)', ylabel='Derajat kritis',
           title='Prioritas tiket helpdesk TI', ylim=(-.05, 1.05))
    ax.grid(alpha=.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / 'p1_helpdesk.png', dpi=200)
    plt.close(fig)

if __name__ == '__main__':
    gambar_rating()
    print('Rating | Crisp | Linear | Sigmoid')
    for x in [3.8, 3.9, 3.99, 4, 4.01, 4.2]:
        print(f'{x:.2f} | {crisp(x, 4):.0f} | '
              f'{linear_naik(x, 2.5, 4.5):.3f} | {sigmoid(x):.3f}')
    tugas_helpdesk()
