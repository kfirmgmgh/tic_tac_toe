# submitter: kfir mutzary gridi
#ID:206397770
# Function to draw a circle at a specified position on the board
def draw_circle(x, y, board, radius=55):
    board.hideturtle()  # Hide the turtle cursor for aesthetic purposes
    # Calculate the center coordinates for the circle based on grid position
    circle_x = y * 200 - 220
    circle_y = 150 - x * 200
    board.color("orange")  # Set the color of the turtle to orange
    board.pensize(10)  # Set the line thickness to 10
    board.speed('fastest')  # Set the drawing speed to the fastest
    board.penup()  # Lift the pen up to move to the start position without drawing
    board.goto(circle_x, circle_y)  # Move to the calculated start position
    board.pendown()  # Put the pen down to start drawing
    board.circle(radius)  # Draw the circle with the specified radius
    board.penup()  # Lift the pen up after drawing is complete
    board.hideturtle()  # Hide the turtle cursor again

# Function to draw an 'X' at a specified position on the board
def draw_x(x, y, board, size_x=100):
    board.hideturtle()  # Hide the turtle cursor for aesthetic purposes
    # Calculate the center of the 'X' based on grid position
    center_x = y * 200 - 200
    center_y = 200 - x * 200
    half_size = size_x / 2  # Calculate half the size of the 'X' to get endpoints
    board.color("dark blue")  # Set the color of the turtle to dark blue
    board.pensize(10)  # Set the line thickness to 10
    board.speed('fastest')  # Set the drawing speed to the fastest
    board.penup()  # Lift the pen up to move to the start position without drawing
    # Draw the first diagonal of 'X'
    board.goto(center_x - half_size, center_y - half_size)
    board.pendown()
    board.goto(center_x + half_size, center_y + half_size)
    board.penup()
    # Draw the second diagonal of 'X'
    board.goto(center_x - half_size, center_y + half_size)
    board.pendown()
    board.goto(center_x + half_size, center_y - half_size)
    board.penup()  # Lift the pen up after drawing is complete
    board.hideturtle()  # Hide the turtle cursor again

# Function to highlight the winning sequence on the board
def highlight_winner(board, start_pos, end_pos):
    board.pensize(10)  # Set the line thickness to 10 for visibility
    board.speed("fastest")  # Set the speed to slowest to highlight the drawing process
    board.pencolor("red")  # Set the color to red to distinguish the winning sequence
    board.penup()
    board.goto(start_pos)  # Move to the starting position of the winning sequence
    board.pendown()
    board.goto(end_pos)  # Draw a line to the end position of the winning sequence
    board.penup()  # Lift the pen up after drawing is complete
