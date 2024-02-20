"""Version 14 - displaying the high score from the file"""

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
score_font = pygame.font.SysFont("snake chan.ttf", 30)
exit_font = pygame.font.SysFont("impact", 30)
msg_font = pygame.font.SysFont("calibri", 50)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves


# Function to keep track of the highest score - writes value to a file
def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", 'r')
    except IOError:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value


# Function to update record of the highest score
def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score


# Function to save updated hgh score if player beats it
def save_high_score(high_score):
    high_score_file = open("HI_score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()


# Function to display player score throughout the game
def player_score(score, score_colour, hi_score):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20))  # Coordinates for top right

    # High score
    display_score = score_font.render(f"High Score: {hi_score}", True,
                                      score_colour)
    screen.blit(display_score, (10, 10))  # Coordinates for top left


# Function to display messages throughout the game
def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


# Function to create snake - replaces the previous snake drawing section in
# main loop
def draw_snake(snake_list):
    for i in snake_list:
        # x and y coordinates of snake section, and dimensions
        pygame.draw.rect(screen, purple, [i[0], i[1], 20, 20])


# Function to run the main game loop
def game_loop():

    # Loop to keep screen open until user presses 'X'
    quit_game = False
    game_over = False

    # Snake will be 20 x 20 pixels - coordinates set to work for a 20px grid
    snake_x = 480  # Centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 340  # Centre point vertically is (720-20 snake height)/2 = 350

    snake_x_change = 0  # Holds the value of changes in the x-coordinate
    snake_y_change = 0  # Holds the value of changes in the y-coordinate
    snake_list = []
    snake_length = 1

    # Setting a random position for the food - to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    # Load the high score
    high_score = load_high_score()
    print(f"high_score: {high_score}")  # For testing purposes only

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            save_high_score(high_score)
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
                            if event.key == pygame.K_SPACE:
                                end = True

                        # If user presses 'Q' game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True

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

        screen.fill(yellow)  # Changes screen (surface) from default black
        # to yellow

        # Create snake (replaces simple rectangle in previous section)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)  # Nest snake head in snake list

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Detect if snake head touches any other part of the snake
        for x in snake_list[:-1]:  # Counting from the end of the snake list
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        # Keeping track of the player's score
        score = snake_length - 1  # Score excludes snake's head
        player_score(score, black, high_score)

        # Get high score
        high_score = update_high_score(score, high_score)

        # Link speed of snake to player score to increase difficulty
        if score > 3:
            speed = score
        else:
            speed = 3

        # Using a sprite (instead of the previous circle) to represent food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_2.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        # Collision detection (test if snake touches food)

        # Detecting snake contact with food sprite (instead of circle)
        if snake_x == food_x and snake_y == food_y:
            # Set new random position for food if snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

            # Load the high score
            high_score = load_high_score()

            # Increase length of snake (by original size)
            snake_length += 1

        # Sets the speed at which each iteration of the game loop
        # Runs in frames per second (fps). IN this case it is set to 5fps
        clock.tick(speed)

    pygame.quit()
    quit()


# Main Routine
game_loop()