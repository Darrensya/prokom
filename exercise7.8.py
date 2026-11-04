sandwichOrder = ['tuna', 'mayo', 'telur', 'beef']
finish = []

while sandwichOrder:
    skrg = sandwichOrder.pop()
    print(f"aku telah membuat pesanan {skrg} sandwich.")
    finish.append(skrg)
    
print("\nSandwhich yang telah dibuat :")
for sandwich in finish:
    print(sandwich.title())