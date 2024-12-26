
import turtle
import Q1_draw_shapes

def setup_screen():
    # Initialize the game screen and set its title and dimensions
    screen = turtle.Screen()
    screen.title("Bleach Tic Tac Toe Game")
    screen.setup(width=600, height=600)
    return screen

def draw_board(board):
    # Prepare the board for drawing without showing the turtle
    board.hideturtle()
    board = turtle.Turtle()  # Create a new turtle object for drawing the board
    board.pensize(10)  # Set the thickness of the lines
    board.speed('fastest')  # Set the drawing speed to the fastest
    board.color('white')  # Set the line color to white
    board.penup()  # Lift the pen to move without drawing
    # Draw horizontal lines of the board
    for i in range(2):
        board.hideturtle()  # Hide the turtle while moving to start position
        board.goto(-300, 100 - 200 * i)  # Move to the starting position for each line
        board.pendown()  # Start drawing
        board.forward(600)  # Draw a horizontal line
        board.penup()  # Lift the pen after drawing the line
    # Rotate the turtle to draw vertical lines
    board.right(90)  # Rotate the turtle to face vertically
    # Draw vertical lines of the board
    for i in range(2):
        board.hideturtle()  # Hide the turtle while moving to start position
        board.goto(-100 + 200 * i, 300)  # Move to the starting position for each line
        board.pendown()  # Start drawing
        board.forward(600)  # Draw a vertical line
        board.penup()  # Lift the pen after drawing the line
    board.right(-90)  # Reset turtle orientation to default
    board.hideturtle()  # Hide the turtle after finishing drawing

def redraw_board(board, game_state):
    # Redraw the entire board based on the current game state
    board.hideturtle()  # Ensure the turtle is hidden before redrawing
    draw_board(board)  # Redraw the empty board
    # Update the board based on the game state with 'X' or 'O'
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == 'X':
                Q1_draw_shapes.draw_x(i, j, board)  # Draw 'X' at the specified position
                board.hideturtle()  # Hide the turtle after drawing
            elif game_state[i][j] == 'O':
                Q1_draw_shapes.draw_circle(i, j, board)  # Draw 'O' at the specified position
                board.hideturtle()  # Hide the turtle after drawing
