import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = [int(input_item) for input_item in input.read().splitlines()]
input_array.sort()

# Part 1
for i, a in enumerate(input_array):
    for b in input_array[i+1:]:
        if(a + b == 2020):
            print(a * b)
        elif (a + b > 2020):
            break

# Part 2
for i, a in enumerate(input_array):
    for j, b in enumerate(input_array[i+1:]):
        for c in input_array[j+1:]:
            if(a + b + c == 2020):
                print(a * b * c)
            elif (a + b + c > 2020):
                break
