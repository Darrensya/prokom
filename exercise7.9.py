sandwichOrder = ['pastrami', 'tuna', 'mayo', 'pastrami', 'pastrami', 'telur', 'beef']
finish = []

print('Maaf deli kehabisan pastrami')

while 'pastrami' in sandwichOrder:
    sandwichOrder.remove('pastrami')

while sandwichOrder:
    skrg = sandwichOrder.pop()
    print(f"aku telah membuat pesanan {skrg} sandwich.")
    finish.append(skrg)
    
print("\nSandwhich yang telah dibuat :")
for sandwich in finish:
    print(sandwich.title())