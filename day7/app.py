import os
import sys

input = open(os.path.join(sys.path[0], "input.txt"), "r")

input_array = input.read().splitlines()

all_rules = {}
SHINY_GOLD = 'shiny gold'

for rule in input_array:
    rule = rule.split(' contain')
    current_bag = rule[0].replace('bags', '').strip(' ')
    bag_rules = rule[1].split(',')
    parsed_bag_rules = {}
    for bag_rule in bag_rules:
        bag_rule = bag_rule.replace('.', '').replace(
            'bags', '').replace('bag', '').strip(' ')
        if bag_rule == 'no other':
            pass
        else:
            parsed_bag_rules[bag_rule[2:]] = int(bag_rule[0])
    all_rules[current_bag] = parsed_bag_rules

# Part 1
all_parents = []


def find_parents_recursively(parents):
    newParents = []
    for br in all_rules.keys():
        for parent in list(parents):
            if parent in all_rules[br]:
                newParents.append(br)
    if newParents == []:
        all_parents.append(list(newParents))
        return
    all_parents.append(list(parents))
    return find_parents_recursively(set(newParents))


find_parents_recursively([SHINY_GOLD])
all_bag_colors_containing_shiny_gold = set(
    [item for sublist in all_parents for item in sublist])
# shiny gold is excluded from count
print(len(all_bag_colors_containing_shiny_gold)-1)


# Part 2
def count_children_bags(parent_color):
    color_children = all_rules[parent_color]
    if color_children == {}:
        return 0
    else:
        sum_bags = 0
        for color_child in color_children.keys():
            sum_bags += color_children[color_child] * \
                (1 + count_children_bags(color_child))
        return sum_bags


print(count_children_bags(SHINY_GOLD))
