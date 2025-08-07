# OOP (Object Oriented Programming)

# Contoh object
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def info_bio(self):
        print(f"Hello nama saya {self.nama} dan umur saya {self.umur}!")
        
    def ulang_tahun(self):
        hasil_umur = self.umur + 1
        print(f"Jadi umur saya sekarang {hasil_umur}")    
        
        
orang = Orang("Budi", 38) # Instance
orang.info_bio()
orang.ulang_tahun()

print("============================================")

class Matematika:
    def __init__(self, nama):
        self.nama = nama
        
    def info(self):
        print(f"Ini adalah object {self.nama}")    
    
    def tambah(self, a, b):
        hasil = a+b
        return f"Hasil {self.nama} adalah {hasil}"
    
matika = Matematika("Hitungan")
matika.info()
hasil_tambah = matika.tambah(4, 5)   
print(hasil_tambah) 

print("==================================================")

# parent
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        
    def info_siswa(self):
        print(f"Nama mahasiswa: {self.nama}")
        

# child/pewaris parent        
class MahasiswaJurusan(Mahasiswa):
    def __init__(self, nama, jurusan):
        super().__init__(nama)
        self.jurusan = jurusan
    
    # menimpa fungsi yg di parent    
    # def info_siswa(self):
    #     print(f"Nama: {self.nama}")
            
    def info_jurusan(self):
        print(f"Info jurusan mahasiswa {self.nama} adalah {self.jurusan}")     
                        
mahasiswa = MahasiswaJurusan("Agis", "Teknik Informatika")
mahasiswa.info_siswa()
mahasiswa.info_jurusan()           
        
print("==================================================")

class Hewan:
    def __init__(self, bunyi):
        self.bunyi = bunyi
        
    def suara(self):
        print("Suara hewan...")
        
    def jenis(self):
        print(f"Jenis suara hewan {self.bunyi}")    
            
class Kucing(Hewan):
    def __init__(self, bunyi, jumlah_kaki = 2):
        super().__init__(bunyi)
        self.jumlah_kaki = jumlah_kaki
    
    def kaki(self):
        print(f"Kakinya: {self.jumlah_kaki}")    
        
    def suara(self):
        print(f"Suara kucing: {self.bunyi}")
        
class Ayam(Hewan):
    def suara(self):
        print(f"Suara ayam: {self.bunyi}")
        
hewan_kucing = Kucing("Meong!", 4)

hewan_ayam = Ayam("Petok!")

hewan_kucing.suara()
hewan_kucing.jenis()
hewan_kucing.kaki()

hewan_ayam.suara()
hewan_ayam.jenis()                     