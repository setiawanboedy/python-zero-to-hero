# latihan_exception_handling.py
# Latihan exception handling dan penggabungan materi sebelumnya

# Latihan 1: tangani error saat mengakses index list yang tidak ada
data = [1, 2, 3]
try:
    print(data[5])  # Index 5 tidak ada
except IndexError:
    print("Error: Index tidak ditemukan!")

# Latihan 2: tangani error saat mengakses key dictionary yang tidak ada
mahasiswa = {"nama": "Budi", "umur": 20}
try:
    print(mahasiswa["alamat"])
except KeyError:
    print("Error: Key 'alamat' tidak ada di dictionary!")

# Latihan 3: buat fungsi kalkulator sederhana dengan exception handling
def kalkulator(a, b, operasi):
    try:
        if operasi == "+":
            return a + b
        elif operasi == "-":
            return a - b
        elif operasi == "*":
            return a * b
        elif operasi == "/":
            if b == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
            return a / b
        else:
            raise ValueError("Operasi tidak+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ valid!")
    except Exception as e:
        return f"Error: {e}"

print(kalkulator(10, 2, "+"))   # 12
print(kalkulator(10, 0, "/"))   # Error: Tidak bisa membagi dengan nol!
print(kalkulator(10, 2, "%"))   # Error: Operasi tidak valid!

# Latihan 4: validasi input dengan multiple exception
def input_angka():
    while True:
        try:
            angka = int(input("Masukkan angka (1-100): "))
            if angka < 1 or angka > 100:
                raise ValueError("Angka harus antara 1-100!")
            return angka
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nProgram dihentikan!")
            break

# Latihan 5: baca file dengan exception handling
def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: File tidak ditemukan!"
    except PermissionError:
        return "Error: Tidak ada izin untuk membaca file!"
    except Exception as e:
        return f"Error tidak diketahui: {e}"

print(baca_file("file_tidak_ada.txt"))

# Latihan 6: validasi data mahasiswa dengan custom exception
class DataMahasiswaError(Exception):
    pass

def validasi_mahasiswa(data):
    try:
        if "nama" not in data:
            raise DataMahasiswaError("Nama harus diisi!")
        if "umur" not in data:
            raise DataMahasiswaError("Umur harus diisi!")
        if data["umur"] < 15 or data["umur"] > 50:
            raise DataMahasiswaError("Umur harus antara 15-50!")
        return "Data valid!"
    except DataMahasiswaError as e:
        return f"Error validasi: {e}"

# Test validasi
data1 = {"nama": "Andi"}  # Tidak ada umur
data2 = {"nama": "Budi", "umur": 60}  # Umur terlalu besar
data3 = {"nama": "Siti", "umur": 20}  # Data valid

print(validasi_mahasiswa(data1))
print(validasi_mahasiswa(data2))
print(validasi_mahasiswa(data3))
