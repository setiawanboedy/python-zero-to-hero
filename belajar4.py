# Function

# struktur fungsi
def nama_fungsi():
    print("aksi")
    
# contoh medium

def cek_bilangan_ganjil_genap():
    angka = 1
    jumlah = 10

    while angka <= jumlah:
        angka += 1
        
        if angka % 2 == 0:
            print("angka genap: ", angka)
        elif angka == 5:
            continue
        elif angka == 7:
            break
        else:
            print("angka ganjil: ", angka)    
            

cek_bilangan_ganjil_genap()        

print("=====================================")
# contoh simple

def sapa_nama(nama):
    print(f"Halo {nama}!")
    
    
sapa_nama("agis")
sapa_nama("budi")

print("==============================")
# tanpa return
def tambah(a, b):
    hasil = a+b
    print(hasil)    
    
tambah(2, 4) # hanya menampilkan nilai tapi tidak ada kembalian
tambah(99, 43)    

print("======================================")
# return value

def kali(a, b):
    hasil = a*b
    return hasil

kali(4, 5) # hanya kembalikan nilai tidak ditampilkan
hasil_kali = kali(4, 5)
print(hasil_kali)

hasil_kurang = hasil_kali - 10
print(hasil_kurang)

print("======================================")
def list_string(cari_kata):
    list_string = ["satu", "dua", "tiga"]
    angka_str = ""
    for angka_string in list_string:
        if angka_string == cari_kata:
            angka_str = angka_string
        
    return angka_str
        
print(list_string("satu") )    
print("======================================")

def jumlah_list_int(list):
    jumlah = 0
    
    for angka_int in list:
        jumlah += angka_int
    return jumlah    

list_int = [4, 2, 3]
jumlah_list = jumlah_list_int(list_int)
print(jumlah_list)

print("==========================")

def len_f(list):
    count =0
    for _ in list:
        count+=1
    return count    

def rata_rata(list):
    # rata = sum(list)/len(list)
    rata = jumlah_list_int(list)/len_f(list)
    return rata

jumlah_rata = rata_rata(list_int)
print(jumlah_rata)

