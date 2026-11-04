usrnm = ["admin", "kai", "cole", "lloyd", "zane"]

for usrnm in usrnm:
    if "admin" in usrnm:
        print("Halo admin, apakah anda mau melihat laporan status?")
    else:
        print(f"Halo {usrnm.title()}, terima kasih telah login kembali.")