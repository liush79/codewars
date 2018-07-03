from common import Test


def is_pangram(s):
    return len(set(c.lower() for c in s if c.isalpha())) is 26


pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)

'''
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence 
    "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
'''