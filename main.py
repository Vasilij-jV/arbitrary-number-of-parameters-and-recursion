# -*- config: utf-8 -*-

# Произвольные параметры
def test(*args, **kwargs):
    for i, arg in enumerate(args):
        print(f'Элемент кортежа: {i} - {arg}')
    for key, value in kwargs.items():
        print(f'Элемент словаря: {key} - {value}')

test([4, 'Lada', True], 834578, (4, 6, 87), table='wooden', sofa='soft', chair='stable', refrigerator='white')

# Факториал
def factorial_calculation(n):
    if n == 1:
        return 1
    n_mines_one = factorial_calculation(n=n - 1)
    return n * n_mines_one

print(factorial_calculation(23))
