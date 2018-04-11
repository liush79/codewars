def solve(s):
    res = ''
    reverse_s = []
    idx_space = []
    for i, c in enumerate(s):
        if c == ' ':
            idx_space.append(i)
        else:
            reverse_s.append(c)

    for i, c in enumerate(s):
        if i in idx_space:
            res += ' '
        else:
            res += reverse_s.pop()
    return res


print solve("codewars")         # "srawedoc"
print solve("your code")        # "edoc ruoy"
print solve("your code rocks")  # "skco redo cruoy"
print solve("i love codewars")  # "s rawe docevoli"
