def rata_rata(data):
    """Menghitung rata-rata data."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Mengembalikan list nilai yang lulus."""
    lulus = []

    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)

    return lulus


# =====================================
# PROGRAM UTAMA
# =====================================

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

print("=" * 45)
print("      ANALISIS NILAI MAHASISWA")
print("=" * 45)

print(f"Daftar nilai       : {nilai}")
print(f"Banyak data        : {banyak_data}")

print("\nSTATISTIK")
print("-" * 45)
print(f"Total nilai        : {total}")
print(f"Rata-rata          : {rata:.2f}")
print(f"Nilai minimum      : {minimum}")
print(f"Nilai maksimum     : {maksimum}")

print("\nKELULUSAN")
print("-" * 45)
print(f"Nilai lulus        : {lulus}")
print(f"Jumlah lulus       : {jumlah_lulus}")
print(f"Jumlah belum lulus : {jumlah_belum_lulus}")

print("=" * 45)

# =====================================
# TEST CASE WAJIB
# =====================================

print("\nTEST CASE WAJIB")
print("=" * 45)

# Test 1: Rata-rata
data1 = [60, 70, 80]
print(f"Data               : {data1}")
print(f"Rata-rata          : {rata_rata(data1):.2f}")
print("Expected           : 70.00")
print()

# Test 2: Minimum/Maksimum
print(f"Data               : {data1}")
print(f"Minimum/Maksimum   : {min(data1)} / {max(data1)}")
print("Expected           : 60 / 80")
print()

# Test 3: Jumlah lulus
print(f"Data               : {data1}")
print(f"Jumlah lulus       : {len(nilai_lulus(data1))}")
print("Expected           : 3")
print()

# Test 4: Batas kelulusan
data2 = [59, 60, 61]
print(f"Data               : {data2}")
print(f"Jumlah lulus       : {len(nilai_lulus(data2))}")
print("Expected           : 2")
print()

# Test 5: List kosong
data3 = []
print(f"Data               : {data3}")
print(f"Rata-rata          : {rata_rata(data3):.2f}")
print("Expected           : Tidak error")
print()

print("=" * 45)
print("Semua test case selesai dijalankan.")
print("=" * 45)