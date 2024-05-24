"""Solution 1 for Advent of Code 2022"""
import sys
sys.path.append('..')
from solutions.get_filepath import get_filepath

FILEPATH = get_filepath(1)

with open(FILEPATH, 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]


# with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    # lines = [line.strip() for line in f.readlines()]


# PART I

def convert_calorie_strs_to_ints(lines: list[str]) -> list[int|str]:
    """Convert lines containing calorie strings to integers. Preserve
    all empty string placements within the list.
    """
    return [int(line) if line != '' else line for line in lines]


def create_calorie_lists(converted_lines: list[int]):
    current_calorie_list = []
    all_calorie_lists = []
    for line in converted_lines:
        if line != '':
            current_calorie_list.append(line)
        else:
            all_calorie_lists.append(current_calorie_list)
            current_calorie_list = []
    return all_calorie_lists


def find_calorie_list_totals(all_calorie_lists: list[int]):
    calorie_totals = []
    for calorie_list in all_calorie_lists:
        calorie_total = sum(calorie_list)
        calorie_totals.append(calorie_total)
    return calorie_totals


def find_max_calorie(calorie_totals: list[int]):
    return max(calorie_totals)


converted_lines = convert_calorie_strs_to_ints(lines)
all_calorie_lists = create_calorie_lists(converted_lines)
calorie_totals = find_calorie_list_totals(all_calorie_lists)
max_calorie = find_max_calorie(calorie_totals)

answer_part_one = max_calorie


# PART II

sorted_calorie_totals = sorted(calorie_totals, reverse=True)
top_three_calorie_totals = sorted_calorie_totals[0:3]
total = sum(top_three_calorie_totals)

answer_part_two = total


if __name__ == '__main__':
    print(f'Answer (Part I): {answer_part_one}')
    print(f'Answer (Part II): {answer_part_two}')
