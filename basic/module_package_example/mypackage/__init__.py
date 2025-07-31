# __init__.py
# File ini membuat folder menjadi package
# Isi file ini dijalankan saat package diimpor

print("Package mypackage telah diimpor!")

# Menentukan apa yang bisa diimpor dari package ini
__all__ = ['calculator', 'utils']
