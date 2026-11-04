# conditional test in the while statement to stop the loop.
prompt = "\nESebutkan toping yang anda inginkan! "
topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Saya akan menambahkan {topping} ke pizza anda.")
        
# active variable to control how long the loop run
prompt = "\nSebutkan toping yang anda inginkan! "
active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Saya akan menambahkan {topping} ke pizza anda")
        
#a break statement to exit the loop when the user enters a 'quit' value
prompt = "\nSebutkan toping yang anda inginkan! "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print(f"Saya akan menambahkan {topping} ke pizza anda")