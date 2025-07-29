# Dictionary

# "dictionary":"kamus"
# { key : value }
{"dictionary" : "kamus"}
{"dictionary" : "kamus", "book": "buku"}

dictionary = {"dictionary" : "kamus1", "book": "buku"}

print(dictionary["dictionary"])
print(dictionary["book"])

print("========================================")
# print key dan value
for k, v in dictionary.items():
    print(f"key: {k} dan value: {v}")

# print hanya key    
for k in dictionary:
    print("key: ",k)
    

dict_gabungan = {"satu" : 1, 4: 3, "empat": 4}
print(dict_gabungan["empat"])

fruits = [
    {"nama buah": "Apel", "berat": 4},
    {"nama buah": "Semangka", "berat": 14},
    {"nama buah": "Anggur", "berat": 24},
]

for buah in fruits:
    print(f"nama buah: {buah["nama buah"]}, berat: {buah["berat"]} kg" )

print("=========================================")
# menghitung rata2 berat buah

jumlah_kalkulasi = 0
jumlah_data = 0

for buah in fruits:
    jumlah_kalkulasi += buah["berat"]
    jumlah_data += 1

jumlah_rata2 = jumlah_kalkulasi/jumlah_data  
print(jumlah_rata2)

