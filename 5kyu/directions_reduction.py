DIRECTION = {'EAST': 1, 'WEST': -1, 'SOUTH': 2, 'NORTH': -2}

def dirReduc(arr):
    for i, a in enumerate(arr):
        if i == len(arr) - 1:
            break
        if DIRECTION[arr[i]] + DIRECTION[arr[i + 1]] == 0:
            del arr[i]
            del arr[i]
            dirReduc(arr)
    return arr


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print dirReduc(a)   # ['WEST']
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print dirReduc(u)   # ["NORTH", "WEST", "SOUTH", "EAST"]