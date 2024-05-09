class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "100hp"


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000

    def horse_powers(self):
        return "200hp"


class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 800000

    def horse_powers(self):
        return "90hp"


my_car = Car()
print('average car params: ', my_car.price, my_car.horse_powers())

nissan_skyline = Nissan()
print('my dream-car params: ', nissan_skyline.price, nissan_skyline.horse_powers())

kia_rio = Kia()
print('my current car params: ', kia_rio.price, kia_rio.horse_powers())
