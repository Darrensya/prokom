pet1 = {
    'jenisHewan': 'kucing',
    'pemilik': 'ren',
    'nama': 'dipsy',
    'umur': 3,
}

pet2 = {
    'jenisHewan': 'kura-kura',
    'pemilik': 'reksa',
    'nama': 'tireks',
    'umur': 2,
}

pet3 = {
    'jenisHewan': 'kelinci',
    'pemilik': 'adzra',
    'nama': 'bunbun',
    'umur': 1,
}

pet4 = {
    'jenisHewan': 'kucing',
    'pemilik': 'reksa',
    'nama': 'blaky',
    'umur': 4,
}

hewan = [pet1, pet2, pet3, pet4]

print("Daftar hewan peliharaan:")
for pet in hewan:
    print(f"\n{pet['nama'].title()}")
    print(f"  Jenis   : {pet['jenisHewan'].title()}")
    print(f"  Pemilik : {pet['pemilik'].title()}")
    print(f"  Umur    : {pet['umur']} tahun")


jumlah = {}
for pet in hewan:
    jenis = pet['jenisHewan']
    jumlah[jenis] = jumlah.get(jenis, 0) + 1

print("\nJumlah per jenis hewan:")
for jenis, total in jumlah.items():
    print(f"  {jenis.title()}: {total}")


punya = {}
for pet in hewan:
    pemilik = pet['pemilik']
    if pemilik not in punya:
        punya[pemilik] = []
    punya[pemilik].append(pet['nama'])

print("\nPemilik dan hewan-hewannya:")
for pemilik, daftar_nama in punya.items():
    nama_gabung = " dan ".join(nama.title() for nama in daftar_nama)
    print(f"  {pemilik.title()}: {nama_gabung}")

