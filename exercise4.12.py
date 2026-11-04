makananSaya = ["es krim", "pizza", "burger"]
makananTeman = makananSaya[:]

makananSaya.append("sate")
makananTeman.append("nasi goreng")

print("Makanan favorit ku adalah:")
for makanan in makananSaya:
    print(makanan)
    
print("\nMakanan favorit temanku adalah:")
for makanan in makananTeman:
    print(makanan)