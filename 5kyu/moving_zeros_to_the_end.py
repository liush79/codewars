def move_zeros(arr):
    return sorted(arr, key=lambda k: type(k) in (int, float) and int(k) == 0)


print (move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print (move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))
