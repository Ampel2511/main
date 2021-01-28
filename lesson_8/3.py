class NotNum(Exception):
    not_num = []

    def __init__(self, data):
        NotNum.not_num.append(data)


user_list = []


def func():
    n = input("Добавьте в список значение, чтобы закончить, введите Q ")
    if n == "Q":
        print(user_list)
        print(f"Не попало в список: {NotNum.not_num}")
    else:
        try:
            if n.isdigit():
                user_list.append(n)
                func()
            else:
                raise NotNum(n)
        except NotNum:
            print("Должны быть только числа")
            func()


func()
