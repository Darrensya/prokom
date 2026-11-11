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
        
class admin(User):
    def __init__(self, namaAwal, namaAkhir, umur, lokasi, pekerjaan):
        super().__init__(namaAwal, namaAkhir, umur, lokasi, pekerjaan)
        self.privileges = ["menambah post", "menghapus post", "ngeban user"]
    def show_privileges(self):
        print(f"Privileges untuk {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


Admin = admin("Eustace", "Bagge", 79, "Kansas", "admin")
Admin.show_privileges()