# belajar_dictionary.py
# Contoh penggunaan Dictionary dalam Python
# Dictionary adalah struktur data yang menyimpan pasangan key-value

# Membuat dictionary
mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika"
}
print("Data mahasiswa:", mahasiswa)

# Mengakses nilai berdasarkan key
print("Nama:", mahasiswa["nama"])

# Menambah dan mengubah data
mahasiswa["angkatan"] = 2022  # Menambah key baru
mahasiswa["umur"] = 21        # Mengubah nilai
print("Setelah update:", mahasiswa)

# Menghapus data
mahasiswa.pop("jurusan")
print("Setelah hapus jurusan:", mahasiswa)

# Iterasi dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)

# List of dictionary
list_mahasiswa = [
    {"nama": "Budi", "umur": 19},
    {"nama": "Siti", "umur": 20}
]
print("List mahasiswa:", list_mahasiswa)
