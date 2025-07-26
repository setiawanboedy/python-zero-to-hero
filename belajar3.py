# Loops: for

#example
list_string = ["satu", "dua", "tiga"]
for angka_string in list_string:
    print(angka_string)

print("================================")
    
list_int = [1, 2, 3]
for angka_int in list_int:
    print(angka_int)
  
print("================================")  
    
# gabung
list_gabung = ["satu", 2, "tiga"]
for angka_gabung in list_gabung:
    print(angka_gabung)
    
print("==============================")

# string
nama_string = "agistinus"
for nama in nama_string:
    print(nama)            

print("==============================")

# range
for angka in range(10):
    print(angka)

print("==============================")
for angka_start in range(5, 10):
    print(angka_start)

print("==============================")
for angka_step in range(1, 10, 2):
    print(angka_step)
     
print("==============================")
     
# Manipulasi Loop
jumlah_angka = 10
for angka in list_int:
    # jumlah_angka = jumlah_angka + angka
    jumlah_angka += angka
print(jumlah_angka)

print("==============================")

jumlah = 10
# Bilangan genap
for angka in range(1, jumlah+1):
    if angka % 2 == 0:
        print(f"angka genap: {angka}")
    elif angka == 5:
        continue    # lanjutkan
    elif angka == 7:
        break
    else:
        print(f"angka ganjil: {angka}")    

print("===========================================")
# =================================================
# Loops: while 

angka_start = 10
while angka_start > 0:
    print(angka_start)
    
    angka_start -= 1
print("angka terakhir:")
print(angka_start)    

print("========================================")

list_string = ["saya", "kamu", "dia"]
start = 0
stop = len(list_string)

while start < stop:
    print(list_string[start])
    # if list_string[start] == "kamu":
    #     continue
    start += 1