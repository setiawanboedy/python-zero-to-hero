# belajar_exception_handling.py
# Contoh penggunaan Exception Handling dalam Python
# Exception handling digunakan untuk menangani error/kesalahan saat program berjalan

# Try-except sederhana
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Input harus berupa angka!")

# Try-except-finally
try:
    file = open("test.txt", "r")
    print("File berhasil dibuka")
except FileNotFoundError:
    print("Error: File tidak ditemukan!")
finally:
    print("Blok finally selalu dijalankan")

# Try-except-else
try:
    x = 5
    y = 2
    hasil = x / y
except ZeroDivisionError:
    print("Pembagian dengan nol!")
else:
    print("Tidak ada error, hasil:", hasil)

# Raise exception sendiri
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    elif umur > 150:
        raise ValueError("Umur terlalu besar!")
    else:
        print("Umur valid:", umur)

try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)
