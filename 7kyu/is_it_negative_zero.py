from common import Test


def is_negative_zero(n):
    return str(n)[0] == '-' and n == 0

# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings


Test.assertEqual(is_negative_zero(-0.0), True)
Test.assertEqual(is_negative_zero(0.0), False)
Test.assertEqual(is_negative_zero(+0.0), False)

'''
There exist two zeroes: +0 (or just 0) and -0.

Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).

In JavaScript/TypeScript, the input will be a number. In Python and Java, the input will be a float.
'''