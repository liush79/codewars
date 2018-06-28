from common import Test as test


# def sum_pairs(ints, s):
#     d = {}
#     for i, n in enumerate(ints):
#         if s - n in ints[i + 1:]:
#             idx = ints[i + 1:].index(s - n)
#             d[i + i + idx] = [ints[i], ints[i + 1 + idx]]
#     return d

def sum_pairs(ints, s):
    tmp = set()
    for n in ints:
        if s - n in tmp:
            return [s - n, n]
        tmp.add(n)
    return None


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

test.describe("Testing For Sum of Pairs")
test.expect(sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
test.expect(sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
test.expect(sum_pairs(l3, -7) is None, "No Match: %s should return None for sum = -7" % l3)
test.expect(sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
