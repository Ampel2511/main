class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}\n"
              f"Должность: {self.position}")

    def get_total_income(self):
        print(f"Доход сотрудника: {self._income['wage'] + self._income['bonus']}")


worker_1 = Position("Иван", "Иванов", "дворник", 20000, 5000)
worker_1.get_full_name()
worker_1.get_total_income()
