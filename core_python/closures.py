"""Замыкания.
Замыкание — это функция, которая динамически генерируется другой функцией,
и они обе могут изменяться и запоминать значения переменных,
которые были созданы вне функции."""


def knights(saying):
    def inner():
        return f'We are the knights who say: {saying}'
    return inner


names = ['Duck', 'Hasenpfeffer']
for name in names:
    # здесь запоминаем функцию с параметрами
    func = knights(name)
    # здесь вызываем её
    print(func())
