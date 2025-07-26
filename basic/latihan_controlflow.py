# latihan_controlflow.py
# Latihan sederhana penggunaan control flow

umur = 18
if umur >= 17:
    print("Sudah boleh membuat KTP")
else:
    print("Belum boleh membuat KTP")

# Contoh medium: menentukan kategori usia
usia = 25
if usia < 13:
    print("Anak-anak")
elif usia < 18:
    print("Remaja")
elif usia < 60:
    print("Dewasa")
else:
    print("Lansia")

# Contoh medium: nested if untuk penilaian ujian
nilai = 85
lulus = True
if lulus:
    if nilai >= 90:
        print("Lulus dengan predikat A")
    elif nilai >= 80:
        print("Lulus dengan predikat B")
    else:
        print("Lulus dengan predikat C")
else:
    print("Tidak lulus")

# Contoh medium: pengecekan login sederhana
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login berhasil!")
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan!")
