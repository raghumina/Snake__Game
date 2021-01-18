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
        self.direction = Vector2(1, 0)

    def draw_sake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            # create rect
            # draw rectangle
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, pygame.Color("blue"), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]



    def check_fail(self):
        # check if snack is outside the wall
        # check if snack hits itself or wall

        if not 0 <= self.snake.body[0] <= cell_number:
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

class FRUIT:
    def __init__(self):
        self.randomize()
        # we have to create x and y position
        # draw a square
        # self.x = random.randint(0, cell_number - 1)
        # self.y = random.randint(0, cell_number - 1)

        # self.pos = pygame.math.Vector2(self.x, self.y)

    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        # draw a rectangle
        pygame.draw.rect(screen, pygame.Color("black"), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        self.pos = pygame.math.Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_sake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
    # reposition the fruit
    # add one block to snake every time it eats fruit


pygame.init()

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))  # this is length and breadth of the game display
clock = pygame.time.Clock()  # to make game more consistent time wise
# test_surface = pygame.Surface((10, 20))
# test_surface.fill(pygame.Color("black"))
# test_rect = test_surface.get_rect(topright = (200,250))

# fruit = FRUIT()
# snake = SNAKE()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    # Here we will draw all our elements such as dispaly image, snake, fruits etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)

        #  pygame.draw.rect(screen, pygame.Color("red"), test_rect)
        #  test_rect.right +=1
    screen.fill(pygame.Color("RED"))
    main_game.draw_elements()

    #  screen.blit(test_surface, test_rect)  # blit stands for block image transfer
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
