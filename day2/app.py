import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = [input_item for input_item in input.read().splitlines()]

entries = []


def validate_entry_by_count(organized_entry):
    count = 0
    for letter in organized_entry["password"]:
        if(letter == organized_entry["letter"]):
            count += 1
    if(organized_entry["min"] <= count <= organized_entry["max"]):
        return 1
    return 0


def validate_entry_by_position(organized_entry):
    letter1_index = organized_entry["min"]
    letter2_index = organized_entry["max"]
    letter1 = ''
    letter2 = ''
    if(len(organized_entry["password"]) >= letter1_index):
        letter1 = organized_entry["password"][letter1_index]
    if(len(organized_entry["password"]) >= letter2_index):
        letter2 = organized_entry["password"][letter2_index]
    if(letter1 == letter2):
        return 0
    if(letter1 == organized_entry["letter"] or letter2 == organized_entry["letter"]):
        return 1
    return 0


validated_entries_count = 0
for entry in input_array:
    policy_password = entry.split(':')
    minmax_letter = policy_password[0].split(' ')
    min_max = minmax_letter[0].split('-')

    organized_entry = {'min': int(min_max[0]), 'max': int(min_max[1]),
                       'letter': minmax_letter[1], 'password': policy_password[1]}

    # Part 1
    # validated_entries_count += validate_entry_by_count(organized_entry)

    # Part 2
    validated_entries_count += validate_entry_by_position(organized_entry)

print(validated_entries_count)
