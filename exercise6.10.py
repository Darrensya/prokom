noFav = {
    'darren': ['7','23'],
    'akhtar': ['13', '45'],
    'danish': ['67', '404','999'],
    'adzra': ['17','34', ' 61'],
    'dzikra': ['1', '5', '78', '91']
}

for nama, number in noFav.items() :
    print (f"{nama.title()} menyukai angka :")
    for angka in number:
        print (f"{angka}")
    print()