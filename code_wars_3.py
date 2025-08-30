"""Задача про светофоры"""
from mod_3_5 import result


def update_light(current):
    match current:
        case 'green': return 'yellow'
        case 'yellow': return 'red'
        case 'red': return 'green'


# print(update_light('yellow'))
# print(update_light('red'))
# print(update_light('green'))

def first_non_consecutive(arr):
    '''перебираем элементы списка и сравниваем с соседним справа'''
    for i in range(len(arr)-1):
        # diferent = arr[i+1] - arr[i]
        # print(f'сравниваем {arr[i]} и {arr[i+1]}, разница:  {diferent}')
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]

    return None

# print(first_non_consecutive([1,2,3,4,6,7,8]))
# print(first_non_consecutive([1,2,3,4,5,6,7,8]))

def _apply(n, op):
    return n if op is None else op(n)

def zero(op=None): return _apply(0, op)
def one(op=None): return _apply(1, op)
def two(op=None): return _apply(2, op)
def three(op=None): return _apply(3, op)
def four(op=None): return _apply(4, op)
def five(op=None): return _apply(5, op)
def six(op=None): return _apply(6, op)
def seven(op=None): return _apply(7, op)
def eight(op=None): return _apply(8, op)
def nine(op=None): return _apply(9, op)

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y

# print(one(times(two())))
# print(seven(plus(five())))

def fibanachi(a):
    fib_numbers = [0]
    if a > 0:
        count = 0
        fib_numbers.append(1)
        while count < a:
            for i in range(1, a):
                j = sum(fib_numbers[-2:])
                fib_numbers.append(j)
                count += 1

    return fib_numbers[-1]

print(fibanachi(2))
