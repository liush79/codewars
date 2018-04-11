num_not = '23457'
num_ok = '01689'
num_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

def solve(a, b):
    result = 0
    for num in range(a, b):
        for n in str(num):
            if n in num_not:
                break
        else:
            rev_num = ''
            for n in str(num)[::-1]:
                rev_num += num_dict[n]
            if num == int(rev_num):
                result += 1
    return result


print solve(0, 10)          # 3
print solve(10, 100)        # 4
print solve(100, 1000)      # 12
print solve(1000, 10000)    # 20
print solve(10000, 15000)   # 6
print solve(15000, 20000)   # 9
print solve(60000, 70000)   # 15
print solve(60000, 130000)  # 55

