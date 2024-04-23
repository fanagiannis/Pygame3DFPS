import pygame as pg

from Settings import*
from Player import*

class Raycaster():
    def __init__(self,rays):
        
        self.rays_casted=rays
        self.step_angle=P.FOV/self.rays_casted
        self.depth=int(map_default.size*map_default.tile_size)

    def cast_rays(self):
        playerposx,playerposy=P.get_pos()
        playermapposx,playermapposy=P.get_map_pos()
        self.start_angle=P.get_angle()-P.HFOV+0.0001
        for rays in range(self.rays_casted):
            
            for depth in range(self.depth):
                PLAYER_X,PLAYER_Y=P.get_pos()
                TARGET_X=PLAYER_X-math.sin(P.get_angle())*self.depth
                TARGET_Y=PLAYER_Y+math.cos(P.get_angle())*self.depth
                pg.draw.line(DISPLAY,(0,255,0),(P.get_pos()),(TARGET_X,TARGET_Y),3)

                row=int(TARGET_Y/map_default.tile_size)
                column=int(TARGET_X/map_default.tile_size)
                square=square=row*map_default.size+column
                if map_default.get_map()[square]=='#':
                    pg.draw.rect(DISPLAY,(0,255,0),(column*map_default.tile_size,row*map_default.tile_size,map_default.tile_size,map_default.tile_size))
                    depth=depth*math.cos(P.get_angle()-self.start_angle)
                    break
            self.start_angle+=self.step_angle
            

    def update(self):
        self.cast_rays()

RayCaster=Raycaster(80)