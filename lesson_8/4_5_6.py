def next_tech():
    next_id = input("Введите 'next' чтобы продолжить распределение или 'exit' чтобы завершить программу ")
    try:
        if next_id == 'next':
            Tech.transfer()
        elif next_id == "exit":
            print("Спасибо за пользование")
            exit()
        else:
            raise ValueError
    except ValueError:
        print("Неправильный ввод команды")
        next_tech()


class Storage:
    storage = {}
    storage_id = 1

    @classmethod
    def add(cls, name, count):
        Storage.storage[Storage.storage_id] = [count, name]
        Storage.storage_id += 1


class Tech:
    def __init__(self, price, weight, release_date, brand, tech_id):
        if self.__class__ == Printer:
            self.tech_class = "принтер"
        elif self.__class__ == Xerox:
            self.tech_class = "ксерокс"
        elif self.__class__ == Scanner:
            self.tech_class = "сканнер"
        self.tech_id = tech_id
        self.brand = brand
        self.price = price
        self.release_date = release_date
        self.weight = weight

    def reception(self):
        try:
            count = int(input(f"Укажите количество ед техники для {self.tech_class} {self.brand} "
                              f"{self.release_date}г ID {self.tech_id} "))
            Storage.add(self, count)
        except:
            print("Введите число")
            self.reception()

    @classmethod
    def transfer(cls):
        for i in Storage.storage.keys():
            print(f"ID записи {i}")
            for key in Storage.storage[i][1].__dict__:
                print(key, "->", Storage.storage[i][1].__dict__[key])
            print("-" * 30)
        try:
            n = int(input("Выберите ID записи "))
            tech = Storage.storage[n][1]
            count = Storage.storage[n][0]
            date = tech.release_date
            tech_id = tech.tech_id
            tech_class = tech.tech_class
            name = tech.brand
            place = input(f"Вы выбрали ID {tech_id} {tech_class} {name} {date} г выпуска в количестве {count} шт, "
                          f"укажите в какой отдел отправить ")
            print(f"В {place} будет отправлен {tech_class} {name} {date} г выпуска в количестве {count} шт")
            Storage.storage.pop(n)
            next_tech()
        except (ValueError, KeyError):
            print("Неверный ID")
            Tech.transfer()


class Printer(Tech):
    def __init__(self, tech_id, price, weight, release_date, brand, kind, color: bool):
        Tech.__init__(self, price, weight, release_date, brand, tech_id)
        self.color = color
        self.kind = kind


class Xerox(Tech):
    def __init__(self, tech_id, price, weight, release_date, brand, speed, color: bool):
        Tech.__init__(self, price, weight, release_date, brand, tech_id)
        self.speed = speed
        self.color = color


class Scanner(Tech):
    def __init__(self, tech_id, price, weight, release_date, brand, sensor, scanner_format, ):
        Tech.__init__(self, price, weight, release_date, brand, tech_id, )
        self.sensor = sensor
        self.format = scanner_format


printer_1 = Printer(1, 6000, 3000, 2019, "Hp", "laser", True)
printer_2 = Printer(2, 6000, 3000, 2019, "Hp", "laser", False)
scanner_1 = Scanner(3, 4500, 1500, 2020, "Canon", "CIS", "A4")
scanner_2 = Scanner(4, 5500, 1500, 2020, "Canon", "CIS", "A4")
xerox_1 = Xerox(5, 3000, 2000, 2018, "Samsung", "60 коп/мин", False)
xerox_2 = Xerox(6, 4000, 2000, 2018, "Samsung", "50 коп/мин", True)

printer_1.reception()
printer_2.reception()
xerox_1.reception()
xerox_2.reception()
scanner_1.reception()
scanner_2.reception()

Tech.transfer()
