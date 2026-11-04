toppiza = "\n Sebutkan toping yang anda inginkan! "

while True:
    topping = input(toppiza)
    
    if topping == 'quit':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza anda")