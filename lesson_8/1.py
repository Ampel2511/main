from datetime import datetime


class Date:

    def __init__(self, date):
        self.user_date = list(map(int, date.split("-")))

    @classmethod
    def func(cls, date):
        for i in date:
            print(i, type(i))
        print(date)

    @staticmethod
    def check(date):
        try:
            check = datetime(date[2], date[1], date[0])
            print(f"Дата {check} существует")
        except:
            print(f"Даты не существует")


ex = Date("26-01-2021")
Date.func(ex.user_date)
Date.check(ex.user_date)
