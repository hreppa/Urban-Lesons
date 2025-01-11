def is_prime_figure(fig):

    for i in range(2, int((fig**0.5) + 1)):

        if fig % i != 0:

        return True

    else:

        return False


numbers = [i for i in range(1, 16)]

print(numbers)

prim_nums = []

not_prim_nums = []



for elem in numbers:

    if elem == 1:

        continue

    elif is_prime_figure(elem):

        prim_nums.append(elem)

    else:

        not_prim_nums.append(elem)


print(f'Список простых чисел: {prim_nums}')

print(f'Список непростых чисел: {not_prim_nums}')