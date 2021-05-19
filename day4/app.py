import os
import sys
from field_validator import required_fields, field_validator

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = input.read().splitlines()
input_array.append('')  # splitlines doesn't read the last newline

current_entry = {}
organized_entries = []

for line in input_array:
    if line == '':
        organized_entries.append(current_entry)
        current_entry = {}
    else:
        fields_raw = line.split(' ')
        for f in fields_raw:
            current_entry[f.split(':')[0]] = f.split(':')[1]

valid_passports_basic = 0
valid_passports_advanced = 0


def validate_all_fields(entry):
    for field in entry.keys():
        if not field_validator(field, entry[field]):
            print(field, entry[field], field_validator(field, entry[field]))
            return False
    return True


for entry in organized_entries:
    if all(rf in entry for rf in required_fields):
        valid_passports_basic += 1
        if validate_all_fields(entry):
            valid_passports_advanced += 1


# Part 1
print(valid_passports_basic)

# Part 2
print(valid_passports_advanced)
