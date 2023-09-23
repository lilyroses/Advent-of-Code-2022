"""
Generator script for creating directory and files for the Advent of
Code 2022 challenge.
"""

import os
import nbformat



# CHANGE THESE VARIABLES
n = 0

title = ''


# Path to location of Advent of Code files
PROJECT_FOLDER = '/home/lilyroses/code/Advent-of-Code-2022/'
# Default folder/file names
SOLUTION_FILENAME = 'solution.ipynb'
INSTRUCTIONS_FILENAME = 'instructions.md'
INPUT_FILENAME = 'input.txt'

ERRORS = [FileNotFoundError, FileExistsError]

# GENERATE DIRECTORY 
def create_dir(num):
    """Create a directory with the naming format day_n"""
    dir = f'day_{num}/'
    full_path = PROJECT_FOLDER + dir
    
    try:
        os.mkdir(full_path)
    except FileExistsError as e:
        print(f'e')
    except FileNotFoundError:
        print(f'Error: Path `{full_path}` not found')


create_dir(n)