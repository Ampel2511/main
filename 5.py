from functools import reduce


def product(prev, current):
    return prev * current


numbers = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(product, numbers))
