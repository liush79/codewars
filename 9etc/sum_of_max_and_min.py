def sum_of_max(inputs):
    maxs = sorted(inputs, cmp=lambda x, y: cmp(x + y, y + x))
    mins = list(maxs)
    maxs.reverse()
    return int(''.join(maxs)) + int(''.join(mins))


print sum_of_max(['1', '2', '3']), ', 444'
print sum_of_max(['2', '9', '10', '21', '24']), ', 102634359'
