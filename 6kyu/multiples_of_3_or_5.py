def solution(ns):
    return sum(set(n for n in range(1, ns) if n % 3 == 0 or n % 5 == 0))


print solution(10)  # 23

