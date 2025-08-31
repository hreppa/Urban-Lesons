def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    numbers = [i for i in range(a, b + 1)]
    numbers_str = [str(i) for i in numbers]
    for i in numbers_str:

        for j in range(len(i)):
            if int(i) == int(i[j]) ** (j + 1):
                result.append(int(i))
    return result

print(sum_dig_pow(88, 100))