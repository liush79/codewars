def check_pattern(pattern, sequence):
    len_pattern = len(pattern)
    if (len(sequence) - 1) % len(pattern) != 0:
        return False
    for i, s in enumerate(sequence):
        if i == 0:
            continue
        idx = (i % len_pattern) - 1
        if pattern[idx] != sequence[i] - sequence[i - 1]:
            break
    else:
        if (len(sequence) - 1) % len_pattern != 0:
            return False
        return True
    return False


def find_pattern(sequence):
    pattern = []
    for i, s in enumerate(sequence):
        if i == 0:
            continue
        pattern.append(sequence[i] - sequence[i - 1])
        if check_pattern(pattern, sequence):
            return pattern


print find_pattern([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1])     # [1, 1, 1, 1, -1, -1, -1, -1]
print find_pattern([1, 5, 2, 3, 1, 5, 2, 3, 1])     # [4, -3, 1, -2]

