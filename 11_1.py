class Number(int):
    def __str__(self):
        return f"{self:02}"


class Date:
    date_attrs = ('day', 'month', 'year')

    def __init__(self, date: str):
        day, month, year = self.transform(date.split('-'))

        if not self.validate(day, month, year):
            raise ValueError(f'{date} - неправильный формат даты')

        self.day = day
        self.month = month
        self.year = year

    def __iter__(self):
        for attr in self.date_attrs:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date):
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date):
        if not all(map(lambda x: isinstance(x, int), date)):
            return False

        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1])

    def __str__(self):
        return f"Текущая дата '{'-'.join([str(d) for d in self])}'"


if __name__ == '__main__':
    try:
        print(Date('01-02-2022'))
        print(Date('12-13-2022'))
    except ValueError as error:
        print(error)
