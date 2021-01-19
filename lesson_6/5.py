class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print(f"Я {self.title} Я пишу ручкой")


class Pencil(Stationery):

    def draw(self):
        print(f"Я {self.title} Я пишу карандашом")


class Handle(Stationery):

    def draw(self):
        print(f"Я {self.title} Я пишу маркером")


pen = Pen("pen_1")
pencil = Pencil("pencil_1")
handle = Handle("handle_1")

pen.draw()
pencil.draw()
handle.draw()

