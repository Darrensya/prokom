usrnm = []

if usrnm:
    for usrnm in usrnm:
        if "admin" in usrnm:
            print("Halo admin, apakah anda mau melihat laporan status?")
        else:
            print(f"Halo {usrnm.title()}, terima kasih telah login kembali.")
else:
    print("Kita perlu mencari anggota!")