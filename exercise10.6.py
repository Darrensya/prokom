angka1 = input("Masukkan angka: ")
angka2 = input("Masukkan angka lain: ")

try:
    total = int(angka1) + int(angka2)
except ValueError:
    print("maaf harus angka.")
else:
    print(f"hasilnya : {total}.")