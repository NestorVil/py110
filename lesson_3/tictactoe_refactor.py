import os
import random
import time

INITIAL_MARKER = ' '
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"
WHO_MOVES_FIRST = [1, 2, 3]
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],   # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],   # columns
        [1, 5, 9], [3, 5, 7]               #diagnols
    ]

def prompt(message):
    print(f"==>{message}")

def first_move():
    prompt("Who should make the first move (1: for player, 2: for computer, 3: random)")
    while True:
        choice = input().strip()
        match choice:
            case "1":
                return WHO_MOVES_FIRST[0]
            case "2":
                return WHO_MOVES_FIRST[1]
            case "3":
                return random.choice(WHO_MOVES_FIRST[:2])
            case _:
                prompt("Please select 1 for player, 2 for computer, or 3 for random")

def display_board(board):
    os.system("clear")

    prompt("First to 3 wins gl")
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}")
    print()
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----|-----|-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----|-----|-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')
    print()

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}

def join_or(sequence, delimiter=", ", word="or"):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {word} {sequence[1]}"
    
    leading_items = delimiter.join(str(item) for item in sequence[0:-1])
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'


def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)] 
        prompt(f"Choose a square ({join_or(valid_choices)}): ")
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = None
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break
    
    if not square:
        if board[5] == INITIAL_MARKER:
            square = 5

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square

    return None

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER 
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return "Player"
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return "Computer"

    return None

def initialize_scores():
    return {"player_score": 0, "computer_score": 0}

def increment_scores(scores, board):
    if detect_winner(board) == "Player":
        scores["player_score"] += 1
    elif detect_winner(board) == "Computer":
        scores["computer_score"] += 1
    
    return "Tie"

def round_decided(board):
    if someone_won(board) or board_full(board):
        display_board(board)
        if detect_winner(board):
            prompt(f"{detect_winner(board)} won the round :D")
        else:
            prompt("It's a tie:/")
        
        prompt("Restarting round...")
        time.sleep(2)
    
        return True
    
def display_score(scores):
    prompt(f"Player's score is {scores["player_score"]}, Computer's score is {scores["computer_score"]}")

def play_again():
    prompt("Play again? (y or n)")
    while True:
        answer = input().strip()
        if answer not in ["y", "Y", "n", "N"]:
            prompt("Please enter 'y' or 'n'")
        else:
            return answer

def choose_square(board, current_player):
    if current_player == 1:
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def alternate_player(current_player):
    if current_player == 1:
        return 2
    elif current_player == 2:
        return 1

def play_round(board, scores, current_player):
    while True:
        display_board(board)
        display_score(scores)
        choose_square(board, current_player)
        current_player = alternate_player(current_player)
        if round_decided(board) or board_full(board):
            break

def play_tic_tac_toe():
    game_running = True
    scores = initialize_scores()

    while game_running:
        board = initialize_board()
        current_player = first_move()

        play_round(board, scores, current_player)
        increment_scores(scores, board)

        if scores["player_score"] == 3 or scores["computer_score"] == 3:
            os.system("clear")
            prompt(f"{detect_winner(board)} won the game :D")
            display_score(scores)
            scores = initialize_scores()

            if play_again() in ["n", "N"]:
                game_running = False
    
    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()