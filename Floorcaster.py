import pygame as pg
import numpy as np

from Settings import *

class Floorcaster():
    def __init__(self,game):
        self.game=game
        self.HRES=240
        self.VERTICAL=240
        self.HALFRES=int(self.VERTICAL/2)
        self.MOD=self.HRES/60
        self.POSX,self.POSY,self.ROT=0,0,0
        self.FRAME=np.random.uniform(0,1,(self.HRES,self.VERTICAL,3))
        self.LoadSky()   
        self.LoadGround() 
    
    def LoadSky(self):
        #self.sky=pg.image.load('Assets/Textures/sky.png').convert_alpha()
        #self.sky=pg.surfarray.array3d(self.sky)#pg.transform.scale(self.sky,(SCREEN_WIDTH,SCREEN_HEIGHT)))
        pg.draw.rect(self.game.DISPLAY,'black',(0,self.game.SCREEN_HEIGHT/2,self.game.SCREEN_WIDTH,self.game.SCREEN_HEIGHT))

    def LoadGround(self):
        pg.draw.rect(self.game.DISPLAY,(25,25,25),(0,self.game.SCREEN_HEIGHT/2,self.game.SCREEN_WIDTH,self.game.SCREEN_HEIGHT))
        pass
    
    def LoadSurface(self):
        #surf_sky = pg.surfarray.make_surface(self.sky)
        #surf_sky= pg.transform.scale(surf_sky,(self.game.SCREEN_WIDTH,self.game.SCREEN_HEIGHT))
        #self.game.DISPLAY.blit(surf_sky,(0,0))
        pass

    def LoadFrames(self,player):
        self.POSX,self.POSY=player.get_pos()
        self.ROT=player.get_angle()

    def Update(self):
        self.LoadSurface() 
        self.LoadGround()   
        