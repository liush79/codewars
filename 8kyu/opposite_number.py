from common import Test as test


def opposite(number):
    return -number


test.assert_equals(opposite(1), -1)


'''
Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
'''