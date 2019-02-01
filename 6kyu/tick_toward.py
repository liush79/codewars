from common import Test


def tick_toward(start, target):
    result = [start]
    while True:
        x = start[0] + 1 if start[0] < target[0] else start[0] if start[0] == target[0] else start[0] - 1
        y = start[1] + 1 if start[1] < target[1] else start[1] if start[1] == target[1] else start[1] - 1
        if start[0] == x and start[1] == y:
            break
        result.append((x, y))
        start = (x, y)
    return result


Test.assert_equals(tick_toward((5, 5), (5, 7)), [(5, 5), (5, 6), (5, 7)])
Test.assert_equals(tick_toward((3, 2), (4, 5)), [(3, 2), (4, 3), (4, 4), (4, 5)])
Test.assert_equals(tick_toward((5, 1), (5, -2)), [(5, 1), (5, 0), (5, -1), (5, -2)])


'''
Define a function that generates medial values between two coordinates and returns them in an array from start to target. For example, if the starting point is [1,1] and the target point is [3,2] then the shortest route from start to target would be [[1,1], [2,2], [3,2]]. The route should go only through integral coordinates.

Note: you should move diagonally until the path from your current position to the target can be represented as a fully horizontal/vertical line.

'''