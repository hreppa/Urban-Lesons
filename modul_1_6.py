# Пример результата выполнения программы:
#
# Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
#
# Existing value: 2002
#
# Not existing value: None
#
# Deleted value: 1999
#
# Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}
#
#
# Set: {1, 'Яблоко', 42.314}
#
# Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}

# Создаём библиотеку
my_dict = {"Petr": 1964, 'Ivan': 1966, "Egor": 1111}

# выводим на печать
print(f'Dict: {my_dict}')

# выводим на печать значение с ключом Егор
print(f'Existing value: {my_dict['Egor']}')

# обращаемся к несуществующему ключу, вывод без ошибки
print(f'Existing value: {my_dict.get('Gosha')}')

# создали ещё одну библиотеку для слияния
new_dict = {'Klusha': 1988, 'Sam': 1999}

# удаляем ключ из библиотеки с выводам значения на печать
print(f'Deleted value: {my_dict.pop('Egor')}')

# Сливаем две библиотеки в одну
my_dict.update(new_dict)

# выводим обновлённую библиотеку на печать
print(f'Modified dictionary: {my_dict}')
print()

# создаем множество
my_set = {124, 'Груша', 3.14}

print(f'Set: {my_set}')

# Создаём вспом кортеж
dop_set = (True, False)

# добавляем кортеж в множество
my_set.add(dop_set)

print(f'Modified set: {my_set}')
