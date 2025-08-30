def is_valid_walk(walk):
    if len(walk) > 10:
        return False
    lockation = [0, 0]
    count = 0
    while count < 10:
        for i in walk:
            if i == 'e':
                lockation[0] += 1
            elif i == 'w':
                lockation[0] -= 1
            elif i == 's':
                lockation[1] += 1
            elif i == 'n':
                lockation[1] -= 1
            count += 1

    return True if lockation == [0,0] else False

def is_valid_walk_2(walk):
    return (len(walk)==10 and walk.count('e') == walk.count('w') and walk.count('s') == walk.count('n'))

# task = ['n','s','n','s','n','s','n','s','n','s', 'w']
task = ['n','s','n','s','n','s','n','s','n']

print(is_valid_walk(task))

def cockroach_speed(s):
    return int(s*1000/36)

print(cockroach_speed(1.09))
print(round(1.5*100000/3600))
print(int(1.5*100000/3600))
print(1.5*100000/3600)

def remove_every_other(my_list):
    return my_list[::2]

words_5 = ['Hello', 'Goodbye', 'Hello Again']
words_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(remove_every_other(words_5))
a = enumerate(words_6)
print(dict(a))