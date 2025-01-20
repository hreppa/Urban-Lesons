a = '450607809'

# def last_num(num):
#     print(num)
#     a = len(num)
#     print(a)
#     if a >= 1:
#         first = num[1:]
#         # print(first)
#         # last_num(first[1:])
#         first = last_num(first)# a -= 1
#     else:
#         return first
# last_num(a)

def clean_num(num):
    """
    функция для очистки строки от нулей
    """
    clean = ''
    for i in num:
        if i != '0':
            clean = clean + i

    return clean

print(clean_num(a))
experiment = clean_num(a)

# def f_num(num):
#     nekst = num[1:]
#     first = num[0]
#     if len(num) > 0:
#         print(first)
#         print(f_num(nekst))
#     # return sum_num

# print(f_num(experiment))

# print(clean(__doc__))

print(dir(experiment))

# print(dir(a))
