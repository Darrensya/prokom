orang = "\n Berapa usia anda?"

while True:
    umur = input(orang)
    
    if umur == 'quit':
        break
    
    umur = int(umur)
    if umur < 3:
        print("Tiket anda gratis")
    elif umur <= 12 :
        print ("Tiket anda 10$")
    else:
        print ("Tiket anda 15$")