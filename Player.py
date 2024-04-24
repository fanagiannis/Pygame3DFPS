import pygame as pg 
import math

from Settings import *
from Map import*

class Player:
    def __init__(self):
        self.speed=1*DELTA_TIME
        self.pos=((int(SCREEN_WIDTH/2)/2),(int(SCREEN_WIDTH/2)/2))
        self.posx,self.posy=self.pos
        
        self.angle=math.pi
        self.FOV=math.pi/3
        self.HFOV=self.FOV/2
        self.forward=False

        self.curmap=map_s
    
    def draw(self):
        self.look()  
        pg.draw.circle(DISPLAY,(255,0,0),(int(self.posx),int(self.posy)),8)
        pass
    
    def look(self):
        pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle-self.HFOV)*50),int(self.posy+math.cos(self.angle-self.HFOV)*50)),3)
        pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle+self.HFOV)*50),int(self.posy+math.cos(self.angle+self.HFOV)*50)),3)

    def move(self):
        keys=pg.key.get_pressed()

        if keys[pg.K_a]:self.angle-=0.1
        if keys[pg.K_d]:self.angle+=0.1

        if keys[pg.K_w]:
            self.forward=True
            self.posx+=-math.sin(self.angle)*self.speed
            self.posy+=math.cos(self.angle)*self.speed
        if keys[pg.K_s]:
            self.forward=False
            self.posx-=-math.sin(self.angle)*self.speed
            self.posy-=math.cos(self.angle)*self.speed
        pass
    
    def map_collision(self):
        column=int(self.posx/self.curmap.tile_size)
        row=int(self.posy/self.curmap.tile_size)
        square=row*self.curmap.size+column
        if self.curmap.get_map()[square]=='#':
            if self.forward:
                self.posx-=-math.sin(self.angle)*self.speed
                self.posy-=math.cos(self.angle)*self.speed
            else:
                self.posx+=-math.sin(self.angle)*self.speed
                self.posy+=math.cos(self.angle)*self.speed

    def get_pos(self):
        return self.posx,self.posy

    def get_angle(self):
        return self.angle
    
    def get_map_pos(self):
        return int(self.posx),int(self.posy)
    
    def update(self):
        self.map_collision()
        self.move()
        #self.draw()
        pass

P=Player()