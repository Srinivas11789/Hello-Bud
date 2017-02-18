import pygame
import time
import math
import random

# Window Setting
width = 250
height = 250

# Color Setting
color = pygame.Color(100, 255, 0, 0)
background_color = pygame.Color(0, 0, 0, 0)

# Initialize PyGame
pygame.init()

# Window title
pygame.display.set_caption("Hello! Bud")

# Viewing Screen Settings
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

# Surface Settings
surface = pygame.Surface((width, height))
surface.fill(background_color)

# Run Loop for the Sine Wave and the Line Display
running = True
i = 1
sine = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Redraw the background
    surface.fill(background_color)

    # Update sine wave
    frequency = i/10
    i = i + 2
    amplitude = i
    if i > 50:
        i=0
    speed = 0.01
    for x in range(0, width):
        y = 1*(height/2)
        if sine:
           y = int((height/2) + amplitude*math.sin(frequency*((float(x)/width)*(2*math.pi) + (speed*time.time()))))
        surface.set_at((x, y), color)

    # Put the surface we draw on, onto the screen
    screen.blit(surface, (0, 0))

    # Show it.
    pygame.display.flip()
