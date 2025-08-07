# latihan_module_package.py
# Latihan penggunaan Module & Package

# Import module built-in
import os
import sys
from random import choice, shuffle

from module_package_example import mymodule
from module_package_example.mypackage import calculator, utils

print("=== Latihan Module Built-in ===")
print("Direktori saat ini:", os.getcwd())
print("Platform:", sys.platform)

# Latihan dengan random
buah = ["apel", "jeruk", "mangga", "pisang"]
print("Buah random:", choice(buah))
shuffle(buah)
print("Buah setelah shuffle:", buah)

# Import module kita sendiri
print("\n=== Latihan Module Sendiri ===")
try:
    # Tambahkan path ke sys.path agar bisa import dari folder lain
    sys.path.append('module_package_example')
    
    print(mymodule.salam("Budi"))
    print(f"10 x 7 = {mymodule.kali(10, 7)}")
    print(f"20 / 4 = {mymodule.bagi(20, 4)}")
    print(f"PI = {mymodule.PI}")
    
except ImportError as e:
    print(f"Error import mymodule: {e}")

# Import dari package
print("\n=== Latihan Package ===")
try:
    
    # Test calculator
    print(f"15 + 8 = {calculator.tambah(15, 8)}")
    print(f"20 - 7 = {calculator.kurang(20, 7)}")
    print(f"5 * 6 = {calculator.kali(5, 6)}")
    print(f"2^3 = {calculator.pangkat(2, 3)}")
    
    # Test utils
    print(f"12 genap? {utils.is_genap(12)}")
    print(f"7 prima? {utils.is_prima(7)}")
    print(f"5! = {utils.faktorial(5)}")
    
except ImportError as e:
    print(f"Error import package: {e}")

# Latihan membuat dan menggunakan module temporary
print("\n=== Latihan Module Temporary ===")

def buat_module_temp():
    """Membuat file module sementara"""
    code = '''
def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_keliling_persegi(sisi):
    return 4 * sisi

KONSTANTA = "Ini dari module temp"
'''
    with open('temp_module.py', 'w') as f:
        f.write(code)
    print("Module temporary berhasil dibuat!")

