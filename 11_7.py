class ComplexNumber:
    def __init__(self, real, imag=0):
        self.complex = complex(real, imag)

    def __add__(self, other):
        return ComplexNumber(self.complex + other.complex)

    def __mul__(self, other):
        return ComplexNumber(self.complex * other.complex)

    def __str__(self):
        return f'{self.complex}'


a = ComplexNumber(5, 6)
b = ComplexNumber(3, 1)

print(a + b)
print(a * b)
