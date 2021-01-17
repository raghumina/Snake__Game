# SNAKE GAME
# THIS SNAKE GAME WAS MADE WITH THE HELP OF PYGAME MODULE
# PYTHON PYGAME MODULE IS USE TO CREATE GAMES
import sys
import pygame

pygame.init()

cell_size = 20
cell_number = 40

screen = pygame.display.set_mode((400, 500))  # this is length and breadth of the game display
clock = pygame.time.Clock()  # to make game more consistent time wise
# test_surface = pygame.Surface((10, 20))
# test_surface.fill(pygame.Color("black"))
# test_rect = test_surface.get_rect(topright = (200,250))

while True:
    # Here we will draw all our elements such as dispaly image, snake, fruits etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        #  pygame.draw.rect(screen, pygame.Color("red"), test_rect)
        #  test_rect.right +=1
    screen.fill(pygame.Color("Green"))
    #  screen.blit(test_surface, test_rect)  # blit stands for block image transfer
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
