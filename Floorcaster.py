import pygame as pg
import numpy as np

from Settings import *

class Floorcaster():
    def __init__(self):
        self.HRES=120
        self.VERTICAL=100
        self.HALFRES=int(self.VERTICAL/2)
        self.MOD=self.HRES/60
        self.POSX,self.POSY,self.ROT=0,0,0
        self.FRAME=np.random.uniform(0,1,(self.HRES,self.VERTICAL,3))
        self.LoadSky()   
        self.LoadGround() 

    def LoadSky(self):
        self.sky=pg.image.load('Assets/Images/skybox.jpg').convert_alpha()
        self.sky=self.sky.convert_alpha()
        self.sky=pg.surfarray.array3d(pg.transform.scale(self.sky,(360,self.HALFRES*2)))

    def LoadGround(self):
        self.floor=pg.surfarray.array3d(pg.image.load('Assets/Images/floor2.jpg').convert_alpha())
    
    def LoadSurface(self):
        surf = pg.surfarray.make_surface(self.FRAME*255)
        surf= pg.transform.scale(surf,(SCREEN_WIDTH,SCREEN_HEIGHT))
        DISPLAY.blit(surf,(0,0))

    def LoadFrames(self,player):
        self.POSX,self.POSY=player.get_pos()
        self.ROT=player.get_angle()
        frame=self.FrameCalculation(self.HRES,self.MOD,self.HALFRES,self.POSX,self.POSY,self.ROT,self.floor,self.FRAME)
   
    def FrameCalculation(self,HRES,MOD,HALFRES,POSX,POSY,ROT,floor,frame):
        for i in range(HRES):
            ROT_i=ROT+np.deg2rad(i/MOD-30)
            sin,cos,cos2=np.sin(ROT_i),np.cos(ROT_i),np.cos(np.deg2rad(i/MOD-30))

            frame[i][:]=self.sky[int(np.rad2deg(ROT_i)%359)][:]/255    

            for j in range (HALFRES):
                n=(HALFRES / (HALFRES- j))/cos2
                #x,y= self.POSX*0.1+cos*n,self.POSY*0.1 +sin*n 
                x,y= POSY*0.1+cos*n,-POSX*0.1 +sin*n                                          #!!!WARNING! REVERSE X AND Y FROM PLAYER MOVEMENT! y=-PLAYER POSISTION ON Y!

                gx,gy=int(x*1%1*100),int(y*1%1*100)                                                     #gx,gy = ground x and ground y  HERE YOU CAN ADJUST THE RESOLUTION SCALE
                shader=0.2+0.8*(1-j/HALFRES)                                              
                frame[i][HALFRES*2-j-1]=shader*floor[gx][gy]/255
        return frame

    def Update(self,player): 
        self.LoadFrames(player)
        self.LoadSurface()
        pass
