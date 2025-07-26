# Belajar Control flow
# Operator: ==, !=, >, <, >=, <=

umur = 18
nama = "Budi"

# If condition (Kondisi Jika)
if umur > 18:
    print("Lebih besar")
    print("Lebih besar")
    
if umur >= 18:
    print("Lebih besar sama dengan")

if umur == 18:
    print("Sama dengan")

if umur <= 18:
    print("Lebih kecil sama dengan")
    
if umur < 18:
    print("Lebih kecil sama dengan") 

if umur != 18:
    print("Tidak sama dengan")        

print("=============================================")
# Else Condition (Kondisi selain dari kondisi jika)

if umur > 18:
    print("Lebih besar")
else:
    print("Besar")
    
if nama == "Budi":
    print("Nama saya")
else:
    print("Bukan nama saya")      
    
if nama != "Budi":
    print("Nama saya")
else:
    print("Bukan nama saya")            
    
# TODO (Latihan) Melengkapi Operator codition
    
    
print("===============================================")
# Elseif condition

if umur > 18:
    print("Dewasa")
elif umur < 18:
    print("Bocil")
else:
    print("Bayi")            