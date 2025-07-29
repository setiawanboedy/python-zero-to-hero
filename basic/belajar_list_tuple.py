# belajar_list_tuple.py
# Contoh penggunaan List dan Tuple dalam Python
# List dan Tuple adalah struktur data untuk menyimpan banyak nilai

# List: dapat diubah (mutable)
daftar_buah = ["apel", "jeruk", "mangga"]
print("List buah:", daftar_buah)
print("Buah pertama:", daftar_buah[0])  # Mengakses elemen pertama

daftar_buah.append("pisang")  # Menambah elemen ke list
print("Setelah ditambah pisang:", daftar_buah)

daftar_buah[1] = "anggur"  # Mengubah elemen kedua
print("Setelah diubah:", daftar_buah)

# Tuple: tidak dapat diubah (immutable)
data_tuple = (10, 20, 30)
print("Tuple data:", data_tuple)
print("Elemen kedua:", data_tuple[1])
# data_tuple[0] = 99  # Akan error jika di-uncomment

# Konversi list ke tuple dan sebaliknya
list_ke_tuple = tuple(daftar_buah)
tuple_ke_list = list(data_tuple)
print("List ke tuple:", list_ke_tuple)
print("Tuple ke list:", tuple_ke_list)
