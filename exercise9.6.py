class Restoran:

    def __init__(self, namarestoran, jenis):
        self.namarestoran = namarestoran
        self.jenis = jenis
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.namarestoran} menyediakan makanan {self.jenis}.")

    def open_restaurant(self):
        print(f"{self.namarestoran} sudah buka!")
        
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment
        
class IceCreamStand(Restoran):
    def __init__(self, namarestoran, jenis="dessert"):
        super().__init__(namarestoran, jenis)
        self.rasa = []

    def show_rasa(self):
        print(f"{self.namarestoran} menyediakan rasa:")
        for flavor in self.rasa:
            print(f"- {flavor}")


stand = IceCreamStand("Scoops Ahoy")
stand.rasa = ["vanilla", "coklat", "strawberry", "cookiesncream", "mint"]
stand.show_rasa()