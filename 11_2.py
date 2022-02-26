class ZeroError(Exception):
    text = 'Деление на ноль запрещено!'

    def __str__(self):
        return self.text


class UserInput(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroError
        return UserInput(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(UserInput, input('Разделите два числа: ').split('/'))
            print(dividend / divider)
        except ZeroError as error:
            print(error)
            break
