# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [8, 5, 2, 2, 1]
numbers = int(input("Сколько чисел хотите добавить в рейтинг? "))
i = 0
while i < numbers:
    number = int(input("Введите число "))
    if number in my_list:
        index = my_list.index(number)
        count = my_list.count(number)
        my_list.insert(index + count, number)
        print(my_list)
    else:
        my_list.append(number)
        my_list.sort()
        my_list.reverse()
        print(my_list)
    i += 1

