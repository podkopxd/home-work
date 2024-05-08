class Building:
    total = 0

    def __init__(self):
        Building.total += 1

all_buildings = []

while len(all_buildings) < 40:
    new_building = Building()
    all_buildings.append(new_building)

print(all_buildings)
print(Building.total)
