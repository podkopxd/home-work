class Building:
    def __init__(self, floors, type):
        self.numberOfFloors = floors
        self.buildingType = type

    def __eq__(self, other):
        return self is other

my_house = Building(9, None)
is_eq = my_house.buildingType == my_house.numberOfFloors
print(is_eq)
