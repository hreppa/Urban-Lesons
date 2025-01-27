# Задание "Раз, два, три, четыре, пять .... Это не всё?":
#
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
#
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
#
#
#
# data_structure = [
#
#   [1, 2, 3],
#
#   {'a': 4, 'b': 5},
#
#   (6, {'cube': 7, 'drum': 8}),
#
#   "Hello",
#
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
#
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
#
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.
#
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
#
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
#
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
#
# data_structure = [
#
# [1, 2, 3],
#
# {'a': 4, 'b': 5},
#
# (6, {'cube': 7, 'drum': 8}),
#
# "Hello",
#
# ((), [{(2, 'Urban', ('Urban2', 35))}])
#
# ]
#
# result = calculate_structure_sum(data_structure)
#
# print(result)
#
# Выходные данные (консоль):
#
# 99

# def calculate_structure_sum(data):
#     """
#     функция раскрытия структуры списка
#     """

def calculate_structure_sum(mass):
    count = 0
    for elem in mass:
        print(elem)
        if isinstance(elem, str):
            if elem.isalpha:
                print(elem)
                count += len(elem)
            # elif elem.isdigit:
            #   return int(elem)
            elif isinstance(elem, int):
                print(elem)
                count += elem
        elif isinstance(elem, list):
            print(elem)
            for i in range(len(elem)):
                count += calculate_structure_sum(elem[i])
                # return count_figure_list(elem)
        elif isinstance(elem, dict):
            print(elem)
            for i in elem:
                # print(calculate_structure_sum(i), calculate_structure_sum(mass[i]))
                count += (calculate_structure_sum(i) + calculate_structure_sum(elem[i]))
                # return count_figure_dict(elem)
        elif isinstance(elem, set):
            print(elem)
            count += calculate_structure_sum(elem)
        else:
            count += elem
            break
    return count


def next_try(mass):
    for elem in mass:
        # print(elem)
        # if not isinstance(elem, int)
        print(type(elem), elem)
        if isinstance(elem, list):
            print('это список')
            for i in elem:
                print(i, type(i))
        elif isinstance(elem, dict):
            print("это библиотека")
            for i in elem:
                print(i, elem[i])
        elif isinstance(elem, tuple):
            print('это кортеж')
            for i in elem:
                print(i)
                # if not isinstance(i, int):
                #     print(f'он состоит из - {next_try(i)}: {type(i)}')
                #     print()
        elif isinstance(elem, set):
            print('это множество')
            for i in elem:
                print(f'он состоит из - {i}')

def next_try_2(mass):
    for i in range(len(mass)):
        print(i)
        print(next_try(mass[i]))

data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

# result = calculate_structure_sum(data_structure)
#
# print(result)
# next_try(data_structure)
next_try_2(data_structure)