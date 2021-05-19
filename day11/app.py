import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = [list(i) for i in input.read().splitlines()]

# test = open(os.path.join(sys.path[0], "test_layout.txt"), "r")
# test_layout = [list(i) for i in test.read().splitlines()]


def occupied_adjacent_seats(layout, i, y):
    valid = []
    all_indexes = [(i-1, y-1), (i-1, y), (i-1, y+1), (i, y-1),
                   (i, y+1), (i+1, y-1), (i+1, y), (i+1, y+1)]

    for pair in all_indexes:
        if(pair[0] >= 0 and pair[0] < len(layout) and pair[1] >= 0 and pair[1] < len(layout[0])):
            valid.append(layout[pair[0]][pair[1]])

    return valid.count('#')


def occupied_visible_seats(layout, i, y):
    adjacent_seats = []

    # up
    cursor = [i-1, y]
    while cursor[0] >= 0:
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor[0] = cursor[0]-1

    # down
    cursor = [i+1, y]
    while cursor[0] < len(layout):
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor[0] = cursor[0]+1

    # left
    cursor = [i, y-1]
    while cursor[1] >= 0:
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor[1] = cursor[1]-1

    # right
    cursor = [i, y+1]
    while cursor[1] < len(layout[0]):
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor[1] = cursor[1]+1

    # down-right
    cursor = [i+1, y+1]
    while cursor[0] < len(layout) and cursor[1] < len(layout[0]):
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor = [cursor[0]+1, cursor[1]+1]

    # up-right
    cursor = [i-1, y+1]
    while cursor[0] >= 0 and cursor[1] < len(layout[0]):
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor = [cursor[0]-1, cursor[1]+1]

    # down-left
    cursor = [i+1, y-1]
    while cursor[0] < len(layout) and cursor[1] >= 0:
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor = [cursor[0]+1, cursor[1]-1]

    # up-left
    cursor = [i-1, y-1]
    while cursor[0] >= 0 and cursor[1] >= 0:
        seat = layout[cursor[0]][cursor[1]]
        if seat != '.':
            adjacent_seats.append(seat)
            break
        cursor = [cursor[0]-1, cursor[1]-1]

    return adjacent_seats.count('#')


def apply_round_changes(layout, occupied_seats_counter, max_occ_seats):
    new_layout = []
    for i, row in enumerate(layout):
        new_layout.append(list(layout[i]))
        for y, seat in enumerate(row):
            if seat == '#' and occupied_seats_counter(layout, i, y) > max_occ_seats:
                new_layout[i][y] = 'L'
            elif seat == 'L' and occupied_seats_counter(layout, i, y) < 1:
                new_layout[i][y] = '#'
    return new_layout


def iterate_layouts(layout, round_changer, validator, max_occ_seats):
    state = list(layout)
    new_state = round_changer(state, validator, max_occ_seats)
    while new_state != state:
        state = list(new_state)
        new_state = round_changer(state, validator, max_occ_seats)
    return state


def count_occupied_seats(layout):
    counter = 0
    for row in layout:
        counter += row.count('#')
    return counter


print('Part 1:', count_occupied_seats(
    iterate_layouts(input_array, apply_round_changes, occupied_adjacent_seats, 3)))

print('Part 2:', count_occupied_seats(
    iterate_layouts(input_array, apply_round_changes, occupied_visible_seats, 4)))
