from common import Test


def get_middle(s):
    idx_mid = int(len(s) / 2)
    return s[idx_mid] if len(s) % 2 != 0 else s[idx_mid - 1:idx_mid + 1]


Test.assert_equals(get_middle("test"), "es")
Test.assert_equals(get_middle("testing"), "t")
Test.assert_equals(get_middle("middle"), "dd")
Test.assert_equals(get_middle("A"), "A")
Test.assert_equals(get_middle("of"), "of")

'''
You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
'''

# BEST
# def get_middle(s):
#    return s[(len(s)-1)/2:len(s)/2+1]
