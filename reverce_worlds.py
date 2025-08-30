""""Задача: развернуть слова в строке оставляя пробелы как есть"""
def is_pangrams(st):
    # print(sorted(''.join(st.split() if isalpha).upper()))

    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters = set(''.join(filter(str.isalpha, st)).upper())
    return alphabet <= letters

is_pangrams("     .lkri  lkejsf    JUktd   ")

def add_binary(a, b):
    return (bin(a + b)[2:])

# print(add_binary(39, 10))

fig = add_binary(9, 10)

# print(type(fig), fig)

import re

def printer_error(s):
    return f'{len(re.findall(r'[n-z]', s))}/{len(s)}'

# print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))

def abc(sequence):
    unique = []
    for i in sequence:
        if not unique or i != unique[-1]:
            unique.append(i)
    return list(unique)

# print(abc("AAAABBBCCDAABBB"))
simbols = ([1, 2, 2, 3, 3, 3, 2])
# print(abc(simbols))

def find_smallest_int(arr):
    # Code here
    return min(arr)

# print(find_smallest_int([5, -5,10, -10]))
count = 0
def persistence(n, trace = False):
    # your code
    count = 0

    while n >= 10:
        if trace:
            a = 1
            for i in str(n):
                a *= int(i)
                print(a, count, end=' -> ')
            n = a
            count += 1
        if trace:
            print(n)
    # return 1+ persistence(a)
    return count


# print(persistence(999, trace=True))

def presistence_recurstion(n):
    if n < 10:
        return 0
    asist = 1
    for i in str(n):
        asist *= int(i)
    return 1 + presistence_recurstion(asist)

# print(presistence_recurstion(999))

def order(centence: str) -> str:
    words = centence.split()
    words_lib = {}

    for i in words:
        for leter in i:
            if leter.isdigit():
                words_lib[leter] = i
        figure_in_word = sorted(words_lib)
        print(figure_in_word)
        valut_str = ''
        for keys in figure_in_word:
            print(figure_in_word[keys])
            # valut_str += figure_in_word[keys]
    return valut_str

a = "is2 Thi1s T4est 3a"
# print(order(a))


def are_you_playing_banjo(name):
    if name[0].upper() == 'R':
        return f'{name} plays banjo'

    return f'{name} does not play banjo'

# print(are_you_playing_banjo('Bravo'))
# print(are_you_playing_banjo('ravo'))


def sum_mix(arr):
    total = 0
    for i in arr:
        if isinstance(i, str):
            total += int(i)
        else:
            total += i

    return total

def sum_mix_2(arr):
    return sum(x for x in arr)


# print(sum_mix_2([1,2,3.8,4.5,-5.3]))
# print(sum_mix_2([]))

def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))
# print(square_digits(159))

def get_count(sentence):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for leter in sentence:
        if leter in vowels:
            count += 1
    return count

def get_count_2(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(letters in vowels for letters in sentence)

# print(get_count("aeiou"))

def number(bus_stops):
    stops = len(bus_stops)
    outgoing = 0
    incoming = 0

    for stop in range(stops):
        incoming += bus_stops[stop][0]
        outgoing += bus_stops[stop][1]
    print(f'вошло {incoming}, вышло {outgoing}')
    remane = incoming - outgoing
    return f'{remane} человек осталось в автобусе'

def number_2(bus_stops):
    return sum(on - off for on, off in bus_stops)

# print(number_2([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))

unique = {}
nums = [ 1, 1, 1, 2, 1, 1, 3,3,3 ]
# print(nums.count(3))
for i in nums:
    if i not in unique:
        unique[i] = nums.count(i)
# print(unique.keys() if unique.values() < 2 else None)
for elem, cnt in unique.items():
    print(elem)
    if cnt == 1:
        print(f'уникальное число {elem}')

from collections import Counter

def unique_num(nums):
    cnt_tuple = Counter(nums)
    for elem, cnt in cnt_tuple.items():
        if cnt == 1:
            return elem

print(f'{unique_num(nums)} уникальное число')

a = set(nums)
print(a)
cnt = {}
for i in a:
    cnt[i] = nums.count(i)

print(cnt)