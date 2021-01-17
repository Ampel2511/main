f = open("file_4.txt", "r")
for line in f:
    file_2 = open("file_4.1.txt", "a")
    print(f'{line.replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре")}',
          file=file_2)
