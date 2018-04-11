def solution(a):
    cnt = idx = 0
    len_a = len(a)
    if len_a == 0:
        return -1
    while True:
        cnt += 1
        idx += a[idx]
        if idx < 0 or idx >= len_a:
            return cnt
        if cnt > len(a):
            return -1


print solution([1, 2, 2, -1])
