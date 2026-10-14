import os
import math
from functools import partial
from pathlib import Path
import mysql.connector

# Parameter mengikuti tugas usia, berbentuk trapesium.
PARAM = {
    'bayi': (0, 0, 2, 5),
    'anak': (6, 8, 9, 11),
    'remaja': (10, 12, 17, 19),
    'pemuda': (15, 17, 22, 24),
    'dewasa': (20, 22, 63, 65),
    'lansia': (65, 70, 95, 100)
}
UJI = {
    'bayi': [1, 4], 'anak': [7, 10],
    'remaja': [11, 18], 'pemuda': [16, 23],
    'dewasa': [21, 64], 'lansia': [68, 96]
}

def naik(x, a, b):
    return (x - a) / (b - a)

def turun(x, c, d):
    return (d - x) / (d - c)

FUNGSI = {
    'nol': lambda x: 0.0,
    'satu': lambda x: 1.0
}
for kategori, (a, b, c, d) in PARAM.items():
    if a < b:
        FUNGSI[f'fungsi_{kategori}_naik'] = partial(naik, a=a, b=b)
    FUNGSI[f'fungsi_{kategori}_turun'] = partial(turun, c=c, d=d)

def fuzzifikasi_usia(x, kategori, koneksi):
    if kategori not in PARAM:
        raise ValueError('Kategori tidak dikenal')
    if not math.isfinite(x) or not 0 <= x <= 150:
        raise ValueError('Usia harus berada pada [0, 150]')
    # Nama tabel hanya berasal dari kategori yang telah divalidasi.
    sql = f'''
        SELECT usia_min, usia_max, nilai_fuzzy
        FROM usia_{kategori}
        WHERE %s >= usia_min
          AND (%s < usia_max OR (%s = 150 AND usia_max = 150))
        ORDER BY usia_min
    '''
    with koneksi.cursor() as cursor:
        cursor.execute(sql, (x, x, x))
        rows = cursor.fetchall()
    if len(rows) != 1:
        raise RuntimeError('Interval database kosong atau bertumpuk')
    lo, hi, nama = rows[0]
    if nama not in FUNGSI:
        raise KeyError(f'Fungsi belum terdaftar: {nama}')
    mu = float(FUNGSI[nama](x))
    if not 0 <= mu <= 1:
        raise ValueError('Derajat keanggotaan tidak valid')
    return lo, hi, nama, mu

def main():
    # Jalankan SQL terlebih dahulu melalui phpMyAdmin.
    koneksi = mysql.connector.connect(
        host=os.getenv('FUZZY_DB_HOST', 'localhost'),
        port=int(os.getenv('FUZZY_DB_PORT', '3306')),
        user=os.getenv('FUZZY_DB_USER', 'root'),
        password=os.getenv('FUZZY_DB_PASSWORD', ''),
        database='fuzzy_modul1'
    )
    try:
        print('Kategori | Usia | Interval | Fungsi | mu')
        rows = []
        for kategori, usia_uji in UJI.items():
            for x in usia_uji:
                lo, hi, nama, mu = fuzzifikasi_usia(x, kategori, koneksi)
                print(f'{kategori} | {x} | [{lo},{hi}) | '
                      f'{nama} | {mu:.4f}')
                rows.append(
                    f'{kategori},{x},{lo},{hi},{nama},{mu:.4f}')
        out = Path(__file__).parent / 'hasil'
        out.mkdir(exist_ok=True)
        (out / 'p3_mysql.csv').write_text(
            'kategori,usia,min,max,fungsi,mu\n' + '\n'.join(rows),
            encoding='utf-8'
        )
    finally:
        koneksi.close()

if __name__ == '__main__':
    main()
