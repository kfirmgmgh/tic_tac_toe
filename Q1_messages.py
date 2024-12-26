import turtle
import time
import Q1_sound_effects
import tkinter
from tkinter import messagebox

def show_start_message():
    # Set up turtle graphics for displaying the start message
    board = turtle.Turtle()
    board.hideturtle()  # Hide the turtle pointer for clean display
    board.penup()  # Lift the pen to move without drawing
    board.color('red')  # Set text color to red
    # Move turtle to screen center and write "Ready! Set! Go!"
    board.goto(0, 0)
    board.write("Ready! Set! Go! ", align="center", font=("Comic Sans MS", 56, "bold"))
    # Play a sound effect for the start message
    Q1_sound_effects.play_sound("ready-set-go-sound-268353.mp3")
    time.sleep(2)  # Pause the screen to let users read the message
    board.clear()  # Clear the message after 2 seconds

def display_draw(board):
    # Prepare the board for writing the draw message
    board.penup()  # Ensure no drawing occurs when moving to position
    board.color('red')  # Set text color to red
    board.goto(0, 0)  # Move turtle to screen center
    message = "It's a Draw!"
    # Display the draw message on the screen
    board.write(message, align="center", font=("Comic Sans MS", 56, "bold"))
    # Play a sound effect for a draw situation
    Q1_sound_effects.play_event_sound("aizen_yare_yare.mp3")

def display_winner(winner, board):
    # Prepare the board to display the winner message
    board.penup()
    board.color('blue')  # Set text color to blue for winner
    board.goto(0, 0)  # Move turtle to screen center
    message = "{} Wins!".format(winner)  # Format the message with the winner's name
    # Display the winner message on the screen
    board.write(message, align="center", font=("Comic Sans MS", 56, "bold"))
    # Play a victory sound effect
    Q1_sound_effects.play_event_sound("luffy_gear_5_laughing.mp3")

def display_spot_taken_message():
    # Use tkinter to create a pop-up message for a taken spot
    root = tkinter.Tk()
    root.withdraw()  # Hide the main tkinter window
    # Show an error messagebox indicating the spot is already taken
    messagebox.showerror('Error', 'This spot is already taken')
    root.destroy()  # Destroy the tkinter instance after displaying the message

def display_invalid_number_input_message():
    # Use tkinter to create a pop-up for invalid number input
    root = tkinter.Tk()
    root.withdraw()  # Hide the main tkinter window
    # Show an error messagebox requesting valid integer input
    messagebox.showerror('Error', 'Please enter a valid integer numbers of row and column')
    root.destroy()  # Destroy the tkinter instance after displaying the message
