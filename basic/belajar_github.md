# Belajar Git & GitHub untuk Pemula

## 1. Apa itu Git & GitHub?
- **Git**: Sistem kontrol versi untuk mencatat perubahan kode/program.
- **GitHub**: Layanan hosting untuk menyimpan repository Git secara online, kolaborasi, dan berbagi kode.

## 2. Kenapa Harus Belajar Git & GitHub?
- Mencatat riwayat perubahan kode
- Kolaborasi tim
- Backup & berbagi kode
- Wajib di dunia kerja IT

## 3. Instalasi Git
- Download di https://git-scm.com/downloads
- Ikuti petunjuk instalasi sesuai OS (Windows/Mac/Linux)
- Cek instalasi: buka terminal/cmd, ketik: `git --version`

## 4. Setup Awal Git
```bash
git config --global user.name "Nama Kamu"
git config --global user.email "email@kamu.com"
```

## 5. Membuat Repository Baru
```bash
# Buat folder project
mkdir nama_project
cd nama_project
# Inisialisasi git
git init
```

## 6. Menyimpan Perubahan (commit)
```bash
# Tambah file baru
code hello.py
# Cek status
git status
# Tambah ke staging
git add hello.py
# Simpan perubahan
git commit -m "menambahkan hello.py"
```

## 7. Membuat Akun GitHub
- Daftar di https://github.com
- Buat repository baru via web

## 8. Menghubungkan Git Lokal ke GitHub
```bash
# Tambahkan remote origin
# (ganti URL dengan repo GitHub kamu)
git remote add origin https://github.com/username/nama_project.git
# Push pertama kali
git branch -M main
git push -u origin main
```

## 9. Clone Repository dari GitHub
```bash
git clone https://github.com/username/nama_project.git
```

## 10. Kolaborasi: Pull, Branch, Merge
```bash
# Ambil update terbaru
git pull origin main
# Buat branch baru
git checkout -b fitur-baru
# Merge branch ke main
git checkout main
git merge fitur-baru
```

> 1. Buat repo baru di GitHub
> 2. Clone ke lokal, tambahkan file, commit, dan push
> 3. Coba buat branch, edit file, merge ke main

## 11. Tips Penting
- Selalu commit perubahan kecil & jelas
- Gunakan `.gitignore` untuk file yang tidak perlu diupload
- Sering lakukan `git pull` sebelum mulai kerja
- Baca dokumentasi: https://git-scm.com/doc

---

## 12. Cara Membatalkan Commit & Staging

### Membatalkan Commit Terakhir (commit belum di-push)
```bash
git reset --soft HEAD~1
# Membatalkan commit, perubahan tetap di staging area

git reset --mixed HEAD~1
# Membatalkan commit, perubahan kembali ke working directory (belum di-stage)
```

### Membatalkan File dari Staging (unstage)
```bash
git reset HEAD nama_file
# File keluar dari staging area, tapi perubahan tetap ada
```

### Membatalkan Semua File dari Staging
```bash
git reset
# Semua file keluar dari staging area
```

### Catatan:
- Jika commit sudah di-push ke GitHub, gunakan `git revert` untuk membatalkan dengan aman.
- Hati-hati dengan `git reset --hard` karena akan menghapus perubahan di working directory!

---

> **Latihan:**
> 1. Buat repo baru di GitHub
> 2. Clone ke lokal, tambahkan file, commit, dan push
> 3. Coba buat branch, edit file, merge ke main

