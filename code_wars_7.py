def delete_nth(order,max_e):
    new_lst = {}
    result = []
    max_cmt = 1
    for i in order:
        if new_lst.get(i, 0) < max_e:
            new_lst[i] = new_lst.get(i, 0) + 1
            result.append(i)

    return result

def delete_nth_2(order,max_e):
    result = []
    for i in order:
        if result.count(i) < max_e: result.append(i)

    return result


lst_1 = [20,37,20,21, 21, 20, 37,40, 37, 37, 40]
new_lst = {}
result = []
max_cmt = 1
for i in lst_1:
    if i not in new_lst:
        new_lst[i] = 1
        result.append(i)
    elif new_lst[i] < max_cmt:
        new_lst[i] += 1
        result.append(i)
    else:
        continue

# print(result)
print(lst_1)

print(delete_nth_2(lst_1, 1))

dict_1 = enumerate(lst_1)
# print(dict(dict_1))

# print([lst_1.count(x) for x in lst_1])

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    return []

