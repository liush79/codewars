def encode(inp):
    final = prev = inp[0]
    cnt = 0
    for s in inp:
        if s == prev:
            cnt += 1
        else:
            final += '%d%s' % (cnt, s)
            cnt = 1
            prev = s
    final += '%d' % cnt
    return final


print encode('AAAABBBBBCD')
