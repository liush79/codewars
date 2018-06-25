# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

n = 1200

arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]


def move_array(arr, n):
    s = len(arr[0]) - 1
    new_arr = arr[0]
    for i in range(1, s):
        new_arr.append(arr[i][s])
    new_arr += arr[s][::-1]
    for i in range(1, s):
        new_arr.append(arr[s - i][0])

    for i in range(0, n):
        new_arr.insert(0, new_arr.pop())

    arr[0] = new_arr[0:s + 1]
    for i in range(1, s):
        arr[i][s] = new_arr[s + i]
    arr[s] = new_arr[s+s:-(s-1)][::-1]
    for i in range(1, s):
        arr[s - i][0] = new_arr[-(s - i)]

    return arr


print move_array(arr, n)
