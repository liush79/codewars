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
#

inputs = [-5, -3, -1]
idx = inputs.index(max(inputs))

tmp_max = 0
sum_max = inputs[idx]
# left
for n in inputs[idx::-1]:
    tmp_max += n
    if tmp_max > sum_max:
        sum_max = tmp_max

# right
tmp_max = 0
for n in inputs[idx:]:
    tmp_max += n
    if tmp_max > sum_max:
        sum_max = tmp_max
print sum_max
