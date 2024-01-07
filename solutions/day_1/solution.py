"""Solution 1 for Advent of Code 2022"""

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [item.strip() for item in f.readlines()]


def find_max_calories(lines: list[str], sep: str = '') -> list[int]:
    """Find the list of foods with the maximum calories."""

    max_calories = 0
    current_food_list_calories = 0

    for line in lines:
        if line != sep:
            current_food_list_calories += int(line)
            # An empty string means the end of the list.
        else:
            if current_food_list_calories > max_calories:
                max_calories = current_food_list_calories
            current_food_list_calories = 0

    return max_calories

print(find_max_calories(data, ''))
