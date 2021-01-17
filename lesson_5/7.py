from json import dump

info_list = []
info_dict = {}
average_profit = dict(average_profit=0)
with open("file_7.txt") as file:
    print()
    for n, data in enumerate(file.read().split(), 0):
        if data.count("firm_") == 1:
            key = data
            info_dict[key] = 0
        elif data.isdigit():
            try:  # try для того чтобы при попытке из издержек вычесть след по порядку значение, которое является
                # строкой, не выдавало ошибку
                file.seek(0)  # как можно обойти момент, когда каждый раз при обращении к файлу,
                # надо переставлять коретку в самое начало?
                profit = int(data) - int(file.read().split()[n + 1])
                if profit > 0:
                    average_profit[average_profit] += profit
                info_dict[key] = profit  # не стал писать abs(profit) чтобы было видно где убыток, а где прибыль
            except:
                pass
    average_profit[average_profit] /= len(info_dict.items())
    info_list.append(info_dict)
    info_list.append(average_profit)
with open("file_7.json", "w") as new_file:
    dump(info_list, new_file)
