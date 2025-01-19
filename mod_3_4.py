# Задача "Однокоренные":
#
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
#
# Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.
#
#
#
# Пункты задачи:
#
# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# При помощи цикла for переберите предполагаемо подходящие слова.
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
# Пример результата выполнения программы:
#
# Исходный код:
#
# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
#
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
#
# print(result1)
#
# print(result2)
#
# Вывод на консоль:
#
# ['richiest', 'orichalcum', 'richies']
#
# ['Able', 'Disable']

def own_root_word(root, *words):
  same_words = []
  root_lower = root.lower()
  print(root_lower)
  for word in words:
    word_lower = word.lower()
    print(word_lower)
    if root_lower in word_lower:
      same_words.append(word)
  return same_words


words_1 = ['rich', 'richiest', 'orichalcum', 'cheers', 'richies']

words_2 = ['Able', 'Mable', 'Disable', 'Bagel']

result_1 = own_root_word('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result_2 = own_root_word('Able', 'Disablement', 'Mable', 'Disable', 'Bagel')

print(result_1)
print(result_2)
#print(words_2[0], words_2[1][0])
