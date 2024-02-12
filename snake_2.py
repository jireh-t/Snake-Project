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
green = (0, 153, 76)

# Fonts for the game
score_font = pygame.font.SysFont("calibri", 20)
exit_font = pygame.font.SysFont("impact", 30)

# Snake will be 20 x 20 pixels
snake_x = 490  # Centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 350  # Centre point vertically is (720-20 snake height)/2 = 350

# Loop to keep screen open until user presses 'X'
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # Create rectangle for snake
    pygame.draw.rect(screen, purple, [snake_x, snake_y, 20, 20])
    pygame.display.update()

pygame.quit
quit()
