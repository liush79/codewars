roman = {
    1: {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'},
    10: {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'},
    100: {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'},
    1000: {1: 'M', 2: 'MM', 3: 'MMM'}
}


def solution(n, base=10000):
    if base == 0:
        return ''
    res = roman[base][int(n / base)] if n / base > 0 else ''
    return res + solution(n % base, base / 10)


print solution(1)   # ,'I', 'solution(1),'I'')
print solution(4)   # ,'IV', 'solution(4),'IV'')
print solution(6)   # ,'VI', 'solution(6),'VI'')
print solution(1990)    # MCMXC
print solution(2008)    # MMVIII
print solution(1666)    # MDCLXVI

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
