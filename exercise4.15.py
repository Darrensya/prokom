#exercise 4.10

kubik = [angka ** 3 for angka in range(1, 11)]

print("3 Angka awal dari list kubik:")
print(kubik[:3])

print("\n3 Angka tengah dari list kubik:")
print(kubik[3:6])

print("\n3 Angka akhir dari list kubik:")
print(kubik[-3:])

#exercise 4.11

pizza = ["magherita", "mushroom", "mozzarella"]
pizzaTeman = pizza[:]

pizza.append("salty sailor")
pizzaTeman.append("pepperoni")

print("Pizza favorit ku adalah:")
for pizza in pizza:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in pizzaTeman:
    print(pizza)

#exercise 4.8
kubik = []

for angka in range(1, 11):
    kubik.append(angka ** 3)

for cube in kubik:
    print(cube)
