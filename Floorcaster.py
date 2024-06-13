import pygame as pg
import numpy as np

from Settings import *

class Floorcaster():
    def __init__(self):
        self.HRES=240
        self.VERTICAL=240
        self.HALFRES=int(self.VERTICAL/2)
        self.MOD=self.HRES/60
        self.POSX,self.POSY,self.ROT=0,0,0
        self.FRAME=np.random.uniform(0,1,(self.HRES,self.VERTICAL,3))
        self.LoadSky()   
        self.LoadGround() 
    
    def LoadSky(self):
        self.sky=pg.image.load('Assets/Images/skybox.jpg').convert_alpha()
        self.sky=pg.surfarray.array3d(self.sky)#pg.transform.scale(self.sky,(SCREEN_WIDTH,SCREEN_HEIGHT)))
        pass

    def LoadGround(self):
        pg.draw.rect(DISPLAY,(50,50,50),(0,SCREEN_HALF_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT))
        pass
    
    def LoadSurface(self):
        surf_sky = pg.surfarray.make_surface(self.sky)
        surf_sky= pg.transform.scale(surf_sky,(SCREEN_WIDTH,SCREEN_HEIGHT))
        DISPLAY.blit(surf_sky,(0,0))

    def LoadFrames(self,player):
        self.POSX,self.POSY=player.get_pos()
        self.ROT=player.get_angle()

    def Update(self,player): pass
