class Building:
    total = 0

    def __init__(self):
        Building.total += 1
        self.number = Building.total

    def __str__(self):
        return f'Экземпляр Building: {self.number}'


buildings = []

for i in range(40):
    buildings.append(Building())

for building in buildings:
    print(building)

print(f'Общее кол-во экземпляров Building: {Building.total}')
