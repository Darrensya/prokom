from moduluser import User

class Privileges:

    def __init__(self):
        self.privileges =  ["menambah post", "menghapus post", "ngeban user"]

    def show_privileges(self):
        print("privileges admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):

    def __init__(self, namaAwal, namaAkhir, umur, lokasi, pekerjaan):
        super().__init__(namaAwal, namaAkhir, umur, lokasi, pekerjaan)
        self.privileges = Privileges()