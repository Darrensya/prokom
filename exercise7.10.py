respons = {}

pollingAct = True

while pollingAct:
    nama = input("\nSiapa namanya? ")
    tmpt = input("Kalo bisa pergi ke 1 tempat mau kemana? ")

    respons[nama] = tmpt

    repeat = input("Apaakh kmu mau orang lain menjawab juga? (yes/no) ")
    if repeat == 'no':
        pollingAct = False

print("\n--- Hasil Polling ---")
for name, place in respons.items():
    print(f"{name.title()} mau mengunjungi {place.title()}.")
