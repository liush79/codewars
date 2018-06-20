def merge(line):
    res = []
    pre = 0
    for n in line:
        if n == 0:
            continue
        if pre == 0:
            pre = n
        elif n == pre:
            res.append(2 * n)
            pre = 0
        else:
            res.append(pre)
            pre = n

    res += [pre] + [0] * (len(line) - len(res) - 1)
    return res


print merge([0, 2, 2, 2])  #
print merge([2, 0, 4, 2])  #
print merge([2, 0, 2, 2])  # [4,2,0,0]
print merge([2, 0, 2, 4])  # [4,4,0,0]
print merge([0, 0, 2, 2])  # [4,0,0,0]
print merge([2, 4, 4, 2, 4, 0, 16, 4, 4, 0])