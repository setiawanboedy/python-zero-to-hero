# package
import math
from matapelajaran import matematika
import matapelajaran.biologi as bio

from matapelajaran import matematika # import cara 1
import matapelajaran.matematika as matika # import cara 2
from matapelajaran.matematika import bagi, tambah # import cara 3

akar = math.sqrt(10)
cos = math.cos(0)

hasil_tambah = matematika.tambah(5,6)
hasil_bagi = matematika.bagi(5,6)

list = [3,5,6,3,6]
hitung_list = matematika.jumlah_list_int(list)

nama_ilmiah = bio.nama_ilmiah("padi")

print(akar)
print(cos)
print(hasil_tambah)
print(hasil_bagi)
print(hitung_list)
print(nama_ilmiah)