""""Задача: развернуть слова в строке оставляя пробелы как есть"""
def is_pangrams(st):
    # print(sorted(''.join(st.split() if isalpha).upper()))

    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters = set(''.join(filter(str.isalpha, st)).upper())
    print(type(letters))
    return alphabet == letters

is_pangrams("     .lkri  lkejsf    JUktd   ")