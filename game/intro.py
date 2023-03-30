#Authors: Ukeme Etuk, Biobele Harry, Clinton Quaye

import pygame
import main

# Define some colors
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
PURPLE = (174, 105, 215)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
DIM = pygame.display.get_desktop_sizes()
WIDTH = DIM[0][0]-100
HEIGHT = DIM[0][1]-100
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("FreeSort")

# Create a font object
font = pygame.font.Font(None, 90)

# Create a button rectangle
button_rect = pygame.Rect(150, 400, 200, 80)

# Create a button label
button_label = font.render("Start", True, WHITE)

# Create a game title
title = font.render("Welcome to FreeSort", True, PURPLE)

# Set the intro screen loop to True
intro_screen = True

while intro_screen:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_screen = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                intro_screen = False
    
    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw the title
    screen.blit(title, (110, 100))
    
    # Draw the button
    pygame.draw.rect(screen, PURPLE, button_rect, 0, 20)
    screen.blit(button_label, (173, 413))
    
    # Update the display
    pygame.display.flip()

# Start the game
main.main()

# Quit Pygame
pygame.quit()