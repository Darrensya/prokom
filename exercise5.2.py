#equality and inequality w/ strings
minuman = "kopi"
print(minuman == "kopi")
print(minuman != "teh")
print(minuman == "teh")
print(minuman != "kopi")

#using lower()
nama = "Ren"
print(nama.lower() == "ren")
print(nama == "ren")
print(nama.lower() == "REN")

#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
angka1 = 10
print(angka1 == 10)
print(angka1 == 20)
print(angka1 != 10)
print(angka1 != 20)
print(angka1 > 5)
print(angka1 < 5)
print(angka1 < 15)
print(angka1 > 15)
print(angka1 >= 10)
print(angka1 <= 10)

# using the and keyword and the or keyword
umur = 15
print(angka1 > 5 and umur < 20)
print(angka1 > 20 and umur < 20)
print(angka1 > 5 or umur < 20)
print(angka1 > 15 or umur < 10)

#testing whether an item is in a list
dessert = ["kue", "es krim", "puding"]
print("kue" in dessert)
print("roti" in dessert)

#testing whether an item is not in a list
pastry = ["croissant", "donat", "kue"]
print("roti" not in pastry) 
print("kue" not in pastry)