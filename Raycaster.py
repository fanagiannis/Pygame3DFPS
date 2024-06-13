import pygame as pg
import math
class Raycaster():
    def __init__(self,game):
        self.game=game
        self.CASTED_RAYS=120#int(self.game.SCREEN_WIDTH/5)
        self.MAX_DEPTH=int(self.game.SCREEN_WIDTH/2)
        self.TILE_SIZE=self.game.map.tilesize

    def cast_rays(self):
        SCALE = self.game.SCREEN_WIDTH//self.CASTED_RAYS
        STEP_ANGLE=(self.game.player.FOV)/self.CASTED_RAYS
        PLAYER_X,PLAYER_Y=self.game.player.Get_pos
        START_ANGLE = self.game.player.Get_angle - self.game.player.FOV/2
        for ray in range(self.CASTED_RAYS):
            for depth in range(self.MAX_DEPTH):
                TARGET_X= PLAYER_X + math.cos(START_ANGLE) * depth
                TARGET_Y = PLAYER_Y + math.sin(START_ANGLE) * depth

                row = int(TARGET_Y / self.TILE_SIZE)
                col = int(TARGET_X / self.TILE_SIZE)
                #pg.draw.line(self.game.DISPLAY,'yellow',(self.game.player.Get_pos),(TARGET_X,TARGET_Y),2)
                if self.game.map.mini_map[row][col] == 1:
                    color = 255 / (1 + depth * depth * 0.0001)
                    depth *= math.cos(self.game.player.ANGLE - START_ANGLE)
                    wall_height = 21000 / (depth + 0.0001)
                    wall_height = min(wall_height, self.game.SCREEN_HEIGHT)
                    

                    pg.draw.rect(self.game.DISPLAY, (color, color, color), (ray * SCALE, self.game.SCREEN_HEIGHT / 2 - wall_height / 2, SCALE, wall_height))
                    break

            START_ANGLE+=STEP_ANGLE
    
    def Update(self):
        self.cast_rays()