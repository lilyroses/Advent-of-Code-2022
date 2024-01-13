"""Solution 2 for Advent of Code 2022"""

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = [item.strip() for item in f.readlines()]

LOSE = 0
TIE = 3
WIN = 6

MOVE_CODES = {
    'A': 'rock',
    'X': 'rock',
    'B': 'paper',
    'Y': 'paper',
    'C': 'scissors',
    'Z': 'scissors',
}

MOVE_POINTS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

def parse_codes(codes):
    """Parse input data and return move codes."""
    game_info = []
    for code in codes:
        info = (code[0], code[2])
        game_info.append(info)
    return game_info


game_rounds = parse_codes(codes=data)

total_score = 0

for game_round in game_rounds:
    round_score = 0

    opponent_move = MOVE_CODES[game_round[0]]
    my_move = MOVE_CODES[game_round[1]]

    round_score += MOVE_POINTS[my_move]

    # If the outcome is a tie
    if opponent_move == my_move:
        round_score += TIE

    # If the outcome is not a tie:
    else:

        # If my move is rock
        if my_move == 'rock':
            # If the opponent's move is paper, I lose
            if opponent_move == 'paper':
                round_score += LOSE
            # If the opponent's move is scissors, I win
            elif opponent_move == 'scissors':
                round_score += WIN

        # If my move is paper
        elif my_move == 'paper':
            # If the opponent's move is scissors, I lose
            if opponent_move == 'scisscors': 
                round_score += LOSE
            # If the opponent's move is rock, I win
            elif opponent_move == 'rock':
                round_score += WIN

        # If my move is scissors
        elif my_move == 'scissors':
            # If the opponent's move is rock, I lose
            if opponent_move == 'rock':
                round_score += LOSE
            # If the opponent's move is paper, I win
            elif opponent_move == 'paper':
                round_score += WIN

    total_score += round_score
print(total_score)
