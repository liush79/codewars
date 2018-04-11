def snail(array):
    if not array:
        return []
    if len(array) == 1:
        return array[0]
    result = []
    n = len(array[0])
    result += array[0]
    for i in range(1, n-1):
        result.append(array[i][-1])
        del array[i][-1]
    result += reversed(array[-1])
    for i in reversed(range(1, n-1)):
        result.append(array[i][0])
        del array[i][0]
    del array[0]
    del array[-1]
    result += snail(array)
    return result


print snail([[1,2,3],
             [8,9,4],
             [7,6,5]])