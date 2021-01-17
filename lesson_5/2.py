with open("file_2.txt") as file:
    words = 0
    for i, lines in enumerate(file.readlines(), 1):
        words += len(lines.split())
    print(f"Строк - {i}, слов - {words}")
