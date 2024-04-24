class House:
    def __init__(self):
        self.numberOfFloors = 0

    def set(self, floors):
        self.numberOfFloors = int(floors)
        print(self.numberOfFloors)


my_home = House()
my_home.set(11)
