import pygame as pg
import math

from numba import njit

class Raycaster():
    def __init__(self,game):
        self.game=game
        self.CASTED_RAYS=int(self.game.SCREEN_WIDTH/10)
      
        self.MAX_DEPTH=int(self.game.SCREEN_WIDTH/10)
        self.TILE_SIZE=self.game.map.tilesize
        pass
    
    def cast_rays(self):
        STEP_ANGLE=(self.game.player.FOV)/self.CASTED_RAYS
        START_ANGLE=self.game.player.ANGLE-self.game.player.FOV*2
        for rays in range(self.CASTED_RAYS): 
            for depth in range(self.MAX_DEPTH):
                TARGET_X=self.game.player.posx-math.sin(START_ANGLE)*depth
                TARGET_Y=self.game.player.posy+math.cos(START_ANGLE)*depth
                pg.draw.line(self.game.DISPLAY,'yellow',(self.game.player.posx,self.game.player.posy),(TARGET_X,TARGET_Y),2)

                row=int(TARGET_Y/self.TILE_SIZE)
                column=int(TARGET_X/self.TILE_SIZE)
                square=row*self.game.map.Mapsize
                if self.game.map.check_collision(TARGET_X,TARGET_Y):
                    pg.draw.rect(self.game.DISPLAY,'WHITE',(column*self.TILE_SIZE,row*self.TILE_SIZE,self.TILE_SIZE-2,self.TILE_SIZE-2))

            START_ANGLE+=STEP_ANGLE

    def Update(self):
        self.cast_rays()