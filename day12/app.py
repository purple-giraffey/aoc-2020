import os
import sys
from copy import deepcopy

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = [i for i in input.read().splitlines()]

nav_instructions = []

START_STATE = {'dir': 'E', 'pos': {'N': 0, 'E': 0}}

for i in input_array:
    moving_dir = i[0]
    rotate = None
    value = None
    if i[0] in ['N', 'S', 'E', 'W', 'F']:
        moving_dir = i[0]
    elif i[0] in ['L', 'R']:
        rotate = i[0]
    nav_instructions.append(
        {'move': moving_dir, 'rotate': rotate, 'value': int(i[1:])})

ordered_directions = ['N', 'E', 'S', 'W']


def rotate_ship(instruction, point):
    rotate_dir = 1
    if instruction['rotate'] == 'L':
        rotate_dir = -1
    new_dir_offset = int(instruction['value']/90) * rotate_dir
    new_dir = ordered_directions[(ordered_directions.index(
        point['dir']) + new_dir_offset) % 4]
    return {'dir': new_dir, 'pos': point['pos']}


def move_ship(instruction, state):
    new_state = state
    direction = 1
    move = instruction['move']
    if move == 'F':
        move = state['dir']
    if move in ['S', 'W']:
        direction = -1
        if move == 'S':
            move = 'N'
        else:
            move = 'E'
    new_state['pos'][move] += instruction['value'] * direction
    return new_state


def follow_nav_instructions(nav_instructions, start_state):
    current_state = deepcopy(start_state)
    for i in nav_instructions:
        if i['rotate']:
            current_state = rotate_ship(i, current_state)
        elif i['move']:
            current_state = move_ship(i, current_state)
    return current_state


final_destination = follow_nav_instructions(nav_instructions, START_STATE)


print('Part 1:', abs(final_destination['pos']
                     ['N'])+abs(final_destination['pos']['E']))


START_WAYPOINT = {'dir': None, 'pos': {'N': 1, 'E': 10}}


def move_waypoint(instruction, waypoint):
    new_point = waypoint
    direction = 1
    move = instruction['move']
    if move in ['S', 'W']:
        direction = -1
        if move == 'S':
            move = 'N'
        else:
            move = 'E'
    new_point['pos'][move] += instruction['value'] * direction
    return new_point


def rotate_waypoint(instruction, waypoint):
    new_waypoint = waypoint
    new_waypoint_pos = {}
    rotate_dir = 1
    if instruction['rotate'] == 'L':
        rotate_dir = -1
    new_dir_offset = int(instruction['value']/90) * rotate_dir
    for direction in waypoint['pos'].keys():
        dir_sign = 1
        new_dir = ordered_directions[(ordered_directions.index(
            direction) + new_dir_offset) % 4]
        if new_dir == 'S':
            new_dir = 'N'
            dir_sign = -1
        elif new_dir == 'W':
            new_dir = 'E'
            dir_sign = -1
        new_waypoint_pos[new_dir] = waypoint['pos'][direction] * dir_sign
    new_waypoint['pos'] = new_waypoint_pos
    return new_waypoint


def move_ship_forward(instruction_value, waypoint, state):
    new_state = state
    new_state['pos']['N'] += waypoint['pos']['N'] * instruction_value
    new_state['pos']['E'] += waypoint['pos']['E'] * instruction_value
    return new_state


def follow_nav_instructions_actual(nav_instructions, start_state, start_waypoint):
    current_state = deepcopy(start_state)
    current_waypoint = deepcopy(start_waypoint)
    for i in nav_instructions:
        if i['rotate']:
            current_waypoint = rotate_waypoint(
                i, current_waypoint)
        elif i['move']:
            if i['move'] == 'F':
                current_state = move_ship_forward(
                    i['value'], current_waypoint, current_state)
            else:
                current_waypoint = move_waypoint(i, current_waypoint)
    return current_state


final_destination_final_final_1 = follow_nav_instructions_actual(
    nav_instructions, START_STATE, START_WAYPOINT)

print('Part 2:', abs(final_destination_final_final_1['pos']
                     ['N'])+abs(final_destination_final_final_1['pos']['E']))
