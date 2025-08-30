# def delete_nth(order,max_e):
#     order_set = dict(order)
#     for i in order_set:
#     order_new = [x for x in order if order.count(x) <= max_e]
#     return order_new
#
# print(delete_nth([20,37,20,21, 21, 20, 37, 37, 37], 1))


lst_1 = [20,37,20,21, 21, 20, 37, 37, 37]
dict_1 = enumerate(lst_1)
print(dict(dict_1))

# print([lst_1.count(x) for x in lst_1])