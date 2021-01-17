file = open("file_6.txt", "r")
info = {}
# существует способ вытащить из строки, многомерного массива и тд только определенные значения, например только цифры, чтобы избежать этого?
for i in file.read().replace("-", "").replace(":", "").replace("(лаб)", "").replace("(пр)", "").replace("(л)", "").split():
    if i.isalpha():
        key = i
        info[key] = 0
    elif i.isdigit():
        info[key] += int(i)
file.close()
print(info)
