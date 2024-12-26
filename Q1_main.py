# submitter: kfir mutzary gridi
#ID:206397770
import turtle
import Q1_draw_board
import Q1_check_game_state
import Q1_sound_effects
import pygame
import Q1_messages
import Q1_input_handling


def main():
    # Set up the game screen and load background image
    screen = Q1_draw_board.setup_screen()
    screen.bgpic("BLEACH_TYBW_FCA_Blogsplash_1200x630.gif")

    # Choosing the game mode (player vs player or player vs computer)
    mode = Q1_input_handling.choosing_game_mode()

    # Create a turtle object to draw the game board
    board = turtle.Turtle()
    Q1_draw_board.draw_board(board)

    # Initialize pygame for sound effects and display the start message
    Q1_sound_effects.init_pygame()
    Q1_messages.show_start_message()
    Q1_sound_effects.play_background_music()

    # Initialize the game state as a 3x3 grid of None
    game_state = []
    for _ in range(3):
        row = [None, None, None]
        game_state.append(row)

    # Define player symbols and set the initial turn
    players = ['X', 'O']
    turn = 0
    game_over = False

    while not game_over:
        player = players[turn % 2]
        move_made = False

        while not move_made:
            if mode == 2 and player == 'O':
                # Handle computer's move for 'O' in 2-player mode
                x, y = Q1_input_handling.computer_move(game_state, board, player)
                game_state[x][y] = player
                move_made = True
            else:
                # Handle player input and validate the move
                x, y = Q1_input_handling.get_player_input(player)
                if game_state[x][y] is None:
                    game_state[x][y] = player
                    move_made = True
                else:
                    # Display message if the spot is already taken
                    Q1_messages.display_spot_taken_message()
            if move_made:
                # Redraw the board after a valid move
                Q1_draw_board.redraw_board(board, game_state)

        # Check the game state to determine the outcome (win/draw)
        result = Q1_check_game_state.check_state_game(game_state, board)
        if result and result != "Draw":
            # Display the winner and end the game
            Q1_messages.display_winner(result, board)
            game_over = True
        elif result == "Draw":
            # Display draw and end the game
            Q1_messages.display_draw(board)
            game_over = True

        # Increment turn count
        turn += 1
        # Check for draw by maximum turns without a winner
        if turn >= 9 and not result:
            Q1_messages.display_draw(board)
            game_over = True

    # Quit pygame and turtle modules
    pygame.quit()
    turtle.done()
    # Keep the screen open until manually closed
    screen.mainloop()


if __name__ == "__main__":
    main()
