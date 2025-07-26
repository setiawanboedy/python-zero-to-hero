# latihan_function.py
# Latihan sederhana penggunaan function di Python

# Latihan 1: fungsi tanpa parameter
# Buat fungsi yang menampilkan "Belajar Python itu mudah!"
def motivasi():
    print("Belajar Python itu mudah!")

motivasi()

# Latihan 2: fungsi dengan parameter
# Buat fungsi yang menerima nama dan menampilkan "Selamat datang, <nama>!"
def selamat_datang(nama):
    print(f"Selamat datang, {nama}!")

selamat_datang("Budi")

# Latihan 3: fungsi dengan return value
# Buat fungsi yang mengalikan dua angka dan mengembalikan hasilnya
def kali(a, b):
    return a * b

hasil = kali(4, 6)
print("Hasil kali:", hasil)

# Latihan 4 (medium): fungsi untuk cek bilangan genap/ganjil
def cek_genap_ganjil(angka):
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")

cek_genap_ganjil(7)

# Latihan 5 (medium): fungsi untuk menghitung rata-rata dari list angka
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

angka_list = [10, 20, 30, 40]
print("Rata-rata:", rata_rata(angka_list))
