import pygame as pg 
import math

from Settings import *

class Player:
    def __init__(self):
        self.speed=2
        self.pos=((int(SCREEN_WIDTH/2)/2),(int(SCREEN_WIDTH/2)/2))
        self.posx,self.posy=self.pos
        
        self.depth=300
        self.angle=math.pi
        self.FOV=math.pi/3
        self.HFOV=self.FOV/2
    
    def draw(self):  
        TARGET_X=self.posx-math.sin(self.angle)*self.depth
        TARGET_Y=self.posy+math.cos(self.angle)*self.depth
        pg.draw.line(DISPLAY,(0,255,0),(self.posx,self.posy),(TARGET_X,TARGET_Y),3)
        pg.draw.circle(DISPLAY,(255,0,0),(int(self.posx),int(self.posy)),8)
        pass

    def move(self):

        pass
    def update(self):
        pass

P=Player()