import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = input.read().splitlines()


def calculate_row(row_input):
    f_to_0 = row_input.replace('F', '0')
    b_to_1 = f_to_0.replace('B', '1')
    return int(b_to_1, 2)


def calculate_col(col_input):
    l_to_0 = col_input.replace('L', '0')
    r_to_1 = l_to_0.replace('R', '1')
    return int(r_to_1, 2)


highest_id = 0
all_seats = []

for bp in input_array:
    row = bp[:7]
    col = bp[7:]
    row_num = calculate_row(row)
    col_num = calculate_col(col)
    id = row_num * 8 + col_num
    if id > highest_id:
        highest_id = id
    all_seats.append(id)

# Part 1
print(highest_id)

# Part 2
all_seats_sorted = sorted(all_seats)
for i, s in enumerate(all_seats_sorted):
    if i < len(all_seats_sorted)-1:
        if all_seats_sorted[i+1] != s+1:
            print(s-1)
