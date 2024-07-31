import os
from string import ascii_letters

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(INPUT_FILE, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


# PART I
PRIORITY_VALUES = dict(zip(ascii_letters, list(range(1,53))))

item_priority_values = 0

for line in lines:
    num_items = len(line)
    compartment_1 = line[:num_items//2]
    compartment_2 = line[num_items//2:]
    shared_items = []

    for item in compartment_2:
        if item in compartment_1:
            if item not in shared_items:
                shared_items.append(item)
    
    for item in shared_items:
        item_priority_values += PRIORITY_VALUES[item]

print(item_priority_values)


# PART II
item_priority_values = 0

elf_groups = [lines[i * 3:(i + 1) * 3] for i in range((len(lines) + 3 - 1) // 3)]
for elf_group in elf_groups:
    shared_items = []
    for item in elf_group[0]:
        if item in elf_group[1] and item in elf_group[2]:
            if item not in shared_items:
                shared_items.append(item)
    for item in shared_items:
        item_priority_values += PRIORITY_VALUES[item]

print(item_priority_values)
