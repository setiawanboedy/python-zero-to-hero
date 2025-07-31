# belajar_module_package.py
# Contoh penggunaan Module & Package dalam Python
# Module adalah file Python yang berisi kode yang bisa diimpor
# Package adalah kumpulan module dalam folder

import math  # Import module built-in
import random
from datetime import datetime

from module_package_example import salam, kali
from module_package_example.mypackage import calculator  # Import specific function

# Menggunakan module built-in
print("Nilai pi:", math.pi)
print("Akar kuadrat 16:", math.sqrt(16))
print("Angka random:", random.randint(1, 10))
print("Waktu sekarang:", datetime.now())

# Import dengan alias
import math as m
print("Cos 0:", m.cos(0))

# Import semua function (tidak disarankan)
# from math import *

# Import module yang kita buat sendiri
# Pastikan file mymodule.py ada di folder yang sama
try:
    print("Salam dari module:", salam("Andi"))
    print("Hasil kali:", kali(5, 3))
except ImportError:
    print("Module mymodule belum dibuat")

# Import dari package yang kita buat
try:
    print("Hasil penjumlahan:", calculator.tambah(10, 5))
except ImportError:
    print("Package mypackage belum dibuat")
