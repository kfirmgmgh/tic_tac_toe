
import turtle
import Q1_messages
import Q1_check_game_state
import random
def get_player_input(player):
    # Collect row and column input from the player using graphical input pop-ups

        x = turtle.numinput("Player " + str(player), "Enter your row (0, 1, 2): ", minval=0, maxval=2)
        y = turtle.numinput("Player " + str(player), "Enter your column (0, 1, 2): ", minval=0, maxval=2)
    # Validate that the inputs are not None and are integers, then return them as integers
        if x is not None and y is not None and x.is_integer() and y.is_integer():
            return int(x), int(y)
        else:
            # Display an error message if the inputs are invalid
            Q1_messages.display_invalid_number_input_message()
def computer_move(game_state,board,player):
    # Assign 'O' as the computer's symbol
    computer='O'
    # Check if there is a winning move available for the computer
    win_move=check_if_can_win(game_state,board,computer)
    if win_move:
        return win_move
    # Check if there is a move that can block the opponent from winning
    block_move=find_blocking_move(game_state,player)
    if block_move:
        return block_move
    # List of moves with priority; center and corners have higher priority
    priority_moves = [[1, 1], [0, 0], [0, 2], [2, 0], [2, 2], [0, 1], [1, 0], [1, 2], [2, 1]]
    # Try to place 'O' in one of the priority moves if the spot is empty
    for x, y in priority_moves:
        if game_state[x][y] is None:
            return x, y
    return None

def check_if_can_win(game_state,board,player):
    n = 3 # Define the size of the game grid
    # Iterate through all possible moves
    for i in range(n):
        for j in range(n):
            # Test if placing 'player' in the empty spot wins the game
            if game_state[i][j] is None:
                game_state[i][j] = player
                if Q1_check_game_state.check_state_game(game_state,board) == player:
                    game_state[i][j] = None
                    return i, j
                game_state[i][j] = None
    return None
def find_blocking_move(game_state, player):
    n = 3 # Game grid size
    opponent = 'X' if player == 'O' else 'O' # Determine the opponent's symbol
    # Two-dimensional array to store potential blocking moves
    should_block_moves=[]
    # Check each row, column, and diagonal for a potential blocking move
    for i in range(n):
        if game_state[i][0] == opponent and game_state[i][1] == opponent and game_state[i][2] is None:
            should_block_moves.append([i,2])
        if game_state[i][0] == opponent and game_state[i][2] == opponent and game_state[i][1] is None:
           should_block_moves.append([i,1])
        if game_state[i][1] == opponent and game_state[i][2] == opponent and game_state[i][0] is None:
            should_block_moves.append([i,0])

    for j in range(n):
        if game_state[0][j] == opponent and game_state[1][j] == opponent and game_state[2][j] is None:
            should_block_moves.append([2,j])
        if game_state[0][j] == opponent and game_state[2][j] == opponent and game_state[1][j] is None:
            should_block_moves.append([1,j])
        if game_state[1][j] == opponent and game_state[2][j] == opponent and game_state[0][j] is None:
            should_block_moves.append([0,j])

    if game_state[0][0] == opponent and game_state[1][1] == opponent and game_state[2][2] is None:
            should_block_moves.append([2,2])
    if game_state[0][0] == opponent and game_state[2][2] == opponent and game_state[1][1] is None:
        should_block_moves.append([1, 1])
    if game_state[1][1] == opponent and game_state[2][2] == opponent and game_state[0][0] is None:
            should_block_moves.append([0,0])

    if game_state[0][2] == opponent and game_state[1][1] == opponent and game_state[2][0] is None:
            should_block_moves.append([2,0])
    if game_state[0][2] == opponent and game_state[2][0] == opponent and game_state[1][1] is None:
            should_block_moves.append([1,1])
    if game_state[1][1] == opponent and game_state[2][0] == opponent and game_state[0][2] is None:
            should_block_moves.append([0,2])
    # Randomly decide whether to block or not
    if should_block_moves and random.random()>0.40:
        return random.choice(should_block_moves)
    return None


def choosing_game_mode():
    # Request the user to choose the game mode with a numerical input pop-up
    mode = turtle.numinput("Please choose Game Mode", 'Enter 1 for Player VS Player,2 for Player VS Computer',minval=1,maxval=2)
    # Validate the input and default to mode 1 if the input is invalid
    if mode.is_integer() and mode == 2 and mode is not None:
        return int(mode)
    else:
        return 1
