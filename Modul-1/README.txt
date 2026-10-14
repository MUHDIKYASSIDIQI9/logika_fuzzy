MODUL 1 LOGIKA FUZZY
Muh Diky Assidiqi — 240306052

Isi paket
- Praktikum1_240306052.py: rating crisp/linear/sigmoid dan tiket helpdesk.
- Praktikum2_240306052.py: waktu respons dan penggunaan CPU.
- Praktikum3_240306052.sql: enam tabel interval usia untuk MySQL.
- Praktikum3_240306052.py: fuzzifikasi berdasarkan query interval MySQL.
- Praktikum4_240306052.py: operasi fuzzy dan tugas bandwidth.
- Praktikum5_240306052.py: model CPU/RAM/Risiko, tujuh simulasi,
  dan pembacaan hasil pengukuran nyata jika CSV tersedia.
- rekam_data_nyata.py: alat pendamping pengukuran CPU/RAM.
- verifikasi_usia_tanpa_database.py: reproduksi acuan usia tanpa MySQL.
- hasil/: grafik, CSV, dan output terminal yang tersedia.

Persiapan di terminal
pip install numpy matplotlib mysql-connector-python psutil

Jalankan setiap berkas dari folder paket, misalnya:
python Praktikum1_240306052.py

Pengujian MySQL
1. Aktifkan MySQL pada WAMP.
2. Impor Praktikum3_240306052.sql melalui phpMyAdmin.
   SQL menggunakan database fuzzy_modul1 dan mengisi ulang enam tabel
   usia yang namanya tercantum di dalamnya. Periksa sebelum mengimpor
   jika Anda sudah memiliki tabel dengan nama tersebut.
3. Sesuaikan host, port, user, dan password di kode atau variabel
   lingkungan FUZZY_DB_HOST, FUZZY_DB_PORT, FUZZY_DB_USER,
   FUZZY_DB_PASSWORD. Default localhost:3306, root, password kosong.
4. Jalankan python Praktikum3_240306052.py.
5. Cocokkan hasil p3_mysql.csv dengan tabel acuan di laporan.

Status pengujian
- Praktikum 1, 2, 4, 5 telah dieksekusi dengan Python.
- Praktikum 3 telah diuji pada komputer mahasiswa dengan MySQL.
  Seluruh 12 hasil p3_mysql.csv sesuai dengan acuan manual/Python.
- Praktikum 5 memuat lima pengukuran nyata pada laptop yang menjalankan
  server lokal WAMP, ditambah tujuh skenario simulasi yang diberi label.
  Seluruh pengukuran nyata menghasilkan CPU Rendah=1 dan RAM Tinggi=1.
  Data nyata belum mencakup seluruh rentang; simulasi menguji transisi
  dan ekstrem tanpa menggantikan pengukuran nyata.
- Risiko output pada Praktikum 5 baru dirancang. Skor akhir belum
  dihitung karena inferensi dan defuzzifikasi dilanjutkan di Modul 2.

Laporan Word
Cover dibuat minimal agar dapat Anda lengkapi. Bukti hasil MySQL
dan data nyata Praktikum 5 sudah dimasukkan dalam laporan revisi.
