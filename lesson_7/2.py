class Clothes:

    total = 0

    def __init__(self, type, param):
        if type.capitalize() == "Костюм":
            self.type = type
            self.growth = param
            Clothes.total += 2 * self.growth + 0.3
        elif type.capitalize() == "Пальто":
            self.type = type
            self.size = param
            Clothes.total += self.size / 6.5 + 0.5

    @property
    def count(self):
        if self.type == "Костюм":
            return f"{round(2 * self.growth + 0.3, 2)} расход ткани для создания костюма"
        elif self.type == "Пальто":
            return f"{round(self.size/6.5 + 0.5, 2)} расход ткани для создания пальто"

    @property
    def total_count(self):
        return f"{round(Clothes.total, 2)} m - общий расход"


name_1 = Clothes("Костюм", 1.89)
print(name_1.count)
name_2 = Clothes("Костюм", 1.74)
print(name_2.count)
name_3 = Clothes("Пальто", 42)
print(name_3.count)
name_4 = Clothes("Пальто", 50)
print(name_4.count)

print(name_1.total_count)
