required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]
optional_field = 'cid'


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def field_validator(field, input):
    if field == optional_field:
        return True
    elif field in required_fields:
        if field in ['byr', 'iyr', 'eyr']:
            year_bounds = {
                'byr': (1920, 2002),
                'iyr': (2010, 2020),
                'eyr': (2020, 2030)
            }
            if input.isnumeric() and len(input) == 4 and year_bounds[field][0] <= int(input) <= year_bounds[field][1]:
                return True
        elif field == 'hgt':
            metric_sys = input[-2:]
            height = input[:-2]
            if not height.isnumeric():
                return False
            if metric_sys == 'cm':
                return 150 <= int(height) <= 193
            elif metric_sys == 'in':
                return 59 <= int(height) <= 76
        elif field == 'hcl':
            if len(input) == 7 and input[0] == '#':
                return is_hex(input[1:])
        elif field == 'ecl':
            return input in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif field == 'pid':
            return len(input) == 9 and input.isnumeric()
        return False
    else:
        return False
