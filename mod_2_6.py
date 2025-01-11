# TODO "Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа."

import random

def num_gen(fig):
    """
    генератор двузначного чилса
    возвращает число и сумму цифр
    ab (str), ab_sum (int)
    """
    a = random.randint(0,fig)
    # b = random.randint(0,10)
    # ab = str(a) + str(b)
    # ab_sum = a + b
    return a

def password_gen(figer):
    code_list = ''
    for i in range(3, figer):
        while True:
            if figer % num_gen(figer) == 0:
                code_list.join(num_gen())
                break
            continue
    return code_list

base_number = int(input('Введите число от 3 до 20 для создания кодового числа: '))+1

code_number = password_gen(base_number)
print(f'Кодовое число\n\t {code_number}')

print(num_gen()[1], num_gen())
print(num_gen()[0], num_gen()[1])
