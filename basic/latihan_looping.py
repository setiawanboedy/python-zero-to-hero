# latihan_looping.py
# Latihan sederhana penggunaan looping

for i in range(1, 4):
    print("Angka:", i)

angka = 5
while angka > 0:
    print("Mundur:", angka)
    angka -= 1

# Contoh medium: for loop dengan list
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print("Saya suka", item)

# Contoh medium: while dengan break
count = 0
while True:
    print("Perulangan ke-", count)
    count += 1
    if count == 3:
        break  # Keluar dari loop saat count == 3

# Contoh medium: nested loop (perulangan bersarang)
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
