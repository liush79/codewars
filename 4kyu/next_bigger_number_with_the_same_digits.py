def find_next(str_n):
    first_value = str_n[0]
    idx = 1
    while True:
        if str_n[-idx] > first_value:
            result = str_n[-idx]
            del str_n[-idx]
            str_n.sort()
            result += ''.join(str_n)
            return result
        idx += 1


def next_bigger(n):
    str_n = str(n)
    len_str = len(str_n)
    for idx in range(1, len_str+1):
        copy_str = list(str_n[-idx:])
        copy_str.sort()
        copy_str.reverse()
        if list(str_n[-idx:]) == copy_str:
            continue
        return int(str_n[:len_str-idx] + find_next(list(str_n[-idx:])))
    return -1


print next_bigger(12)       # 21
print next_bigger(513)      # 531
print next_bigger(2017)     # 2071
print next_bigger(414)      # 441
print next_bigger(144)      # 414
