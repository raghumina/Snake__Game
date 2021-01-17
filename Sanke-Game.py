# SNAKE GAME
# THIS SNAKE GAME WAS MADE WITH THE HELP OF PYGAME MODULE
# PYTHON PYGAME MODULE IS USE TO CREATE GAMES
import sys
import pygame
import random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_sake(self):
        for block in self.body:
            # create rect
            # draw rectangle
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)


class FRUIT:
    def __init__(self):
        # we have to create x and y position
        # draw a square
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_size - 1)

        self.pos = pygame.math.Vector2(self.x, self.y)

    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_number)
        # draw a rectangle
        pygame.draw.rect(screen, (200, 200, 200), fruit_rect)


pygame.init()

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))  # this is length and breadth of the game display
clock = pygame.time.Clock()  # to make game more consistent time wise
# test_surface = pygame.Surface((10, 20))
# test_surface.fill(pygame.Color("black"))
# test_rect = test_surface.get_rect(topright = (200,250))

fruit = FRUIT()

while True:
    # Here we will draw all our elements such as dispaly image, snake, fruits etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        #  pygame.draw.rect(screen, pygame.Color("red"), test_rect)
        #  test_rect.right +=1
    screen.fill(pygame.Color("Green"))
    fruit.draw_fruit()
    #  screen.blit(test_surface, test_rect)  # blit stands for block image transfer
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
