line = input("Введите строку, чтобы выйти введите пустую строку ")
while line != " ":
    file = open("file_1.txt", "a")
    file.write(f"{line}\n")
    file.close()
    line = input("Введите строку, чтобы выйти введите пустую строку ")
