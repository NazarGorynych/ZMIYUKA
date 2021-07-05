import pygame
import sys
from random import choice
from conig import *


class Snake:

    def __init__(self):
        self.position = [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)]
        self.length = 1
        self.direction = choice([(UP), (DOWN), (LEFT), (RIGHT)])

    def drawS(self, surface):
            rect = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, (255, 0, 0), rect)

    def get_head_pos(self):
        # self.position = [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)]
        return self.position

    def turn(self, point):
        pass

    def move(self):
        mov = self.get_head_pos()

        # self.direction = choice([(UP), (DOWN), (LEFT), (RIGHT)])
        x, y = self.direction[0], self.direction[1]
        self.position[0] += (x * GRIDSIZE)
        self.position[1] += (y * GRIDSIZE)
        self.position[0] %= SCREEN_WIDTH
        self.position[1] %= SCREEN_HEIGHT
            # [
            # ((mov[0][0] + (x * GRIDSIZE) / SCREEN_WIDTH), ((mov[0][1] + (y * GRIDSIZE)) / SCREEN_HEIGHT))]


class Food:
    
    @staticmethod
    def draw_food(surface):
        rect = (rnumber, rnumber2), (GRIDSIZE, GRIDSIZE)
        pygame.draw.rect(surface, (0, 255, 255), rect)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, (10, 20, 10), r)
            else:
                pygame.draw.rect(surface, (15, 50, 20), r)


# COSMETICS
pygame.display.set_caption('ZMIYUKA')
icon = pygame.image.load('snakes (1).png')
pygame.display.set_icon(icon)


# GAME LOOP
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    meal = Food()
    johny = Snake()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(surface, (0, 0))
        draw_grid(surface)
        clock.tick(10)
        meal.draw_food(surface)
        johny.move()

        # JOHNY.get_head_pos()
        johny.drawS(surface)
        pygame.display.update()


main()
