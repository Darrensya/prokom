print("Addition Calculator")
print("Enter 'q' at any time to quit.")

while True:
    angka1 = input("\nMasukkan angka: ")
    if angka1 == "q":
        break

    angka2 = input("Masukkan angka: ")
    if angka2 == "q":
        break
            
try:
    total = int(angka1) + int(angka2)
except ValueError:
    print("maaf harus angka.")
else:
    print(f"hasilnya : {total}.")