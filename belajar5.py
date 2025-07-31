# List dan tuple

list_data = [24,35,41,14,51,53,74] # list (mutable)
tuple = (1,2,3,4) # tuple (immutable)

list_3 = list_data[6]
print(list_3)

tuple_3 = tuple[3]
print(tuple_3)

print("===================================")
# tambah data ke list
list_data.append(80)
print("append: ", list_data)

# Insert data di index fleksible
list_data.insert(1, 40)
print("insert: ",list_data)

# ambil data dengan index 7
list_7 = list_data[7]
print(list_7)


print("===================================")
# konversi tupel ke list
tuple2 = (41,22,43,4)

tuple_to_list = list(tuple2)

print(tuple_to_list)

print("===================================")
# gabungan 2 list
list1 = ["apel", "anggur"]
list2 = ["semangka", "salak"]

list_gabung = list1 + list2
print(list_gabung)

print("===================================")
# Slicing
list_data = [24,35,41,14,51,53,74]
list_range_start = list_data[4:] # range start dan seterusnya
list_range_start_stop = list_data[4:7] # index start dari 0, index stop dari 1
list_range_stop = list_data[:4] # range seterusnya sampai stop

print("List start: ", list_range_start)
print("List start dan stop: ", list_range_start_stop)
print("List stop: ", list_range_stop)

print("===================================")
# Mencari jumlah bilangan genap
list_data = [24,35,41,14,51,53,74]
jumlah_ganap = 0
for data in list_data:
    if data % 2 == 0:
        jumlah_ganap += 1
print("Jumlah bilangan genap: ", jumlah_ganap)

# Tugas
# Melengkapi catatan metode list beserta contohnya