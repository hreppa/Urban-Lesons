a = '4560789'

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
    clean = ''
    for i in num:
        if i != '0':
            clean = clean + i

    return clean

print(clean_num(a))