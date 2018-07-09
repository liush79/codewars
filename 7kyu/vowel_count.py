from common import Test as test


def getCount(inputStr):
    return len([s for s in inputStr if s in 'aeiou'])


test.assert_equals(getCount("abracadabra"), 5)
