class Building:
    total = 0

    def __init__(self):
        Building.total += 1


all_buildings = []
for i in range(40):
    new_building = Building()
    all_buildings.append(new_building)

print(all_buildings)
print("Total number of buildings:", Building.total)
