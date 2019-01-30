from common import Test


def calc_type(a, b, res):
    # we don't check division is true, because 'Only valid arguments will be passed to the function.'
    return 'addition' if a + b == res else 'subtraction' if a - b == res else 'multiplication' if a * b == res else 'division'


Test.assert_equals(calc_type(1, 2, 3), "addition")
Test.assert_equals(calc_type(10, 5, 5), "subtraction")
Test.assert_equals(calc_type(10, 4, 40), "multiplication")
Test.assert_equals(calc_type(9, 5, 1.8), "division")


'''
You have to create a function which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

Example:
calcType(1, 2, 3) -->   1 ? 2 = 3   --> "addition"

Notes
In case of division you should expect that the result of the operation is obtained by using / operator on the input values - no manual data type conversion or rounding should be performed.
Cases with just one possible answers are generated.
Only valid arguments will be passed to the function.
'''