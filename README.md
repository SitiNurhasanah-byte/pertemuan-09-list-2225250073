# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Siti Nurhasanah  
**NIM:** 2225250073
**Kelas:** 3B  

## Tujuan

Mengolah kumpulan data numerik menggunakan list Python.

---

## Struktur Program

### Latihan

| File | Deskripsi |
|--------|--------|
| `01_buat_list.py` | Membuat list dan menampilkan jumlah elemen |
| `02_indeks_slicing.py` | Menggunakan indeks dan slicing pada list |
| `03_manipulasi_list.py` | Mengubah, menambah, menyisipkan, dan menghapus elemen list |
| `04_agregasi_nilai.py` | Menghitung total, rata-rata, minimum, dan maksimum |
| `05_filter_kelulusan.py` | Menyaring nilai yang memenuhi batas kelulusan |
| `06_fungsi_statistik.py` | Membuat fungsi rata-rata untuk list |

### Praktik

| File | Deskripsi |
|--------|--------|
| `praktik/analisis_nilai_mahasiswa.py` | Analisis data nilai mahasiswa dan pengujian test case |

---

## Cara Menjalankan

Jalankan program utama menggunakan terminal:

python praktik/analisis_nilai_mahasiswa.py

atau

python3 praktik/analisis_nilai_mahasiswa.py


---

## Hasil Pengujian

| No | Data | Yang Diperiksa | Hasil Diharapkan | Hasil Aktual | Status |
|----|------|------|------|------|------|
| 1 | `[60, 70, 80]` | Rata-rata | `70.00` | `70.00` | ✅ Lulus |
| 2 | `[60, 70, 80]` | Minimum / Maksimum | `60 / 80` | `60 / 80` | ✅ Lulus |
| 3 | `[60, 70, 80]` | Jumlah Lulus | `3` | `3` | ✅ Lulus |
| 4 | `[59, 60, 61]` | Batas Kelulusan 60 | `2 Lulus` | `2 Lulus` | ✅ Lulus |
| 5 | `[]` | Penanganan List Kosong | Tidak Error | Tidak Error | ✅ Lulus |

---

## Hasil Program

Data nilai:

```text
[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
```

Output ringkasan:

```text
=============================================
      ANALISIS NILAI MAHASISWA
=============================================

Daftar nilai       : [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
Banyak data        : 10

STATISTIK
---------------------------------------------
Total nilai        : 695
Rata-rata          : 69.50
Nilai minimum      : 45
Nilai maksimum     : 90

KELULUSAN
---------------------------------------------
Jumlah lulus       : 7
Jumlah belum lulus : 3
=============================================
```

---

## Refleksi

Pada praktikum ini saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel dan memudahkan pengolahan data numerik menggunakan fungsi bawaan Python seperti:

- `len()`
- `sum()`
- `min()`
- `max()`

Selain itu, saya memahami cara melakukan filtering data menggunakan perulangan dan percabangan untuk menentukan data yang memenuhi syarat tertentu.

Kesalahan yang berhasil diperbaiki adalah penanganan list kosong pada fungsi rata-rata. Tanpa pengecekan jumlah data, program dapat mengalami error karena pembagian dengan nol. Masalah tersebut diperbaiki dengan menambahkan kondisi:

```python
if len(data) == 0:
    return 0
```

Sehingga fungsi dapat berjalan dengan baik untuk semua data uji, termasuk list kosong.
