import pygame as pg

from Settings import*
from Player import*

class Raycaster():
    def __init__(self,rays):
        self.start_angle=P.angle-P.HFOV
        self.rays_casted=rays
        self.step_angle=P.FOV/self.rays_casted
        self.depth=int(map_default.size*map_default.tile_size)

    def cast_rays(self):
        for rays in range(self.rays_casted):
            for depth in range(self.depth):
                TARGET_X=P.posx-math.sin(P.angle)*self.depth
                TARGET_Y=P.posy+math.cos(P.angle)*self.depth
                pg.draw.line(DISPLAY,(0,255,0),(P.posx,P.posy),(TARGET_X,TARGET_Y),3)

    def update(self):
        self.cast_rays()

RayCaster=Raycaster()