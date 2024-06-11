class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return (self.numberOfFloors == other.numberOfFloors and
                    self.buildingType == other.buildingType)
        return False


building1 = Building(5, 'Жилой')
building2 = Building(5, 'Жилой')
building3 = Building(1, 'Гараж')
building4 = 'Просто строка'

print(building1 == building2)
print(building1 == building3)
print(building1 == building4)
