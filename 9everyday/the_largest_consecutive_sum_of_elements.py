# -*- coding: utf-8 -*-
# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
# 정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오.단, 시간복잡도는 O(n).

# Given an integer array, find the largest consecutive sum of elements.

# 예제}
#
# Input: [-1, 3, -1, 5]
#
# Output: 7 // 3 + (-1) + 5
#
# Input: [-5, -3, -1]
#
# Output: -1 // -1
#
# Input: [2, 4, -2, -3, 8]
#
# Output: 9 // 2 + 4 + (-2) + (-3) + 8


def solution(inputs):
    current_sum = max_sum = inputs[0]
    for i, n in enumerate(inputs):
        if i == 0:
            continue
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    return max_sum


print solution([-1, 3, -1, 5])      # 7
print solution([-5, -3, -1])        # -1
print solution([2, 4, -2, -3, 8])   # 9
print solution([3, -1, -1, 3])      # 4
