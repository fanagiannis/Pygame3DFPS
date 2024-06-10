import pygame as pg
import numpy as np

from Settings import *

class Floorcaster():
    def __init__(self):
        self.HRES=120
        self.VERTICAL=200
        self.HALFRES=int(self.VERTICAL/2)
        self.MOD=self.HALFRES/60
        self.POSX,self.POSY,self.ROT=0,0,0
        self.FRAME=np.random.uniform(0,1,(self.HRES,self.VERTICAL,3))
        
        self.sky=pg.image.load('Assets/Images/skybox.jpg')
        self.sky=self.LoadSky()
        

    def LoadSky(self):
        self.sky=pg.surfarray.make_surface(self.FRAME*255)
        self.sky=pg.transform.scale(self.sky,(SCREEN_WIDTH,SCREEN_HEIGHT))
        DISPLAY.blit(self.sky,(0,0))
        #pg.display.update()
        #self.sky=pg.surfarray.array3d(pg.transform.scale(self.sky,(360,self.HALFRES*2)))
        pass

    def update(self,player):
        self.LoadSky()
        for i in range(self.HRES):
            ROT_i=self.ROT+np.deg2rad(i/self.MOD-30)
            sin,cos=np.sin(ROT_i),np.cos(ROT_i)

            #self.FRAME[i][:]=self.SURF[int(np.rad2deg(ROT_i)%360)][:]/255

            for j in range (self.HALFRES):
                n=self.HALFRES / (self.HALFRES- j)
                x,y= self.POSY*0.1+cos*n,-self.POSX*0.1 +sin*n                                          #!!!WARNING! REVERSE X AND Y FROM PLAYER MOVEMENT! y=-PLAYER POSISTION ON Y!
                if int(x)%2 ==int(y)%2:
                    self.FRAME[i][self.HALFRES*2-j-1]=[0,0,0]
                else:
                    self.FRAME[i][self.HALFRES*2-j-1]=[1,1,1]
        self.POSX,self.POSY=player.get_pos()
        self.ROT=player.get_angle()
        print(self.POSX,self.POSY,self.ROT)
        #surf = pg.surfarray.make_surface(self.FRAME*255)
        #surf= pg.transform.scale(surf,(800,600))
        #DISPLAY.blit(surf,(0,0))
        pass