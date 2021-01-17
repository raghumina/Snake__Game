# SNAKE GAME
# THIS SNAKE GAME WAS MADE WITH THE HELP OF PYGAME MODULE
# PYTHON PYGAME MODULE IS USE TO CREATE GAMES
import sys
import pygame

pygame.init()


screen = pygame.display.set_mode((600, 600))  # this is length and breadth of the game display
clock = pygame.time.Clock()  # to make game more consistent time wise


while True:
    # Here we will draw all our elements such as dispaly image, snake, fruits etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    pygame.display.update()
    clock.tick(60)     # 60 frames per second
