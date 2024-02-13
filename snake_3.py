"""Version 3 setting up movements of the snake"""

import pygame
import time
pygame.init()

# Set screen size and icon
screen = pygame.display.set_mode((1000, 720))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Jireh Tseng")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
purple = (109, 11, 222)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 153)

# Fonts for the game
score_font = pygame.font.SysFont("calibri", 20)
exit_font = pygame.font.SysFont("impact", 30)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves

# Loop to keep screen open until user presses 'X'
quit_game = False

# Snake will be 20 x 20 pixels
snake_x = 490  # Centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 350  # Centre point vertically is (720-20 snake height)/2 = 350

snake_x_change = 0  # Holds the value of changes in the x-coordinate
snake_y_change = 0  # Holds the value of changes in the y-coordinate

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0

            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0

            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20

            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(yellow)  # Changes screen (surface) from default black to green

    # Create rectangle for snake
    pygame.draw.rect(screen, purple, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5)  # Sets the speed at which each iteration of the game loop
    # Runs in frames per second (fps). IN this case it is set to 5fps

pygame.quit
quit()
