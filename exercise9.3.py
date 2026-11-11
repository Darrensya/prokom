class User:

    def __init__(self, namaAwal, namaAkhir, umur, lokasi, pekerjaan):
        self.first_name = namaAwal
        self.last_name = namaAkhir
        self.age = umur
        self.location = lokasi
        self.pekerjaan = pekerjaan

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")
        print(f"Jurusan: {self.pekerjaan}")

    def greet_user(self):
        print(f"Selamat datang kembali, {self.first_name} {self.last_name}!")


user_1 = User("Clark", "Kent", 25, "Kansas", "Jurnalis")
user_2 = User("Peter", "Griffin", 35, "P.Rhode", "Inspektur Keselamatan")
user_3 = User("Eustace", "Bagge", 79, "Kansas", "Petani")


for user in (user_1, user_2, user_3):
    user.describe_user()
    user.greet_user()
    print()