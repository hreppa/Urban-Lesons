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

# print(dir(experiment))

# print(dir(a))


# print('рисование треугольников')
#
#
# # -*- coding: utf-8 -*-
#
# # pip install simple_draw
#
# import simple_draw as sd
#
# # нарисовать треугольник из точки (300, 300) с длиной стороны 200
# length = 200
# point = sd.get_point(300, 300)
#
# # v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# # v1.draw()
# #
# # v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# # v2.draw()
# #
# # v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# # v3.draw()
#
# # определить функцию рисования треугольника из заданной точки с заданным наклоном
# def triangle(point, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
#     v3.draw()
#
#
# point_0 = sd.get_point(300, 300)
#
# for angle in range(0, 361, 30):
#     triangle(point=point_0, angle=angle)
#
# sd.pause()

a = {'cube': 7, 'drum': 8}
for key in a:
    print(key, a[key])
    if isinstance(key,str):
        print(f'{key} count symbol {len(key)}')