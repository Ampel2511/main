from time import sleep
from itertools import cycle

colors = ["красный", "желтый", "зеленый"]


class TrafficLight:
    __color = " "

    def running(self):
        if self.__color == " ":
            self.__color = "красный"
            print(f"Горит {self.__color}")
        elif self.__color == "красный":
            sleep(7)
            self.__color = "желтый"
            print(f"Горит {self.__color}")
        elif self.__color == "желтый":
            sleep(2)
            self.__color = "зеленый"
            print(f"Горит {self.__color}")
        elif self.__color == "зеленый":
            sleep(15)
            self.__color = "красный"
            print(f"Горит {self.__color}")

    def check(self, color):
        if self.__color != color:
            print("Ошибка! Цвет не совпадает! Порядок нарушен!")
            exit()
        elif self.__color == " ":
            pass


light = TrafficLight()


def work(traffic_light, n, colors):
    i = 0
    for color in cycle(colors):
        if i > 3 * n:
            break
        traffic_light.running()
        traffic_light.check(color)


n = int(input("Сколько циклов работы светофора вы хотите проверить? "))

work(traffic_light=light, n=n, colors=colors)
