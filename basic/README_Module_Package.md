# README_Module_Package.md

## Materi Module & Package Python

### Struktur Folder:
```
basic/
├── belajar_module_package.py          # Penjelasan konsep module & package
├── latihan_module_package.py          # Latihan lengkap
├── demo_module_package.py             # Demo penggunaan
└── module_package_example/            # Folder contoh
    ├── mymodule.py                    # Module sederhana
    └── mypackage/                     # Package contoh
        ├── __init__.py                # File init package
        ├── calculator.py              # Module kalkulator
        └── utils.py                   # Module utilitas
```

### Cara Menjalankan:
1. Buka terminal di folder `basic/`
2. Jalankan: `python demo_module_package.py`
3. Untuk latihan lengkap: `python latihan_module_package.py`

### Konsep Penting:
- **Module**: File Python (.py) yang berisi kode
- **Package**: Folder berisi __init__.py dan module-module
- **Import**: Cara menggunakan kode dari file/package lain
- **__name__**: Variabel yang berisi nama module
- **sys.path**: Daftar folder tempat Python mencari module

### Contoh Import:
```python
import math                    # Import module built-in
from datetime import datetime  # Import function spesifik
import mymodule               # Import module sendiri
from mypackage import calculator # Import dari package
```
