rate = 0
with open("file_3.txt") as file:
    for data in file.readlines():
        if int(data.split()[1]) > 19000:
            print(data.split()[0])
        rate += int(data.split()[1])
    file.seek(0)
    rate /= len(file.readlines())
    print(rate)
