def is_prime_figure(fig):
    """
    функция определяющая Простое число или нет

    """

    for i in range(2, int((fig**0.5) + 1)):
        if fig % i == 0:
            break
        return True
    else:
        return False


numbers = [i for i in range(1, 21)] # создаем список от 1 до 15

print(numbers)

prim_nums = [] # список для сбора простых чисел

not_prim_nums = [] # список для сбора не простых чисел

for elem in numbers:
    if elem == 1:
        continue
    elif elem == 2:
        prim_nums.append(elem)
    elif is_prime_figure(elem):
        prim_nums.append(elem)
    else:
        not_prim_nums.append(elem)


print(f'Список простых чисел: {prim_nums}')

print(f'Список непростых чисел: {not_prim_nums}')
