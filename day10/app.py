import os
import sys
from functools import reduce

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = [int(i) for i in input.read().splitlines()]

full_array = [0] + sorted(input_array) + [sorted(input_array)[-1]+3]

one_jolt_diff_count = 0
three_jolt_diff_count = 0

for index, i in enumerate(full_array):
    if index+1 == len(full_array):
        continue
    jolt_diff = full_array[index+1] - i
    if jolt_diff == 1:
        one_jolt_diff_count += 1
    elif jolt_diff == 3:
        three_jolt_diff_count += 1

print(one_jolt_diff_count * three_jolt_diff_count)
