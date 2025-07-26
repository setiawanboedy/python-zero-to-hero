# Latihan looping while

angka = 1
jumlah = 10

while angka <= jumlah:
    if angka % 2 == 0:
        print("angka genap: ", angka)
    elif angka == 5:
        continue
    elif angka == 7:
        break
    else:
        print("angka ganjil: ", angka)    
        
    angka += 1