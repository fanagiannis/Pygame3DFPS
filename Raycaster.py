import pygame as pg
import numpy as np

class Raycaster():
    def __init__(self,game):
        self.game=game
        self.CASTED_RAYS=int(self.game.SCREEN_WIDTH/5)
        self.MAX_DEPTH=int(self.game.SCREEN_WIDTH/2)
        self.TILE_SIZE=self.game.map.tilesize
        pass

    def cast_rays(self):
        SCALE = self.game.SCREEN_WIDTH//self.CASTED_RAYS
        STEP_ANGLE=(self.game.player.FOV)/self.CASTED_RAYS
        START_ANGLE=self.game.player.ANGLE-self.game.player.FOV*2
        PLAYER_X,PLAYER_Y=self.game.player.Get_pos
        for rays in range(self.CASTED_RAYS): 
            for depth in range(self.MAX_DEPTH):
                TARGET_X=PLAYER_X-np.sin(START_ANGLE)*depth
                TARGET_Y=PLAYER_Y+np.cos(START_ANGLE)*depth
                #pg.draw.line(self.game.DISPLAY,'yellow',(self.game.player.posx,self.game.player.posy),(TARGET_X,TARGET_Y),2)

                row=int(TARGET_Y/self.TILE_SIZE)
                column=int(TARGET_X/self.TILE_SIZE)
                square=row*self.game.map.Mapsize
                if self.game.map.check_collision(TARGET_X,TARGET_Y):
                    #pg.draw.rect(self.game.DISPLAY,'WHITE',(column*self.TILE_SIZE,row*self.TILE_SIZE,self.TILE_SIZE-2,self.TILE_SIZE-2))
                    
                    wall_height=42000/(depth+0.001) #min=21000/480~43px max=21000/0.0001=210000000 px (!)

                    pg.draw.rect(self.game.DISPLAY,'WHITE',(rays*SCALE,self.game.SCREEN_HEIGHT/2-wall_height/2,SCALE,wall_height))#

            START_ANGLE+=STEP_ANGLE

    def Update(self):
        self.cast_rays()