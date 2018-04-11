def solve(st, idx):
    if st[idx] != '(':
        return -1
    res = -1
    open_cnt = 0
    for i in range(idx, len(st)):
        if st[i] == '(':
            open_cnt += 1
        elif st[i] == ')':
            open_cnt -= 1
            if open_cnt == 0:
                return i
    return res


print solve("((1)23(45))(aB)", 0)       # 10
print solve("((1)23(45))(aB)", 1)       # 3
print solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))", 0)        # 29
print solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))", 19)      # 22
