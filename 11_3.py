class IsNotNumber(Exception):
    text = 'Это не число!'

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        try:
            user_input = input('Введите число для заполнения списка, после "stop" для выхода: ')
            if user_input == 'stop':
                print('Вы вышли из программы')
                break
            if not user_input.isdigit():
                raise IsNotNumber
            my_list.append(int(user_input))
        except IsNotNumber as error:
            print(error)

    print(my_list)
