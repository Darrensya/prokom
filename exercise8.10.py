def msg(psn, terkirim) :
    while psn :
        pesanskrg =psn.pop(0)
        print(f"Mengirim : {pesanskrg}")
        terkirim.append(pesanskrg)
        
teks = [
    'Halo!',
    'Bagaiamana kabarmu?',
    'jangan lupa janji kita ya!!'
]

terkirim =[]
msg(teks, terkirim)

print("\nOriginal list:", teks)
print("Terkirim:", terkirim)