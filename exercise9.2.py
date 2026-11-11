class Restoran:

    def __init__(self, namarestoran, jenis):
        self.namarestoran = namarestoran
        self.jenis = jenis

    def describe_restaurant(self):
        print(f"{self.namarestoran} menyediakan makanan {self.jenis}.")

    def open_restaurant(self):
        print(f"{self.namarestoran} sudah buka!")


restaurant1 = Restoran("sushi yay", "jepang")
restaurant2 = Restoran("taco bell", "mexico")
restaurant3 = Restoran("haidilao hotpot", "cina")



restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
