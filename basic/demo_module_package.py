# demo_module_package.py
# Demo penggunaan module dan package yang sudah dibuat
# Jalankan file ini dari folder basic untuk melihat hasilnya

import sys
import os

from module_package_example import mymodule
from module_package_example.mypackage import calculator, utils

# import module_package_example/mymodule

# Menambahkan path ke folder module_package_example
sys.path.append(os.path.join(os.path.dirname(__file__), 'module_package_example'))

print("=== Demo Module & Package ===")

# Demo mymodule
print("\n1. Demo mymodule:")
try:
    print(f"  - Salam: {mymodule.salam('Python Learner')}")
    print(f"  - Kali: {mymodule.kali(7, 8)}")
    print(f"  - Bagi: {mymodule.bagi(15, 3)}")
    print(f"  - PI: {mymodule.PI}")
    print(f"  - Nama aplikasi: {mymodule.NAMA_APLIKASI}")
except ImportError as e:
    print(f"  Error: {e}")

# Demo mypackage
print("\n2. Demo mypackage:")
try:
    
    print("  Calculator:")
    print(f"    - 10 + 5 = {calculator.tambah(10, 5)}")
    print(f"    - 10 - 3 = {calculator.kurang(10, 3)}")
    print(f"    - 4 * 6 = {calculator.kali(4, 6)}")
    print(f"    - 20 / 4 = {calculator.bagi(20, 4)}")
    print(f"    - 2^4 = {calculator.pangkat(2, 4)}")
    
    print("  Utils:")
    print(f"    - 8 genap? {utils.is_genap(8)}")
    print(f"    - 11 prima? {utils.is_prima(11)}")
    print(f"    - 6! = {utils.faktorial(6)}")
    
except ImportError as e:
    print(f"  Error: {e}")

print("\n=== Panduan Penggunaan ===")
print("1. Pastikan folder 'module_package_example' ada")
print("2. Jalankan file ini dari folder 'basic'")
print("3. Lihat contoh import di belajar_module_package.py")
print("4. Coba latihan di latihan_module_package.py")
