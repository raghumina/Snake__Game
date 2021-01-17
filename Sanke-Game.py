# SNAKE GAME
# THIS SNAKE GAME WAS MADE WITH THE HELP OF PYGAME MODULE
# PYTHON PYGAME MODULE IS USE TO CREATE GAMES
import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))  # this is length and breadth of the game display
clock = pygame.time.Clock()  # to make game more consistent time wise
test_surface = pygame.Surface((50, 20))
test_surface.fill(pygame.Color("black"))

while True:
    # Here we will draw all our elements such as dispaly image, snake, fruits etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    screen.fill(pygame.Color("Green"))
    screen.blit(test_surface, (200, 250))  # blit stands for block image transfer
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
