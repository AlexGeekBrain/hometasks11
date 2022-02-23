# не успел доделать ((
class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, color):
        self.name = name
        self.make = make
        self.color = color
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.color}'


class Printer(Equipment):
    def __init__(self, name, make, color):
        super().__init__(name, make, color)

    def __repr__(self):
        return f'{self.name}, {self.make}, {self.color}'


class Scaner(Equipment):
    def __init__(self, name, make, color):
        super().__init__(name, make, color)


class Xerox(Sklad):
    def __init__(self, name, make, color):
        super().__init__(name, make, color)


sklad = Sklad()
scaner = Scaner('hp', '321', 'black')
sklad.add_to(scaner)
scaner = Scaner('hp', '311', 'white')
sklad.add_to(scaner)
scaner = Scaner('hp', '330', 'white')
sklad.add_to(scaner)
printer = Printer('e-320', 'sony', 'gray')
sklad.add_to(printer)
print(sklad._dict)
sklad.extract('Scaner')
print(sklad._dict)
