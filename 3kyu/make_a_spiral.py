from common import Test


def spiral_fill_1(spiral, s, size):
    if s >= size:
        return
    if size < 2:
        spiral[s][0] = 1
        return

    spiral[s][s - 1] = 1

    for i in range(size - s):
        spiral[s][s + i] = 1
        spiral[s + i][size - 1] = 1
        if size - s > 2:
            spiral[size - 1][s + i] = 1
        if i != 1:
            spiral[s + i][s] = 1
    return spiral_fill_1(spiral, s + 2, size - 2)


def spiralize(size):
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    spiral_fill_1(spiral, 0, size)
    return spiral


Test.assert_equals(spiralize(1), [[1]])
Test.assert_equals(spiralize(2), [[1, 1],
                                  [0, 1]])
Test.assert_equals(spiralize(3), [[1, 1, 1],
                                  [0, 0, 1],
                                  [1, 1, 1]])
Test.assert_equals(spiralize(5), [[1, 1, 1, 1, 1],
                                  [0, 0, 0, 0, 1],
                                  [1, 1, 1, 0, 1],
                                  [1, 0, 0, 0, 1],
                                  [1, 1, 1, 1, 1]])
Test.assert_equals(spiralize(8), [[1, 1, 1, 1, 1, 1, 1, 1],
                                  [0, 0, 0, 0, 0, 0, 0, 1],
                                  [1, 1, 1, 1, 1, 1, 0, 1],
                                  [1, 0, 0, 0, 0, 1, 0, 1],
                                  [1, 0, 1, 0, 0, 1, 0, 1],
                                  [1, 0, 1, 1, 1, 1, 0, 1],
                                  [1, 0, 0, 0, 0, 0, 0, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1]])

# Test.assert_equals(spiralize(10), '')
#