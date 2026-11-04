sungai = {
    'nill' : 'mesir',
    'amazon' : 'brazil',
    'mississippi' : 'AS'
}

for Nsungai, negara in sungai.items():
    print(f"Sungai {Nsungai.title()} berada di {negara.title()}")
    
print("\n Kamus Sungai")
for river in sungai.keys():
    print(river.title())
    
print("\n Kamus Negara")
for country in sungai.values():
    print(country.title())
    
