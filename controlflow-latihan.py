# Latihan Control flow

tinggi = int(input("Masukkan tinggi badan: "))
ket_tinggi = ""

if tinggi > 170:
    print("Tinggi sekali")
    ket_tinggi = "Tinggi sekali"
elif tinggi >= 150:
    print("Tinggi sedang")
    ket_tinggi = "Tinggi sedang"
else:
    print("Pendek")
    ket_tinggi = "Pendek"

nama = str(input("Masukkan nama: "))
ket_nama = ""

if nama == "agis":
    print("Pintar")
    ket_nama = "Pintar"
elif nama == "budi":
    print("cerdas")   
    ket_nama = "cerdas" 
else:
    print("Bodoh")    
    ket_nama = "Bodoh"    

print(f"Nama saya {nama} tinggi badan saya {tinggi}")    
print(f"Nama saya {nama} saya orangnya {ket_nama} tinggi badan saya {tinggi} ({ket_tinggi})")    