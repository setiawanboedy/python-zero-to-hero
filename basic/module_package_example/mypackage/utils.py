# utils.py
# Module utilitas dalam package mypackage

def is_genap(angka):
    """Cek apakah angka genap"""
    return angka % 2 == 0

def is_prima(angka):
    """Cek apakah angka prima"""
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

def faktorial(n):
    """Hitung faktorial"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
