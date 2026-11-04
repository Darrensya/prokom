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
