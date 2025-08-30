
def smash(words):
    # return (" ".join(i for i in words)).strip()
    return " ".join(words)

# print(smash(["hello", "amazing", "world"]))


def find_it(seq):
    seq_set = set(seq)
    # print(seq_set)
    # for i in seq_set:
    #     print(f'число {i} повторяется {seq.count(i)} раз')
    return next(i for i in seq_set if seq.count(i) % 2 != 0)

# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

def series_sum(n):
    # Happy Coding ^_^
    return f'{(sum(1/(i+1) for i in range(0, 3*n, 3))):.2f}'

# answer = series_sum(1)
# print(answer, type(answer))

n = 3
total = 0
# for i in range(0, 3*n, 3):
#     # print(i)
#     a = 1
#     a += i
#     total += 1/a
#     print(i, a, round(total, 2))


def sum_array(arr = []):

    return sum(arr) - min(arr) - max(arr) if len(arr) > 2 else 0

# print(sum_array([-6, -20, -1, -10, -12]))
# print(sum_array([ 3, 5, -10]))
# print(sum_array())

"""Задача в которой надо представить в которой надо вывести номер Века 
    введеного года """
year = 1800

last_fig = year%100
# print(last_fig[-1])

if last_fig == 0:
    century = int(year/100)
else:
    century = int(year/100) + 1
# print(century)

"""" каждую букву в строке пердставить порядковым номером в алфавите """

alphabet = {c: i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}
# print(alphabet['a'])
def alphabet_position(text):
    text_by_number = ""
    text_by_nuomber_2 = ""
    for i in text.lower():
        if i.isalpha():
            # text_by_nuomber += alphabet[i]
            text_by_nuomber_2 = " ".join(alphabet[i])
        else:
            continue

def alphabet_position_2(text):
    return " ".join(
            str(ord(c) - 96) # ord('a') == 97
            for c in text.lower()
            if 'a' <= c <= 'z' # гарантируем, что берем только латинские буквы
                    )

# print(alphabet_position_2("The sunset sets at twelve o' clock."))
# print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
#
# print(alphabet_position_2("The narwhal bacons at midnight."))
# print("20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

def tribonacci(signature, n):
    """Задача Трибоначи"""
    if n > 3:
        while len(signature) < n:
            signature.append(sum(signature[-3:]))

    elif n == 0:
        return []
    return signature[:n]

figures = [5, 10, -3]
# print(tribonacci(figures, 10))
import math
def find_nb(m):
    # t = math.sqrt(m)
    # # print(t)
    # if t**2 != m:
    #     return f'-1 не квадрат'
    # disk = 1+8*t
    # # print(disk)
    # r = math.sqrt(disk)
    # if r**2 != disk: return -1
    # n = (r-1)//2
    # return n if n*(n+1)//2 == t else -1
    count = 0
    res = 0
    while res < m:
        count += 1
        res += count ** 3

    return count if res==m else -1


# print(find_nb(16))
26825883955641
# print(find_nb( 8398419336223001316))

def likes(names):
    count = len(names)
    if not names:
        return "no one likes this"
    elif count == 1: return f'{names[0]} likes this'
    elif count == 2: return f'{names[0]} and {names[1]} like this'
    elif count == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif count > 3:
        others = count - 2
        return f'{names[0]}, {names[1]} and {others} others like this'

def likes_2(names):
    match len(names):
        case 0: return "no one likes this"
        case 1: return f'{names[0]} likes this'
        case 2: return f'{names[0]} and {names[1]} like this'
        case 3: return f'{names[0]}, {names[1]} and {names[2]} like this'
        case n: return f'{names[0]}, {names[1]} and {n-2} others like this'


list_names = ['Alex', 'Jacob', 'Mark', 'Max']
list_names2 = ['Alex', 'Jacob', 'Mark']
list_names3 = []

# print(likes_2(list_names))

def two_sum(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

figures = [1 ,2, 3]
# print(two_sum(figures, 4))

def filter_list(l):
    # new_list = []
    # for i in l:
    #     if i.isdigist():
    return [d for d in l if isinstance(d, int)]

# print(filter_list([1, 2, 'aasf', '1', '123', 123]))

def double_char(s):
    return "".join(i*2 for i in s)

# print(double_char("Hello World"))

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - son_years_old*2)

# print(twice_as_old(55,30))

def string_to_array(s):
    return s.split(" ")

# print(string_to_array(""))

def reverse_seq(n):
    # return list(range(n,0,-1))
    return type(range(n, 0, -1))

# print(reverse_seq(5))

def array_diff(a, b):
    return [i for i in a if i not in b]

# print(array_diff([1,2,3], [1, 2]))

def number(lines):
    numbered_lines = []
    for i in range(len(lines)):

        numbered_lines.append(f'{i+1}: {lines[i]}')
    return numbered_lines

def number_2(lines):
    return [f'{i+1}: {line}' for i, line in enumerate(lines, 1)]
# print(number(["a", "b", "c"]))
# print(number(["a", "b", "c", "dip"]))

# def longest_consec(strarr, k):
#     elem_cnt = len(strarr)
#     counter_ch  = 0 # сумма наибольшая
#     res_concatinate = ""
#     for i in range(elem_cnt - 1):
#         for n in range(k):
#         cnt_let += len(strarr[i+n]) # + len(strarr[i+1])
#         if counter_ch >= cnt_let:
#             continue
#         else:
#             res_concatinate = strarr[i] + strarr[i+1]
#     return res_concatinate

# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

text_list = ["zone", "abigail", "theta", "form", "libe", "zas"]
p = len(text_list)
print(p)
n = 1
k = 2
# concatinate_leter = ''
while n < p:
    n += 1
    for i in range(p-k+1):
        concat_leter = ''
        for n in range(k):
            concat_leter += text_list[i+n]
        print(f'{n} - {text_list[i] + text_list[i+1]}')
        print(concat_leter)
        print(f'в списке слово {text_list[i]}')
    print(n)
print(f'{"abigailtheta"}')

