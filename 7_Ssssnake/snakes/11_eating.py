import random

import pygame, sys
from pygame.locals import *

GAME_CELL_SIZE_PX = 40  # HAVE TO BE EVEN NUMBER
assert (int(GAME_CELL_SIZE_PX/2)*2) == GAME_CELL_SIZE_PX

GAME_CELLS_X = 20
GAME_CELLS_Y = 15

random.seed(a=1)


def draw_segment(surface, x, y):
    """
    :param surface: surface to draw on
    :param x: x coord in game cells
    :param y: y coord in game cells
    :return: 
    """
    WHITE = (255, 255, 255)
    position = (
            x * GAME_CELL_SIZE_PX,
            y * GAME_CELL_SIZE_PX,
            GAME_CELL_SIZE_PX,
            GAME_CELL_SIZE_PX
    )
    pygame.draw.rect(surface, WHITE, position)


def draw_food(surface, x, y):
    """
    :param surface: surface to draw on
    :param x: x coord in game cells
    :param y: y coord in game cells
    :return: 
    """
    RED = (255, 0, 0)
    position = (
        x * GAME_CELL_SIZE_PX + GAME_CELL_SIZE_PX//2,
        y * GAME_CELL_SIZE_PX + GAME_CELL_SIZE_PX//2)
    pygame.draw.circle(surface, RED, position, GAME_CELL_SIZE_PX//2)


class Snake:
    vectors = {
        'UP': (0, -1),
        'DOWN': (0, 1),
        'LEFT': (-1, 0),
        'RIGHT': (1, 0),
    }

    def __init__(self, food):
        self.segments = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]
        self.direction = 'RIGHT'
        self.last_direction = self.direction
        self.food = food

    def _normalize_segments(self):
        for segment in self.segments:
            if segment[0] >= GAME_CELLS_X:
                segment[0] -= GAME_CELLS_X
            if segment[0] < 0:
                segment[0] += GAME_CELLS_X
            if segment[1] >= GAME_CELLS_Y:
                segment[1] -= GAME_CELLS_Y
            if segment[1] < 0:
                segment[1] += GAME_CELLS_Y

    def move(self):
        vector = self.vectors.get(self.direction, (0, 0))
        self.last_direction = self.direction
        # wypadałoby zalogować, że brakuje jakiegos klucza...
        self.segments.pop(0)
        first_segment = self.segments[-1]
        self.segments.append(
            # TODO: a może da się sprytniej? Coś z zip?
            [first_segment[0] + vector[0], first_segment[1] + vector[1]]
        )
        self._normalize_segments()
        self.try_to_eat()

    def draw(self, surface):
        for segment in self.segments:
            draw_segment(surface, *segment)

    def process_event(self, event):
        # te stałe stringi wypadałoby do jakiś constów przenieść
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if not self.last_direction == 'RIGHT':
                    self.direction = 'LEFT'
            elif event.key == K_RIGHT:
                if not self.last_direction == 'LEFT':
                    self.direction = 'RIGHT'
            elif event.key == K_UP:
                if not self.last_direction == 'DOWN':
                    self.direction = 'UP'
            elif event.key == K_DOWN:
                if not self.last_direction == 'UP':
                    self.direction = 'DOWN'

    def try_to_eat(self):
        if (
            self.segments[-1][0] == self.food.x
            and self.segments[-1][1] == self.food.y
        ):
            self.food.eaten()


class FoodProvider:
    def __init__(self):
        self._get_new_coords()

    def _get_new_coords(self):
        self.x = random.randrange(GAME_CELLS_X)
        self.y = random.randrange(GAME_CELLS_Y)

    def draw(self, surface):
        draw_food(surface, self.x, self.y)

    def eaten(self):
        self._get_new_coords()


def draw_background(surface):
    BLACK = (0, 0, 0)
    position = (
        0, 0,
        GAME_CELLS_X * GAME_CELL_SIZE_PX, GAME_CELLS_Y * GAME_CELL_SIZE_PX
    )
    pygame.draw.rect(surface, BLACK, position)


def run_game():
    pygame.init()
    # workaround for: https://github.com/pygame/pygame/issues/331
    pygame.mixer.quit()
    FPS = 10  # Frames Per Second
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(
        (GAME_CELLS_X * GAME_CELL_SIZE_PX, GAME_CELLS_Y * GAME_CELL_SIZE_PX)
    )
    pygame.display.set_caption('Moving segments with snake class')
    food = FoodProvider()
    snake = Snake(food=food)
    while True:
        for event in pygame.event.get():
            print('event: {}'.format(event))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            snake.process_event(event)
        draw_background(DISPLAYSURF)
        snake.draw(DISPLAYSURF)
        food.draw(DISPLAYSURF)
        snake.move()
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    run_game()
