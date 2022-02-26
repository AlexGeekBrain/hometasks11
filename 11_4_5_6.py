class OfficeEquipment:
    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    def __init__(self, model, price, dpi, paper_size, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    def __init__(self, model, price, dpi, paper_size):
        super().__init__(model, price, dpi, paper_size)


class Copier(OfficeEquipment):
    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_size)


class Warehouse:
    __equipments = dict()
    __issued_equipments = dict()

    def add_equipment(self, key, val):
        if self.__equipments.get(key)  == None:
            self.__equipments[key] = 0
        self.__equipments[key] += val

    def issue_equipment(self, key, val):
        extradition = self.__equipments.get(key)
        if extradition != None and extradition >= val:
            self.__equipments[key] -= val
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def numbers(self, key):
        val = self.__equipments.get(key)
        return val if val != None else 0

    def equipments_in_warehouse(self):
        print('Список продукции на складе:')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.numbers(i)} шт.')
        print('-----')

    def issued_equipments(self):
        print(f'\nВыдано в офис:\n{self.__equipments}')


models = [Printer('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet'),
          Printer('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet'),
          Copier('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000),
          Scanner('EPSON Perfection V19', 5110, '4800×4800', 'A3')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:
    print('\nМеню:\n1 - Поставка на склад.\n2 - Выдача со склада.\nEXT - Выход.')
    action = input('> ')
    if action in ['1', '2']:
        s = ''
        for i, eq in enumerate(models):
            s += f'\n({i}) {eq.model} ({warehouse.numbers(i)} шт.)'

        while True:
            print(f'\nВведите модель и количество: {s}')
            try:
                model = int(input('Модель: '))
                if model in range(len(models)):
                    n = int(input('Количество: '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от 0 до {len(models)}')
                continue
            else:
                print('\nОперация выполнена:')
                if (action == '1'):
                    print(f'Принято на склад {models[model].model} - {n} шт.\n')
                    warehouse.add_equipment(model, n)
                elif (action == '2'):
                    m = warehouse.numbers(model)
                    if (n > m):
                        n = m
                        print(f'ВНИМАНИЕ! На складе всего {n} шт. {models[model].model}!')
                    print(f'Выдано со скалада {models[model].model} = {n} шт.\n')
                    warehouse.issue_equipment(model, n)

                warehouse.equipments_in_warehouse()
                break

    elif action == 'EXT':
        print('Вы вышли из программы.')
        break
    else:
        print('Некорректный ввод. Для выбора введите цифры 1 или 2.\nДля выхода из программы введите EXT.')
