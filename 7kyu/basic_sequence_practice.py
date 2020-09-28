from common import Test as test


def sum_of_n(n):
    res = []
    sum = 0
    for i in range(abs(n) + 1):
        if n > 0:
            sum += i
        else:
            sum -= i
        res.append(sum)
    return res


test.assert_equals(sum_of_n(3), [0, 1, 3, 6])
test.assert_equals(sum_of_n(1), [0, 1])
test.assert_equals(sum_of_n(0), [0])
test.assert_equals(sum_of_n(-4), [0, -1, -3, -6, -10])


'''
A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".

In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".

[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3

Your Task

Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.

Examples

 5  -->  [0,  1,  3,  6,  10,  15]
-5  -->  [0, -1, -3, -6, -10, -15]
 7  -->  [0,  1,  3,  6,  10,  15,  21,  28]
'''