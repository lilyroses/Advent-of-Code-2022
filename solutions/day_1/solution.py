"""Solution 1 for Advent of Code 2022"""

# My input data for the day 1 challenge 
INPUT_FILE = 'input.txt'
 
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]


# PART I

def convert_calories_to_ints(items: list[str]):
    """Convert each non-blank line in lines from an integer type to a string
    type.
    """
    converted_items = []

    for item in items:
        # A blank line indicates the end of the current elf's food list
        if item != '':
            converted_item = int(item)
            converted_items.append(converted_item)
        else:
            # Add the blank line to the list, to indicate end of current elf's
            # food list later on
            converted_items.append(item)

    return converted_items


converted_lines = convert_calories_to_ints(lines)


def create_calorie_lists(converted_items: list[int]):
    # Create separate calorie lists from the converted lines.
    # Append each of these calorie lists to a parent list, all_calorie_lists.

    # Holds the current list of integer calorie values, using the converted_lines list.
    # The calorie values are appended to current_calorie_list until a blank line in converted_lines
    # is reached.

    current_calorie_list = []
    # Once a blank line in converted_lines is reached, the current calorie list ends, and is appended
    # to all_calorie_lists. current_calorie_list is then emptied, and the next list built.
    all_calorie_lists = []

    # converted_lines contains the proper data types (ints) for the calorie value lines.
    for converted_line in converted_lines:
        # If the line is a not blank line, we are still building the current calorie list.
        if line != '':
            # Add the current calorie value to the current list of calorie values.
            current_calorie_list.append(line)
        # If we reach a blank line, the current calorie list has ended.
        else:
            # Append the current calorie list to a list that contains all the calorie lists.
            all_calorie_lists.append(current_calorie_list)
            # Reset the current calorie list, so that we can build the next calorie list.
            current_calorie_list = []

    # Returns the list of lists of integer values.
    return all_calorie_lists