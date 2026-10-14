CREATE DATABASE IF NOT EXISTS fuzzy_modul1;
USE fuzzy_modul1;
CREATE TABLE IF NOT EXISTS usia_bayi (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usia_min DECIMAL(6,2) NOT NULL,
  usia_max DECIMAL(6,2) NOT NULL,
  nilai_fuzzy VARCHAR(60) NOT NULL,
  CHECK (usia_min < usia_max)
);
DELETE FROM usia_bayi;
INSERT INTO usia_bayi (usia_min, usia_max, nilai_fuzzy) VALUES
(0, 2, 'satu'),
(2, 5, 'fungsi_bayi_turun'),
(5, 150, 'nol');
CREATE TABLE IF NOT EXISTS usia_anak (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usia_min DECIMAL(6,2) NOT NULL,
  usia_max DECIMAL(6,2) NOT NULL,
  nilai_fuzzy VARCHAR(60) NOT NULL,
  CHECK (usia_min < usia_max)
);
DELETE FROM usia_anak;
INSERT INTO usia_anak (usia_min, usia_max, nilai_fuzzy) VALUES
(0, 6, 'nol'),
(6, 8, 'fungsi_anak_naik'),
(8, 9, 'satu'),
(9, 11, 'fungsi_anak_turun'),
(11, 150, 'nol');
CREATE TABLE IF NOT EXISTS usia_remaja (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usia_min DECIMAL(6,2) NOT NULL,
  usia_max DECIMAL(6,2) NOT NULL,
  nilai_fuzzy VARCHAR(60) NOT NULL,
  CHECK (usia_min < usia_max)
);
DELETE FROM usia_remaja;
INSERT INTO usia_remaja (usia_min, usia_max, nilai_fuzzy) VALUES
(0, 10, 'nol'),
(10, 12, 'fungsi_remaja_naik'),
(12, 17, 'satu'),
(17, 19, 'fungsi_remaja_turun'),
(19, 150, 'nol');
CREATE TABLE IF NOT EXISTS usia_pemuda (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usia_min DECIMAL(6,2) NOT NULL,
  usia_max DECIMAL(6,2) NOT NULL,
  nilai_fuzzy VARCHAR(60) NOT NULL,
  CHECK (usia_min < usia_max)
);
DELETE FROM usia_pemuda;
INSERT INTO usia_pemuda (usia_min, usia_max, nilai_fuzzy) VALUES
(0, 15, 'nol'),
(15, 17, 'fungsi_pemuda_naik'),
(17, 22, 'satu'),
(22, 24, 'fungsi_pemuda_turun'),
(24, 150, 'nol');
CREATE TABLE IF NOT EXISTS usia_dewasa (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usia_min DECIMAL(6,2) NOT NULL,
  usia_max DECIMAL(6,2) NOT NULL,
  nilai_fuzzy VARCHAR(60) NOT NULL,
  CHECK (usia_min < usia_max)
);
DELETE FROM usia_dewasa;
INSERT INTO usia_dewasa (usia_min, usia_max, nilai_fuzzy) VALUES
(0, 20, 'nol'),
(20, 22, 'fungsi_dewasa_naik'),
(22, 63, 'satu'),
(63, 65, 'fungsi_dewasa_turun'),
(65, 150, 'nol');
CREATE TABLE IF NOT EXISTS usia_lansia (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usia_min DECIMAL(6,2) NOT NULL,
  usia_max DECIMAL(6,2) NOT NULL,
  nilai_fuzzy VARCHAR(60) NOT NULL,
  CHECK (usia_min < usia_max)
);
DELETE FROM usia_lansia;
INSERT INTO usia_lansia (usia_min, usia_max, nilai_fuzzy) VALUES
(0, 65, 'nol'),
(65, 70, 'fungsi_lansia_naik'),
(70, 95, 'satu'),
(95, 100, 'fungsi_lansia_turun'),
(100, 150, 'nol');
