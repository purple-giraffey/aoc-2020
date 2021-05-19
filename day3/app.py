import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = input.read().splitlines()


def path_navigator(right, down):
    trees_encountered = 0
    for i, row in enumerate(input_array):
        if(i % down != 0):
            continue
        row_len = len(row)
        transposer = int((i*right)/down) % row_len
        x = row[:transposer]
        row = row[transposer:] + x
        if row[0] == '#':
            trees_encountered += 1
    return trees_encountered


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

solution = 1

for s in slopes:
    solution *= path_navigator(s[0], s[1])

# Part 1
print(path_navigator(3, 1))

# Part 2
print(solution)
