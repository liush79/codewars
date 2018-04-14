d_dict = {"0": [0], "1": [1], "2": [2, 4, 8, 6], "3": [3, 9, 7, 1], '4': [4, 6], '5': [5], '6': [6], '7': [7, 9, 3, 1],'8': [8, 4, 2, 6], '9': [9, 1]}
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    str_n1 = str(n1)
    return d_dict[str_n1[-1]][n2 % len(d_dict[str_n1[-1]]) - 1]


print last_digit(1234, 123)
print last_digit(4, 2)  # , 6)
print last_digit(9, 7)  # , 9)
print last_digit(10, 10 ** 10)  # , 0)
print last_digit(2 ** 200, 2 ** 300)    # , 6)