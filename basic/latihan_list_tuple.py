# latihan_list_tuple.py
# Latihan sederhana dan medium penggunaan List & Tuple

# Latihan 1: buat list berisi 3 nama teman, tampilkan satu per satu
nama_teman = ["Budi", "Siti", "Andi"]
for nama in nama_teman:
    print("Teman:", nama)

# Latihan 2: tambahkan satu nama ke list, lalu tampilkan semua
nama_teman.append("Rina")
print("Setelah ditambah:", nama_teman)

# Latihan 3: buat tuple berisi 3 angka, tampilkan jumlahnya
angka_tuple = (5, 7, 9)
print("Jumlah tuple:", sum(angka_tuple))

# Latihan 4 (medium): ubah semua elemen list menjadi huruf besar
for i in range(len(nama_teman)):
    nama_teman[i] = nama_teman[i].upper()
print("Huruf besar:", nama_teman)

# Latihan 5 (medium): gabungkan dua list menjadi satu
buah1 = ["apel", "jeruk"]
buah2 = ["mangga", "pisang"]
gabungan = buah1 + buah2
print("Gabungan list:", gabungan)

# Latihan 6 (medium): slicing tuple
angka = (1, 2, 3, 4, 5)
print("Slicing 2-4:", angka[1:4])

# Latihan 7 (loop + operator): hitung jumlah angka genap di list
angka_list = [2, 5, 8, 11, 14]
jumlah_genap = 0
for n in angka_list:
    if n % 2 == 0:
        jumlah_genap += 1
print("Jumlah angka genap:", jumlah_genap)

# Latihan 8 (fungsi): buat fungsi untuk mencari nilai maksimum di tuple
def cari_maks(tup):
    maks = tup[0]
    for val in tup:
        if val > maks:
            maks = val
    return maks

data = (7, 3, 12, 5)
print("Nilai maksimum:", cari_maks(data))

# Latihan 9 (controlflow): cek apakah semua elemen list lebih dari 0
angka_cek = [1, 2, 3, 4]
semua_positif = True
for a in angka_cek:
    if a <= 0:
        semua_positif = False
        break
if semua_positif:
    print("Semua elemen positif")
else:
    print("Ada elemen yang tidak positif")

# Latihan 10 (loop + fungsi + operator): jumlahkan semua angka pada list yang lebih dari 5
def jumlah_lebih_dari_lima(lst):
    total = 0
    for x in lst:
        if x > 5:
            total += x
    return total

angka_latihan = [2, 6, 8, 3, 10]
print("Jumlah angka > 5:", jumlah_lebih_dari_lima(angka_latihan))
