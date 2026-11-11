class Restoran:

    def __init__(self, namarestoran, jenis):
        self.namarestoran = namarestoran
        self.jenis = jenis

    def describe_restaurant(self):
        print(f"{self.namarestoran} menyediakan makanan {self.jenis}.")

    def open_restaurant(self):
        print(f"{self.namarestoran} sudah buka!")


restaurant = Restoran("warung pizza", "italia")

print(restaurant.namarestoran)
print(restaurant.jenis)

restaurant.describe_restaurant()
restaurant.open_restaurant()