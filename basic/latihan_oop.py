# latihan_oop.py
# Latihan OOP: class, object, inheritance, encapsulation, polymorphism

# Latihan 1: Buat class PersegiPanjang dengan atribut panjang, lebar, dan method luas & keliling
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())
print("Keliling:", pp.keliling())

# Latihan 2: Buat class Mahasiswa dengan method tampilkan info, lalu buat object dan tampilkan
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")

m1 = Mahasiswa("Rina", "12345")
m1.info()

# Latihan 3: Inheritance - class Dosen turunan dari class Mahasiswa, tambah method mengajar
class Dosen(Mahasiswa):
    def __init__(self, nama, nim, matkul):
        super().__init__(nama, nim)
        self.matkul = matkul
    def mengajar(self):
        print(f"Dosen {self.nama} mengajar {self.matkul}")

d1 = Dosen("Pak Budi", "00001", "Matematika")
d1.info()
d1.mengajar()

# Latihan 4: Encapsulation - buat class dengan atribut private dan method akses
class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo
    def cek_saldo(self):
        return self.__saldo
    def setor(self, jumlah):
        self.__saldo += jumlah
    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup!")

akun = AkunBank("Siti", 100000)
print("Saldo awal:", akun.cek_saldo())
akun.setor(50000)
akun.tarik(30000)
print("Saldo akhir:", akun.cek_saldo())

# Latihan 5: Polymorphism - buat 2 class dengan method sama, perilaku berbeda
class Burung:
    def suara(self):
        print("Cuit cuit!")
class Ayam:
    def suara(self):
        print("Kukuruyuk!")

def bunyikan(hewan):
    hewan.suara()

b1 = Burung()
a1 = Ayam()
bunyikan(b1)
bunyikan(a1)
