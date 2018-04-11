def Descending_Order(num):
    str_num = list(str(num))
    str_num.sort(reverse=True)
    return int(''.join(str_num))


print Descending_Order(0)       # 0
print Descending_Order(15)      # 51
print Descending_Order(123456789)   # 987654321