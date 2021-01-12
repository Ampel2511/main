from random import randint
numbers = [randint(0, 50) for i in range(0, 50)]
print(numbers)
numbers = [numbers[i] for i in range(0, len(numbers)) if numbers.count(numbers[i]) == 1]
print(numbers)
