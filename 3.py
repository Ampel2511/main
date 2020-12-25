# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
print("Сначала через list")
seasons = [["Зима", 12, 1, 2], ["Весна", 3, 4, 5], ["Лето", 6, 7, 8], ["Осень", 9, 10, 11]]
month = int(input("Укажите месяц "))
i = 0
while month > 12 or month <= 0:
    print("Ошибка")
    month = int(input("Укажите месяц "))

while i < len(seasons):
    for season in seasons:
        if month in season:
            print(f"Время года - {season[0]}")
        i += 1

print("Теперь через dict")
seasons = dict(зима=[12, 1, 2], весна=[3, 4, 5], лето=[6, 7, 8], осень=[9, 10, 11])
for season in seasons:
    months = seasons.get(season)
    if month in months:
        print(f"Время года - {season}")
    i += 1
