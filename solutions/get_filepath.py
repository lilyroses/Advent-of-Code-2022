def get_filepath(n):
    """n = day_n"""
    ROOT_DIR = '/home/lilyroses/code/AoC/Advent-of-Code-2022/solutions/'
    CURRENT_DIR = f'day_{n}/'
    INPUT_FILE = 'input.txt'

    FILEPATH = f'{ROOT_DIR}{CURRENT_DIR}{INPUT_FILE}'
    return FILEPATH
