from itertools import count, cycle
start = int(input("Укажите с какого числа начать "))
stop = int(input("Укажите на каком числе закончить "))
# как можно иначе при запросе данных, если они не удовлетворяют требованиям, вернуться к запросу?
# try/except не возвращается к предыдущему действию, как и if/ else
while start > stop:
    print("Начальное значение не может быть меньше конечного")
    start = int(input("Укажите с какого числа начать "))
    stop = int(input("Укажите на каком числе закончить "))
numbers = []
for num in count(start):
    if num > stop:
        break
    else:
        numbers.append(num)
print(numbers)
i = int(input("Сколько раз вы хотите вывести элемент списка? "))
n = 0
for num in cycle(numbers):
    if n > i:
        break
    print(num)
    n += 1
