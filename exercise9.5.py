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
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0


user = User("Eustace", "Bagge", 79, "Kansas", "Petani")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")