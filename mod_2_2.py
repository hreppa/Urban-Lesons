print('Задача на поиск одинаковых чисел')

import random

def number_gen():

    request = input('Для генерации  числа нажмите клавишу Enter')
    return random.randint(1, 10)

cont = True

while cont:
    print()
    first = number_gen()

    second = number_gen()

    hird = number_gen()

    print()
    num_list = [first, second, hird]

    if first == second and second == hird:
        print(f'{num_list} - совпали все тпи числа')

    elif first == second or second == hird or first == hird:
        print(f'{num_list} - совпали два числа')

    else:
        print(f'{num_list} - ничего не совпало')
    print()
    go_ahed = input('продолжить - Enter, закончить - Y')
    a = go_ahed.lower()
    if a == 'y':
        cont = False

print('Игра закончена')
