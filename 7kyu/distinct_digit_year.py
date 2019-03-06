from common import Test


def distinct_digit_year(year):
    return year + 1 if len(set(n for n in str(year + 1))) == 4 else distinct_digit_year(year + 1)


Test.it("Basic Tests")
Test.assert_equals(distinct_digit_year(1987),2013)
Test.assert_equals(distinct_digit_year(2013),2014)

'''
The year of 2013 is the first year after the old 1987 with only distinct digits.

Now your task is to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input/Output
[input] integer year

1000 <= year <= 9000

[output] an integer

the minimum year number that is strictly larger than the input number year and all it's digits are distinct.
'''