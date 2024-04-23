import pygame as pg

from Settings import*
from Player import*

class Raycaster():
    def __init__(self,rays):
        self.rays_casted=rays
        self.step_angle=P.FOV/self.rays_casted
        self.maxdepth=int(map_default.size*map_default.tile_size)
        self.scale=(SCREEN_WIDTH/2)/self.rays_casted
        
        

    def cast_rays(self):
        MAP=map_default.get_map()
        start_angle=P.get_angle()-P.HFOV+0.001
       
        for rays in range(self.rays_casted):   
            for depth in range(self.maxdepth):
                PLAYER_X,PLAYER_Y=P.get_pos()
                PLAYER_ANGLE=P.get_angle()
                TARGET_X=PLAYER_X-math.sin(start_angle)*depth
                TARGET_Y=PLAYER_Y+math.cos(start_angle)*depth
                pg.draw.line(DISPLAY,(0,255,0),(PLAYER_X,PLAYER_Y),(TARGET_X,TARGET_Y),3)

                row=int(TARGET_Y/map_default.tile_size)
                column=int(TARGET_X/map_default.tile_size)
                square=square=row*map_default.size+column


                if MAP[square]=='#':
                    pg.draw.rect(DISPLAY,(0,255,0),(column*map_default.tile_size,row*map_default.tile_size,map_default.tile_size,map_default.tile_size))
                    depth=depth*math.cos(PLAYER_ANGLE-start_angle)
                    
                    color= 255/(1+depth*depth*0.001)
                    wallheight=21000/(depth+0.0001)

                    pg.draw.rect(DISPLAY,(color,color,color),(SCREEN_HEIGHT + rays*self.scale,SCREEN_HEIGHT/2 - wallheight/2,self.scale,wallheight))
                    break
            start_angle+=self.step_angle
            pass
        pass
            

    def update(self):
        self.cast_rays()

RayCaster=Raycaster(80)