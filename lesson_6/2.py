class Road:
    def __init__(self, length, weight, per_1, thickness):
        self._length = length
        self._weight = weight
        self._per_1 = per_1
        self._thickness = thickness

    def calc(self):
        print(f"Необходимая масса асфальта: "
              f"{self._length}м * {self._weight}м * {self._per_1}кг * {self._thickness}см = "
              f"{int(self._length * self._weight * self._per_1 * self._thickness / 1000)} т")


length = int(input("Укажите длину асфальта (м) "))
weight = int(input("Укажите ширину асфальта (м) "))
per_1 = int(input("Укажите массу асфальта для покрытия одного кв м дороги (кг) "))
thickness = int(input("Укажите толщину асфальта (см) "))

road = Road(length, weight, per_1, thickness)
road.calc()
