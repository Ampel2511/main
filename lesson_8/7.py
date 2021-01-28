class Complex:
    def __init__(self, a, b):
        self.complex = complex(a, b)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


num_1 = Complex(4, -6)
num_2 = Complex(5, 9)
print(num_2 + num_1)
print(num_1 * num_2)
