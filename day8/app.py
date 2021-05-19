import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

input_array = [{'instruction': i[:3], 'direction': i[4], 'value': int(
    i[5:]), 'is_executed': False} for i in input.read().splitlines()]


def move(input):
    if input['direction'] == '+':
        direction = 1
    elif input['direction'] == '-':
        direction = -1
    return (input['value']*direction)


def iterate_instructions(input_array):
    cursor = 0
    accumulator = 0
    while True:
        if cursor == len(input_array)-1:
            print('Part 2:', accumulator)
            break
        elif input_array[cursor]['is_executed']:
            break
        elif input_array[cursor]['instruction'] == ACC:
            accumulator += move(input_array[cursor])
            input_array[cursor]['is_executed'] = True
            cursor += 1
            pass
        elif input_array[cursor]['instruction'] == JMP:
            input_array[cursor]['is_executed'] = True
            cursor += move(input_array[cursor])
            pass
        elif input_array[cursor]['instruction'] == NOP:
            input_array[cursor]['is_executed'] = True
            cursor += 1
            pass
    for i in input_array:
        if i['is_executed']:
            i['is_executed'] = False
    return accumulator


# Part 1
print('Part 1:', iterate_instructions(input_array))


# Part 2
new_input_array = list(input_array)

for index, i in enumerate(new_input_array):
    instruction = i['instruction']
    if instruction in [JMP, NOP]:
        if i['instruction'] == NOP:
            new_input_array[index]['instruction'] = JMP
        elif i['instruction'] == JMP:
            new_input_array[index]['instruction'] = NOP
        iterate_instructions(new_input_array)
        new_input_array[index]['instruction'] = instruction
