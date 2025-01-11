# TODO "Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа."

import random

def num_gen():
    """
    генератор двузначного чилса
    возвращает число и сумму цифр
    ab (str), ab_sum (int)
    """
    a = random.randint(0,10)
    b = random.randint(0,10)
    ab = str(a) + str(b)
    ab_sum = a + b
    return ab,  ab_sum

def password_gen(figer):
    # code_list = []
    # for i in range(1, figer):

    pass

# base_number = int(input('Введите число от 3 до 20 на основе которого будет сгенерирована кодовая последовательность. - '))
#
# code_number = password_gen(base_number)
# print(f'Кодовое число\n\t {code_number}')

num_gen()
