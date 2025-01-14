# TODO  написать 3 функции:
# # Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(anything):
    how_mach = len(anything)
    a = anything.lower()
    b = anything.upper()
    global calls
    calls += 1
    return how_mach, a, b


def is_contains(a, b, c):
    global calls
    calls += 1
    unswer = False
    for i in b:
        g = i.lower()
        # print(g)
        if c not in g:
            unswer1 = False
            break
        else:
            # print(g)
            unswer1 = True

    if c in a:
        c.lower()

        unswer2 = True


    if unswer1 and unswer2:
        unswer = True
    return unswer



print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'], 'ban')) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'], 'cycl')) # No matches

print(is_contains('cycle', ['recycling', 'cyclic'], 'ban')) # No matches

print(f'всего вызовов функций - {calls}')
