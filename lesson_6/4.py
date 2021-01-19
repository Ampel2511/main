class Car:
    # по идее, проще так написать и при создании любого экземпляра сразу все запрашивать, чем в каждом дочернем классе прописывать конструктор?
    # def __init__(self, speed, color, name, is_police):
    #     self.speed = speed
    #     self.color = color
    #     self.name = name
    #     self.is_police = is_police

    speed = 0
    color = ""
    name = ""
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(self.speed)

    def show_all(self):
        print(self.name, self.color, self.speed, self.is_police)


class TownCar(Car):

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print(self.speed)

class SportCar(Car):

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print(self.speed)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


car_1 = TownCar(color="blue", speed=50, name="car_1")
car_2 = PoliceCar(color="black", speed=180, name="car_2")
car_3 = SportCar(color="red", speed=300, name="car_3")
car_4 = WorkCar(color="white", speed=35, name="car_4")
car_5 = TownCar(color="yellow", speed=70, name="car_5")
car_6 = WorkCar(color="green", speed=45, name="car_6")
car_7 = Car()

print("-" * 30)

print(car_1.color, car_1.speed, car_1.name)
print(car_2.color, car_2.speed, car_2.name)
print(car_3.color, car_3.speed, car_3.name)
print(car_4.color, car_4.speed, car_4.name)
print(car_5.color, car_5.speed, car_5.name)
print(car_6.color, car_6.speed, car_6.name)
print(car_7.color, car_7.speed, car_7.name)

print("-" * 30)

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_4.show_speed()
car_5.show_speed()
car_6.show_speed()
car_7.show_speed()

print("-" * 30)

car_1.show_all()
car_2.show_all()
car_3.show_all()
car_4.show_all()
car_5.show_all()
car_6.show_all()
car_7.show_all()

