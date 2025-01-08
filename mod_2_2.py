print('Задача на поиск одинаковых чисел')

import random

def number_gen():

    request = input('Для генерации  числа нажмите клавишу Enter')
    return random.randint(1, 10)


first = number_gen()

second = number_gen()

hird = number_gen()

if first == second and second == hird:
    print('совпали все тпи числа')

elif first == second or second == hird or first == hird:
    print('совпали два числа')

else:
    print('ничего не совпало')

print(first, second, hird)

