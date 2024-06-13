import pygame as pg
import math
import sys

# Constants
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1600
MAP_SIZE = 16
TILE_SIZE = SCREEN_WIDTH // (2 * MAP_SIZE)
FOV = math.pi / 3
HALF_FOV = FOV / 2
PLAYER_SPEED = 2
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(math.sqrt(2) * MAP_SIZE * TILE_SIZE)

SCALE = (SCREEN_WIDTH ) // CASTED_RAYS

# Initialize player
PLAYER_X = SCREEN_WIDTH // 4
PLAYER_Y = SCREEN_WIDTH // 5
PLAYER_ANGLE = math.pi

# Map as a 2D array
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def cast_rays():
    start_angle = PLAYER_ANGLE - HALF_FOV
    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            target_x = PLAYER_X + math.cos(start_angle) * depth
            target_y = PLAYER_Y + math.sin(start_angle) * depth

            row = int(target_y / TILE_SIZE)
            col = int(target_x / TILE_SIZE)
            if MAP[row][col] == 1:
                color = 255 / (1 + depth * depth * 0.0001)
                depth *= math.cos(PLAYER_ANGLE - start_angle)
                wall_height = 21000 / (depth + 0.0001)
                wall_height = min(wall_height, SCREEN_HEIGHT)

                pg.draw.rect(WIN, (color, color, color), (0 + ray * SCALE, SCREEN_HEIGHT / 2 - wall_height / 2, SCALE, wall_height))
                break

        start_angle += STEP_ANGLE

def draw_map():
    for row in range(len(MAP)):
        for col in range(len(MAP[row])):
            color = (200, 200, 200) if MAP[row][col] == 1 else (100, 100, 100)
            rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 2, TILE_SIZE - 2)
            pg.draw.rect(WIN, color, rect)
            
    pg.draw.circle(WIN, (255, 0, 0), (int(PLAYER_X), int(PLAYER_Y)), 8)
    pg.draw.line(WIN, (0, 255, 0), 
                 (int(PLAYER_X), int(PLAYER_Y)), 
                 (int(PLAYER_X + math.cos(PLAYER_ANGLE) * 50), int(PLAYER_Y + math.sin(PLAYER_ANGLE) * 50)), 3)

# Initialize pygame
pg.init()
WIN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pg.time.Clock()

# Game loopma
while True:
    #WIN.fill(0,0,0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)

    # Drawing the 2D and 3D views
    pg.draw.rect(WIN, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.draw.rect(WIN, (100, 100, 100), (0, SCREEN_HEIGHT//2 , SCREEN_WIDTH , SCREEN_HEIGHT//2))  # Floor
    pg.draw.rect(WIN, (200, 200, 200), (0, SCREEN_WIDTH//2 , SCREEN_WIDTH, SCREEN_HEIGHT//2))  # Ceiling
    
    #draw_map()
    cast_rays()

    # Player movement and collision detection
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]: PLAYER_ANGLE -= 0.1
    if keys[pg.K_RIGHT]: PLAYER_ANGLE += 0.1
    if keys[pg.K_UP]:
        new_x = PLAYER_X + math.cos(PLAYER_ANGLE) * PLAYER_SPEED
        new_y = PLAYER_Y + math.sin(PLAYER_ANGLE) * PLAYER_SPEED
        if MAP[int(new_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            PLAYER_X, PLAYER_Y = new_x, new_y
    if keys[pg.K_DOWN]:
        new_x = PLAYER_X - math.cos(PLAYER_ANGLE) * PLAYER_SPEED
        new_y = PLAYER_Y - math.sin(PLAYER_ANGLE) * PLAYER_SPEED
        if MAP[int(new_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            PLAYER_X, PLAYER_Y = new_x, new_y

    # Display FPS
    fps = str(int(CLOCK.get_fps()))
    font = pg.font.SysFont('Monospace Regular', 30)
    text_surface = font.render(fps, False, (255, 255, 255))
    WIN.blit(text_surface, (0, 0))
    
    pg.display.flip()
    CLOCK.tick(60)