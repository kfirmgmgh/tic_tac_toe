
# submitter: kfir mutzary gridi
#ID:206397770

import pygame

def init_pygame():
    # Initialize all imported Pygame modules
    pygame.init()
    # Initialize the mixer module for sound playback
    pygame.mixer.init()

def play_sound(sound_file):
    # Load and play a specific sound file
    sound = pygame.mixer.Sound(sound_file)  # Create a Sound object from a file
    sound.play()  # Play the sound

def play_event_sound(sound_file):
    # Play a sound file with special handling to pause and unpause background music
    pygame.mixer.music.pause()  # Pause any currently playing background music
    event_sound = pygame.mixer.Sound(sound_file)  # Create a Sound object for the event
    event_sound.play()  # Play the event sound
    # Wait for the event sound to finish playing
    while pygame.mixer.get_busy():
        pygame.time.delay(100)  # Delay to allow sound to finish without blocking other processes
    pygame.mixer.music.unpause()  # Unpause the background music after the event sound has played

def play_background_music():
    # Play background music continuously
    pygame.mixer.music.load("Escalon.mp3")  # Load the background music file
    pygame.mixer.music.play(-1)  # Start playing the background music in a loop
