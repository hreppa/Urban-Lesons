def is_palindrome(s):
    s1 = ''.join([i for i in s if i.isalnum()])
    return s1.lower() == s1[::-1].lower() # and s.isalnum()

# print(is_palindrome("A man, a plan, a canal. Panama"))
# print()


def comp(array1, array2):
    if array1 and array2:
        return sorted([(i**2) for i in array1]) == sorted(array2)
    else:
        return False


# a1 = [121, 144, 19, 161, 19, 144, 19, 11, 0.2]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19, 0.2*0.2]

a1 = [0.2]
a2 = [0.2**2]
print(a2 == a1, a2, a1)

print(comp(a1, a2))

import math

def comp_float(a, b, tol=1e-9):
    if a is None or b is None:
        return False
    if len(a) != len(b):
        return False
    try:
        sa = sorted(x*x for x in a)
        sb = sorted(b)
        return all(math.isclose(x, y, rel_tol=0.0, abs_tol=tol) for x, y in zip(sa, sb))
    except TypeError:
        return False

print(comp_float(a1, a2))
