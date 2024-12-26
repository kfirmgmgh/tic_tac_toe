# submitter: kfir mutzary gridi
#ID:206397770
import Q1_draw_shapes

def check_state_game(game_state, board):
    n = 3  # Set the size of the Tic Tac Toe grid

    # Check each row for a win
    for i in range(n):
        # Check if all cells in a row are the same and not empty
        if game_state[i][0] is not None and game_state[i][0] == game_state[i][1] == game_state[i][2]:
            # Highlight the winning row
            Q1_draw_shapes.highlight_winner(board, (-300, 200 - i * 200), (300, 200 - i * 200))
            return game_state[i][0]  # Return the winner ('X' or 'O')

    # Check each column for a win
    for j in range(n):
        # Check if all cells in a column are the same and not empty
        if game_state[0][j] is not None and game_state[0][j] == game_state[1][j] == game_state[2][j]:
            # Highlight the winning column
            Q1_draw_shapes.highlight_winner(board, (-200 + j * 200, 300), (-200 + j * 200, -300))
            return game_state[0][j]  # Return the winner ('X' or 'O')

    # Check diagonal (top-left to bottom-right) for a win
    if game_state[0][0] is not None and game_state[0][0] == game_state[1][1] == game_state[2][2]:
        # Highlight the winning diagonal
        Q1_draw_shapes.highlight_winner(board, (-300, 300), (300, -300))
        return game_state[0][0]  # Return the winner ('X' or 'O')

    # Check diagonal (top-right to bottom-left) for a win
    if game_state[0][2] is not None and game_state[0][2] == game_state[1][1] == game_state[2][0]:
        # Highlight the winning diagonal
        Q1_draw_shapes.highlight_winner(board, (300, 300), (-300, -300))
        return game_state[0][2]  # Return the winner ('X' or 'O')

    # Check for any empty cells left, if found return None to continue the game
    for i in range(n):
        for j in range(n):
            if game_state[i][j] is None:
                return None

    # If no empty cells and no winner, declare a draw
    return "Draw"
