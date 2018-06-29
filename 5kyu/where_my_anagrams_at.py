from common import Test


def anagrams(word, words):
    sort_word = sorted(word)
    return [w for w in words if sorted(w) == sort_word]



Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])