"""Version 8 - allow the user to click 'X' to quit"""

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
msg_font = pygame.font.SysFont("calibri", 50)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


# Function to run the main game loop
def game_loop():

    # Loop to keep screen open until user presses 'X'
    quit_game = False
    game_over = False

    # Snake will be 20 x 20 pixels
    snake_x = 490  # Centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 350  # Centre point vertically is (720-20 snake height)/2 = 350

    snake_x_change = 0  # Holds the value of changes in the x-coordinate
    snake_y_change = 0  # Holds the value of changes in the y-coordinate

    # Setting a random position for the food - to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            screen.fill(yellow)
            message("You died! Press 'Q' to Quit or 'A' to play Again",
                    white, purple)
            pygame.display.update()

            # Check if user wants to quit (Q) or play again (A)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Check which key is pressed

                    # If 'Q' is pressed
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False

                    # If 'A' is pressed
                    if event.key == pygame.K_a:
                        game_loop()  # Restart the main game loop

        # Handling response if user presses 'X' - giving them the option to
        # quit, start a new game, or keep playing

        for event in pygame.event.get():

            # Give instructions if user presses 'X'
            if event.type == pygame.QUIT:
                instructions = "Exit: X to Quit, SPACE to resume, R to reset"
                message(instructions, white, purple)
                pygame.display.update()

                end = False

                while not end:
                    for event in pygame.event.get():
                        # If user presses 'X' button, game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True

                        # If user presses 'R' button again, game is reset
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()

                        # If user presses the space-bar, game continues

                        

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
            game_over = True

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


    pygame.quit
    quit()

# Main Routine
game_loop()
