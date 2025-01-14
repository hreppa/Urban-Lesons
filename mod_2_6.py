# TODO "Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа."

import random

def gen_first(fig):
  return random.randint(3, fig)

call_nubers = int(input('Введите число первой вставки: - '))

list_numbers = ''
counter = 0
while counter < call_nubers:
  first_numbers = gen_first(call_nubers)
  second_num = abs(first_numbers - call_nubers)
  # print(gen_first(call_nubers))
  list_numbers += str(first_numbers) # += str(second_num)
  list_numbers += str(second_num)
  counter += 1

print(list_numbers)
