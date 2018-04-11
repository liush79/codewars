def accum(str_acc):
    result = ''
    for i, s in enumerate(str_acc):
        result += s.upper()
        for j in range(0, i):
            result += s.lower()
        result += '-'
    return result[:-1]


print accum("ZpglnRxqenU")  # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
print accum("NyffsGeyylB")  # "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"

