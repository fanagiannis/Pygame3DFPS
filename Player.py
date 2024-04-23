import pygame as pg 
import math

from Settings import *

class Player:
    def __init__(self):
        self.speed=2
        self.pos=((int(SCREEN_WIDTH/2)/2),(int(SCREEN_WIDTH/2)/2))
        self.posx,self.posy=self.pos
        
        self.depth=30
        self.angle=math.pi
        self.FOV=math.pi/3
        self.HFOV=self.FOV/2
    
    def draw(self):  
        self.look()
        pg.draw.circle(DISPLAY,(255,0,0),(int(self.posx),int(self.posy)),8)
        pass
    
    def look(self):
        self.TARGET_X=self.posx-math.sin(self.angle)*self.depth
        self.TARGET_Y=self.posy+math.cos(self.angle)*self.depth
        pg.draw.line(DISPLAY,(0,255,0),(self.posx,self.posy),(self.TARGET_X,self.TARGET_Y),3)

    def move(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_a]:self.angle-=0.1
        if keys[pg.K_d]:self.angle+=0.1

        if keys[pg.K_w]:
            self.posx+=-math.sin(self.angle)*self.speed
            self.posy+=math.cos(self.angle)*self.speed
        if keys[pg.K_s]:
            self.posx-=-math.sin(self.angle)*self.speed
            self.posy-=math.cos(self.angle)*self.speed
        pass

    def get_pos(self):
        return self.posx,self.posy
    
    def update(self):
        self.move()
        pass

P=Player()