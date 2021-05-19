import os
import sys
from functools import reduce

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = [int(i) for i in input.read().splitlines()]

buffer = input_array[:25]


def check_buffer_sums(num: int, array: list):
    for i, n in enumerate(array):
        for m in array[i+1:]:
            if m + n == num:
                return True
    return False


def check_contiguous_sums(num: int, array: list):
    sum_array = [0]

    def sum_total():
        return reduce(lambda a, b: a+b, sum_array)

    for n in array:
        while sum_total() >= num:
            sum_array.pop(0)
            if sum_total() == num:
                return sum_array
        sum_array.append(n)
        if sum_total() == num:
            return sum_array
        elif sum_total() < num:
            continue


for i in input_array[25:]:
    if check_buffer_sums(i, buffer) == False:
        print('Part 1:', i)
        contiguous_sums = check_contiguous_sums(
            i, input_array[:input_array.index(i)])
        contiguous_sums = sorted(contiguous_sums)
        print('Part 2:', contiguous_sums[0] + contiguous_sums[-1])
        break
    else:
        buffer.pop(0)
        buffer.append(i)
