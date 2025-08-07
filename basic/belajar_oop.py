# belajar_oop.py
# Contoh dasar OOP (Object Oriented Programming) dalam Python
# OOP memudahkan pengelolaan kode dengan konsep class dan object

# Membuat class sederhana
class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama}, jurusan {self.jurusan}.")

    def ulang_tahun(self):
        self.umur += 1
        print(f"Selamat ulang tahun, {self.nama}! Umurmu sekarang {self.umur} tahun.")

# Membuat object dari class
mhs1 = Mahasiswa("Andi", 20, "Informatika")
mhs2 = Mahasiswa("Siti", 21, "Matematika")

mhs1.sapa()
mhs2.sapa()
mhs1.ulang_tahun()

# Pewarisan (inheritance)
class MahasiswaAktif(Mahasiswa):
    def __init__(self, nama, umur, jurusan, organisasi):
        super().__init__(nama, umur, jurusan)
        self.organisasi = organisasi

    def info_organisasi(self):
        print(f"Saya aktif di organisasi {self.organisasi}.")

mhs3 = MahasiswaAktif("Budi", 22, "Fisika", "BEM")
mhs3.sapa()
mhs3.info_organisasi()

# Encapsulation: atribut private
class Akun:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private

    def cek_password(self, pwd):
        return pwd == self.__password

akun1 = Akun("user1", "rahasia")
print("Password benar?", akun1.cek_password("rahasia"))
# print(akun1.__password)  # Akan error jika di-uncomment

# Polymorphism: method dengan nama sama, perilaku berbeda
class Hewan:
    def suara(self):
        print("Hewan bersuara...")

class Kucing(Hewan):
    def suara(self):
        print("Meong!")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk!")

hewan1 = Kucing()
hewan2 = Anjing()
hewan1.suara()
hewan2.suara()
