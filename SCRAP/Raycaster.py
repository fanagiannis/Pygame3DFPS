import pygame as pg
import math

from Settings import *


class Raycaster:
    def __init__(self, game):
        self.game=game
        self.MAP=self.game.selectedmap.mini_map
        self.FOV=self.game.player.FOV
        self.PLAYER_ANGLE=self.game.player.angle
        self.CASTED_RAYS=80#SCREEN_WIDTH//2
        self.TILE_SIZE=self.game.selectedmap.tilesize
        self.MAX_DEPTH=int(math.sqrt(2) * MAP_SIZE *self.TILE_SIZE)
        self.STEP_ANGLE = self.FOV/self.CASTED_RAYS
        self.px,self.py=self.game.player.get_pos()
        self.SCALE = (SCREEN_WIDTH ) // self.CASTED_RAYS
        pass

    def cast_rays(self):
        start_angle = self.PLAYER_ANGLE - self.FOV
        for ray in range(self.CASTED_RAYS):
            for depth in range(self.MAX_DEPTH):
                target_x = self.px + math.cos(start_angle) * depth
                target_y = self.py + math.sin(start_angle) * depth

                row = int(target_y / self.TILE_SIZE)
                col = int(target_x / self.TILE_SIZE)
                if self.MAP[row][col] == 1:
                    color = 255 / (1 + depth * depth * 0.0001)
                    depth *= math.cos(self.PLAYER_ANGLE - start_angle)
                    wall_height = 21000 / (depth + 0.0001)
                    wall_height = min(wall_height, SCREEN_HEIGHT)

                    pg.draw.rect(DISPLAY, (color, color, color), (0 + ray * self.SCALE, SCREEN_HEIGHT / 2 - wall_height / 2, self.SCALE, wall_height))
                    break

            start_angle += self.STEP_ANGLE

    def update(self):
        self.cast_rays()
        pass

if __name__=='__main__':
    print("RAYCASTER")