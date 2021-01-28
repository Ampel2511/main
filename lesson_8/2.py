def func():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    try:
        print(a / b)
    except ZeroDivisionError:
        print("делитель не может быть 0")
        func()


func()
