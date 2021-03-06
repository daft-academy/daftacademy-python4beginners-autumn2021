import pygame, sys
from pygame.locals import *

GAME_CELL_SIZE_PX = 50  # HAVE TO BE EVEN NUMBER
assert (int(GAME_CELL_SIZE_PX/2)*2) == GAME_CELL_SIZE_PX

GAME_CELLS_X = 20
GAME_CELLS_Y = 15

# list is a bad idea ...
# much better:
# https://docs.python.org/3.5/library/collections.html#collections.deque
# Ale nie jestem w stanie zgadnąć czy w przypadku krótkiego węża różnica
# będzie zauważalna
snake_segments = [(0, 5), (1, 5), (2, 5)]


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


def move_snake_right(snake_segments):
    # usunięcie ostatniego segmentu
    snake_segments.pop(0)
    # dodanie elementu na początek
    first_segment = snake_segments[-1]
    snake_segments.append((first_segment[0] + 1, first_segment[1]))


def draw_snake(surface, snake_segments):
    for segment in snake_segments:
        draw_segment(surface, *segment)


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
    pygame.display.set_caption('Moving segments')
    # for x in range(GAME_CELLS_X):
    #     for y in range(GAME_CELLS_Y):
    #         if (x + y) % 2 == 0:
    #             draw_segment(surface=DISPLAYSURF, x=x, y=y)
    #         else:
    #             draw_food(surface=DISPLAYSURF, x=x, y=y)
    frame_number = 0
    while True:
        for event in pygame.event.get():
            print('event: {}'.format(event))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # draw_background(DISPLAYSURF)
        draw_snake(DISPLAYSURF, snake_segments)
        move_snake_right(snake_segments)
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    run_game()
