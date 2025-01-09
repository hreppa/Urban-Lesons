# ToDoo
# Запишите исходный список в переменную my_list.
# Напишите цикл while с соответствующими задаче условиями.
# Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

count_ = 0

while count_ < len(my_list):

    if my_list[count_] >= 0:
        if my_list[count_] == 0:
            count_ += 1
            continue
        print(my_list[count_])
        count_ += 1
    else:
        break

print('на этом всё')
