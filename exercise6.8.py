pet1 = {
    'jenisHewan': 'kucing',
    'pemilik': 'ren',
}

pet2 = {
    'jenisHewan': 'kura-kura',
    'pemilik': 'reksa',
}

pet3 = {
    'jenisHewan': 'kelinci',
    'pemilik': 'adzra',
}

hewan = [ pet1, pet2, pet3]

for pet in hewan :
    print (f"{pet['pemilik']} mempunyai hewan peliharaan {pet['jenisHewan']}")