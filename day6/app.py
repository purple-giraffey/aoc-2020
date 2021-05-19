import os
import sys
from functools import reduce

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = input.read().splitlines()
input_array.append('')  # splitlines doesn't read the last newline

# Part 1
current_group_answers = []
all_groups_answers = []

unique_answers_total = 0

for line in input_array:
    if line == '':
        all_groups_answers.append(set(current_group_answers))
        current_group_answers = []
    else:
        for answer in line:
            current_group_answers.append(answer)

for s in all_groups_answers:
    unique_answers_total += len(s)

print(unique_answers_total)

# Part 2
this_group_answers = []
all_answers = []

for member_answer in input_array:
    if member_answer == '':
        all_answers.append(reduce(lambda a, b: set(a) &
                                  set(b), this_group_answers))
        this_group_answers = []
    else:
        this_group_answers.append(set(member_answer))

shared_answers_total = 0

for group_answer in all_answers:
    shared_answers_total += len(group_answer)

print(shared_answers_total)
