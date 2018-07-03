from common import Test


def abbrevName(name):
    return '.'.join([n[0].upper() for n in name.split(' ')])


# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings
Test.assert_equals(abbrevName("Sam Harris"), "S.H")
Test.assert_equals(abbrevName("Patrick Feenan"), "P.F")
Test.assert_equals(abbrevName("Evan Cole"), "E.C")
Test.assert_equals(abbrevName("P Favuzzi"), "P.F")
Test.assert_equals(abbrevName("David Mendieta"), "D.M")


'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
'''