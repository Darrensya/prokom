orang1 = {
    'nama_awal': 'ren',
    'nama_akhir': 'putri',
    'umur': 19,
    'kota': 'Solo'
}

orang2 = {
    'nama_awal': 'akhtar',
    'nama_akhir': 'reksa',
    'umur': 18,
    'kota': 'banten'
}

orang3 = {
    'nama_awal': 'danish',
    'nama_akhir': 'ghais',
    'umur': 19,
    'kota': 'jambi'
}

people = [orang1, orang2, orang3]

for orang in people :
    namaLengkap = f"{orang['nama_awal']} {orang['nama_akhir']}"
    print (f"{namaLengkap}, umur {orang['umur']}, tinggal di {orang['kota']}")