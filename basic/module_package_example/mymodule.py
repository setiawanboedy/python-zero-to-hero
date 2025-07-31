# mymodule.py
# Contoh module sederhana

def salam(nama):
    """Fungsi untuk menyapa"""
    return f"Halo, {nama}! Selamat datang!"

def kali(a, b):
    """Fungsi untuk mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Fungsi untuk membagi dua angka"""
    if b == 0:
        return "Error: Pembagian dengan nol!"
    return a / b

# Variabel dalam module
PI = 3.14159
NAMA_APLIKASI = "Kalkulator Python"

# Kode yang dijalankan saat module diimpor
print(f"Module {__name__} telah diimpor!")

# Kode yang hanya dijalankan jika file ini dijalankan langsung
if __name__ == "__main__":
    print("Module ini dijalankan langsung!")
    print(salam("User"))
    print(f"5 x 3 = {kali(5, 3)}")
