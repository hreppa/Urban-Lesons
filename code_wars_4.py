def fibanachi(a):
    fib_numbers = [0, 1]
    if a > 0:
        count = 1
        fib_numbers.append(1)
        while count < a:
            for i in range(1, a):
                j = sum(fib_numbers[-2:])
                fib_numbers.append(j)
                count += 1

    return fib_numbers[-1]

print(fibanachi(5))

big = 8
print(fibanachi(big), fibanachi(big+1))
print(fibanachi(big)*fibanachi(big+1))

need_grup = fibanachi(6)

shoot = need_grup**0.5

print(shoot)

def product_fib(_prod):
    next_fig = 0
    while next_fig <= _prod:
        prod_result = fibanachi(next_fig) * fibanachi(next_fig + 1)
        if prod_result < _prod:
            next_fig += 1
            continue
        elif prod_result == _prod:
            return f'{fibanachi(next_fig)}, {fibanachi(next_fig + 1)}, True'
        elif _prod == 0:
            return [0, 1, True]
        else:
            return f'{fibanachi(next_fig)}, {fibanachi(next_fig+1)}, False'


print(product_fib(0))

print(product_fib(5895))

def product_fib(prod: int):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]

print(product_fib(800))


def between(a,b):
    return list(range(a,b+1))

print(between(2, 9))

def powers_of_two(n):
    return [2**i for i in range(0, n+1)] # if n > 0 else 1] #

print(powers_of_two(0))

def check(seq, elem):
    return elem in seq

print(check([78, 117, 110, 99, 8, 104, 117, 107, 115], 8))

def no_space(x):
    new_str = ''
    return '-*-'.join(x.split())

text = '8 j 8   mBliB8g  imjB8B8  jl  B'
# print(text.split())
# print(text.replace(' ', ''))
#
# print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))

def duplicate_count(text):
    big_leter = text.replace(' ', '').lower()
    # leters_set = set(big_leter)
    count_doubles = 0
    doubles_leters = []
    for i in set(big_leter):
        if big_leter.count(i) > 1:
            count_doubles += 1
            doubles_leters.append(i)
    return count_doubles, doubles_leters

from collections import Counter

def duplicate_count_2(text):
    # если хотите игнорировать всё, кроме букв и цифр:
    # s = ''.join(ch.lower() for ch in text if ch.isalnum())
    s = ''.join(ch.lower() for ch in text if not ch.isspace())
    # если нужно лишь убрать пробельные символы, используйте: if not ch.isspace()
    # return sum(cnt > 1 for cnt in Counter(s).values())
    return sum(cnt > 1 for cnt in Counter(s).values())

print(dict(cnt for cnt in Counter(''.join(ch.lower() for ch in text if not ch.isspace())).items()))
# big_leter = text.replace(' ', '').lower()
# leters_set = set(big_leter)
# print(big_leter, leters_set)
# print(duplicate_count(text))
# print(duplicate_count_2(text))

import copy

def remove_smallest(numbers):
    new_numbers = copy.deepcopy(numbers)
    figure_min = min(new_numbers)
    idx = new_numbers.index(figure_min)
    print(idx)
    return new_numbers[:idx] + new_numbers[idx + 1:]

fig = [5, 3, 1, 2, 1, 4]
new_numbers = copy.deepcopy(fig)
new_numbers.remove(min(new_numbers))

print(f'{remove_smallest(fig)} а что не так?')
print(f'{fig} старый или новый а это новый список {new_numbers}')

print(fake_bin("45385593107843568"))
