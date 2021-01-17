from functools import reduce


def sum(prev, current):
    return int(prev) + int(current)


n = input("Введите числа, которые хотите записать в файл ")
with open("file_5.txt", "a+") as file:
    file.write(n)
    file.seek(0)
    print(reduce(sum, file.read().split()))






