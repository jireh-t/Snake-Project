"""Version 6 - displaying the fruit and eating it"""

import pygame
import time
import random
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
msg_font = pygame.font.SysFont("impact", 50)


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


clock = pygame.time.Clock()  # Sets the speed at which the snake moves

# Loop to keep screen open until user presses 'X'
quit_game = False

# Snake will be 20 x 20 pixels
snake_x = 490  # Centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 350  # Centre point vertically is (720-20 snake height)/2 = 350

snake_x_change = 0  # Holds the value of changes in the x-coordinate
snake_y_change = 0  # Holds the value of changes in the y-coordinate

# Setting a random position for the food - to start
food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
food_y = round(random.randrange(20, 720 - 20) / 20) * 20

while not quit_game:
    # If snake runs into wall, game ends
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        # Directions to make snake move
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

    if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(yellow)  # Changes screen (surface) from default black to green

    # Create rectangle for snake
    pygame.draw.rect(screen, purple, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    # Create circle for food
    pygame.draw.circle(screen, red, [food_x, food_y], 10)
    pygame.display.update()

    # Collision detection (test if snake touches food)
    if snake_x == food_x - 10 and snake_y == food_y - 10:
        # Set new random position for food if snake touches it
        food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
        food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    clock.tick(5)  # Sets the speed at which each iteration of the game loop
    # Runs in frames per second (fps). IN this case it is set to 5fps

# Display dead message when snake dies and quit
message("You died!", white, purple)
pygame.display.update()
time.sleep(3)

pygame.quit
quit()
