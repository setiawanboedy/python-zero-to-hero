# try and exception

# try -> coba dulu code, kalau erro ditangkap oleh -> exception

# Struktur code try and exception
try:
    # code
    print("Eksekusi kode")
except Exception as e:
    # exception
    print("Tangkap kode: ", e)
    
# finally akan selalu dieksekusi     
isSuccesNotifikasi = False    
try:
    # code
    print("Eksekusi kode")
    isSuccesNotifikasi = True
except Exception as e:
    # exception
    isSuccesNotifikasi = True
    print("Tangkap kode: ", e)
finally:
    isSuccesNotifikasi = False
    print("Block finally selalu dijalankan")
    
print("==========================================")
# Exception umum untuk menangkap semua error tidak spesifik
# Dan exception spesifik kalau tau error codenya
try:
    a = 5
    b = 0
    hasil = a/b
# except ZeroDivisionError:
#     print("Tidak bisa dibagi 0")
except Exception as e:
    print("Error: ", e)         
    
print("==========================================")

# try dan exception dengan lempar error ke exception
def cek_umur(umur):
    try:
        if umur < 0:
            raise ValueError("Umur tidak boleh negatif!")
        elif umur > 150:
            raise ValueError("Umur terlalu tua!")
        else:
            print("Umur sudah valid, yaitu: ", umur)
    except ValueError as error:
        print("Error: ", error)
        
cek_umur(20)        

print("==========================================")
# Custom exception
class NilaiError(Exception):
    pass

def cek_nilai(nilai):
    try:
        if nilai < 60:
            raise NilaiError("Nilai kurang!")
        elif nilai > 100:
            raise NilaiError("Nilai kelebihan!")
        else:
            print("Nilai lulus: ", nilai)
    except NilaiError as error:
        print("Error: ", error)

cek_nilai(60)
print("==========================================")

try:
    angka = 1
    jumlah = 10

    while angka <= jumlah:
        
        if angka % 2 == 0:
            print("angka genap: ", angka)
        elif angka == 5:
            angka += 1
            continue
        elif angka == 7:
            break
        else:
            print("angka ganjil: ", angka)    
        angka += 1
            
except Exception as error:
    print("Error: ", error)            
    
print("==========================================")

# Latihan

def kalkulator(a, operasi, b):
    try:
        if operasi == "+":
            return a+b
        elif operasi == "-":
            return a-b
        elif operasi == "*":
            return a*b
        elif operasi == "/":
            if b == 0:
                raise ZeroDivisionError("Tidak bisa dibagi 0")
            else:
                return a/b
        else:
            raise ValueError("Operasi tidak valid")    
        
    except Exception as error:
        return f"Error: {error}"
        
print(kalkulator(2,"+",3))            
print(kalkulator(2,"-",3))            
print(kalkulator(2,"*",3))            
print(kalkulator(2,"/",3))            
print(kalkulator(2,"/",0))            
print(kalkulator(2,".",0))            