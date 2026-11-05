umur = 25
mbl = 'bmw'
usernames = ['admin', 'kai']
negara = 'ID'

if umur < 4:
    print("balita.")
elif umur >= 18:
    print("dewasa.")

if mbl == 'bmw':
    print("Mobilnya BMW.")

if mbl != 'fortuner':
    print("Mobilnya bukan fortuner.")

if umur >= 18 and umur < 65:
    print("Working age.")
    
if (umur >= 18 and umur < 65
        and negara == 'ID'):
    print("Eligible.")

if usernames:
    print("Ada user.")
else:
    print("kita harus nyari pengguna !")

