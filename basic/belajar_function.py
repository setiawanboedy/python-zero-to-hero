# belajar_function.py
# Contoh penggunaan function (fungsi) dalam Python
# Fungsi digunakan untuk mengelompokkan kode agar mudah digunakan kembali

# Fungsi sederhana tanpa parameter
# Fungsi ini hanya menampilkan pesan

def sapa():
    print("Halo, selamat datang di Python!")

sapa()  # Memanggil fungsi sapa

# Fungsi dengan parameter
# Fungsi ini menerima satu parameter dan menampilkannya

def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Andi")

# Fungsi dengan return value
# Fungsi ini mengembalikan hasil penjumlahan dua angka

def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print("Hasil penjumlahan:", hasil)
