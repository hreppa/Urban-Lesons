def longest_consec(strarr, k):
    elem_cnt = len(strarr)
    grup_cnt = 0
    counter_max  = 0 # сумма наибольшая
    res_concatinate = ""
    if k <= 0 or k >= elem_cnt or not strarr:
        return f'""'
    while grup_cnt < (elem_cnt - k + 1):
        for i in range(elem_cnt - k +1):
            concatinates = ''
            for n in range(k):
                concatinates += strarr[i + n]
                # cnt_let += len(strarr[i+n]) # + len(strarr[i+1])
            if counter_max < len(concatinates):
                counter_max = len(concatinates)
                res_concatinate = concatinates[::]
            else:
                continue
        return res_concatinate

def longest_consec_2(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

text_list = ["zone", "abigail", "theta", "form", "libe", "zas"]
text_list_2 = ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
print(longest_consec_2(text_list_2, 3))

# cnt_elements = len(text_list)
# print(p)
# n = 0
# k = 3
# # concatinate_leters_max = ''
# while n < (cnt_elements-k+1):
#
#     for i in range(cnt_elements-k+1):
#         n += 1
#         concat_leter = ''
#         for g in range(k):
#             concat_leter += text_list[i+g]
#         print(f'{n} - {text_list[i] + text_list[i+1]}')
#         print(concat_leter)
#         print(f'в списке слово {text_list[i]}')
#     print(n)
print(f'{"ixoyx3452zzzzzzzzzzzz"} результат')