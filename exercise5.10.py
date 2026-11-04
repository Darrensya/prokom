user_sekarang = ["admin", "kai", "cole", "lloyd", "zane"]
user_baru = ["ren", "KAI", "cay", "pip", "ZANE"]

user_sekarang_lower = [user.lower() for user in user_sekarang]

for user in user_baru:
    if user.lower() in user_sekarang_lower:
        print(f"Nama pengguna '{user}' sudah digunakan. Silakan pilih nama lain.")
    else:
        print(f"Nama pengguna '{user}' tersedia.")