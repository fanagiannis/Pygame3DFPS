import pygame as pg
import math

from Settings import *
from Player import *

class Raycaster:
    def __init__(self, game):
        self.game = game
        self.rays_casted = SCREEN_WIDTH//2
        self.FOV=math.pi/3
        self.HALF_FOV=self.FOV/2
        self.HALF_NUM_RAYS=self.rays_casted//2
        self.DELTA_ANGLE=self.FOV/self.rays_casted
        self.maxdepth = 20
        
    def cast_rays(self):
        px,py=self.game.player.posx,self.game.player.posy
        x_map,y_map=self.game.player.get_map_pos()
        ray_angle=self.game.player.angle-self.HALF_FOV+0.0001
        for ray in range(self.rays_casted):
            sin_a=math.sin(ray_angle)
            cos_a=math.cos(ray_angle)

            #HORIZONTALS
            y_hor,dy=(y_map+1,1)if sin_a>0 else (y_map-1e-6,-1)

            depth_hor=(y_hor-py)/sin_a
            x_hor=px+depth_hor*cos_a

            delta_depth=dy/sin_a
            dx=delta_depth*cos_a

            for i in range(self.maxdepth):
                tile_hor=int(x_hor),int(y_hor)
                if tile_hor in self.game.selectedmap.world_map:
                    break
                x_hor+=dx
                y_hor+=dy
                depth_hor+=delta_depth

            #VERTICALS 
            x_vert,dx=(x_map+1,1)if cos_a>0 else(x_map-1e-6,-1)
            depth_vert=(x_vert-px)/cos_a
            y_vert=py + depth_vert*sin_a

            delta_depth=dx/cos_a
            dy=delta_depth*sin_a

            for i in range(self.maxdepth):
                tile_vert=int(x_vert),int(y_vert)
                if tile_vert in self.game.selectedmap.world_map:
                    break
                x_vert+=dx
                y_vert+=dy
                depth_vert+=delta_depth
            
            if depth_vert<depth_hor:
                depth=depth_vert
            else:
                depth=depth_hor

            pg.draw.line(DISPLAY,'yellow',(px,py),(100*px+100*depth*cos_a,100*py+100*depth*sin_a),2) 


            ray_angle+=self.DELTA_ANGLE

    def update(self):
        self.cast_rays()
        
if __name__ == '__main__':
    print("RayCaster")
