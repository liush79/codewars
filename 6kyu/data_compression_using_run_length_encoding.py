def encode(string):
    result = ''
    prev = string[0]
    cnt = 0
    for s in string:
        if s == prev:
            cnt += 1
        else:
            result += '%d%s' % (cnt, prev)
            cnt = 1
            prev = s
    result += '%d%s' % (cnt, prev)
    return result


def decode(string):
    result = ''
    num = ''
    for n in string:
        if n.isdigit():
            num += n
        else:
            for _ in range(0, int(num)):
                result += n
            num = ''
    return result


enc_data = encode('AAAAAABBBBBCDDEEE')
print enc_data
print decode(enc_data)