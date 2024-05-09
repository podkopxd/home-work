class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return '100hp'


class Nissan(Vehicle, Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "car"
        self.price = 1500000

    def horse_powers(self):
        return "200hp"


my_car = Nissan()
print('my car params: ', my_car.vehicle_type, ',', my_car.price, ',', my_car.horse_powers())
