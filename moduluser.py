class User:

    def __init__(self, namaAwal, namaAkhir, umur, lokasi, pekerjaan):
        self.first_name = namaAwal
        self.last_name = namaAkhir
        self.age = umur
        self.location = lokasi
        self.pekerjaan = pekerjaan
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")
        print(f"Jurusan: {self.pekerjaan}")

    def greet_user(self):
        print(f"Selamat datang kembali, {self.first_name} {self.last_name}!")
        
    def increment_login_attempts(self):
            self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
