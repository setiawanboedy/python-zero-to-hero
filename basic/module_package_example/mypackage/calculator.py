# calculator.py
# Module kalkulator dalam package mypackage

def tambah(a, b):
    """Penjumlahan dua angka"""
    return a + b

def kurang(a, b):
    """Pengurangan dua angka"""
    return a - b

def kali(a, b):
    """Perkalian dua angka"""
    return a * b

def bagi(a, b):
    """Pembagian dua angka"""
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol!")
    return a / b

def pangkat(a, b):
    """Pangkat dua angka"""
    return a ** b
