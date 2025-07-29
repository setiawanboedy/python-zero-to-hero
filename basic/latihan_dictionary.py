# latihan_dictionary.py
# Latihan dictionary dan penggabungan materi sebelumnya

# Latihan 1: buat dictionary biodata, tampilkan semua datanya
biodata = {"nama": "Rina", "umur": 22, "hobi": "Membaca"}
for k, v in biodata.items():
    print(f"{k}: {v}")

# Latihan 2: update dan hapus key pada dictionary
biodata["hobi"] = "Menulis"
del biodata["umur"]
print("Setelah update dan hapus:", biodata)

# Latihan 3: buat list of dictionary berisi data 3 teman, tampilkan nama saja
teman = [
    {"nama": "Budi", "umur": 20},
    {"nama": "Siti", "umur": 21},
    {"nama": "Andi", "umur": 19}
]
for t in teman:
    print("Nama teman:", t["nama"])

# Latihan 4 (gabungan): hitung rata-rata umur dari list of dictionary
jumlah = 0
for t in teman:
    jumlah += t["umur"]
rata2 = jumlah / len(teman)
print("Rata-rata umur:", rata2)

# Latihan 5 (gabungan): buat fungsi yang menerima list of dictionary mahasiswa, dan mengembalikan nama mahasiswa dengan umur tertua

def cari_tertua(data):
    tertua = data[0]
    for mhs in data:
        if mhs["umur"] > tertua["umur"]:
            tertua = mhs
    return tertua["nama"]

print("Mahasiswa tertua:", cari_tertua(teman))
