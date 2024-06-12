import pygame as pg 
import math

from Settings import *
from Map import*

class Player:
    def __init__(self,map):
        self.speed=100*DELTA_TIME
        self.rot_speed=0.1*DELTA_TIME
        self.pos=((int(SCREEN_WIDTH/2)/2),(int(SCREEN_WIDTH/2)/2))
        self.posx,self.posy=self.pos
        
        self.angle=0#math.pi
        self.FOV=math.pi/3
        self.HFOV=self.FOV/2

        self.curmap=map

        
    
    def draw(self):
        self.look()  
        pg.draw.circle(DISPLAY,(255,0,0),(int(self.posx),int(self.posy)),3)
        pass
    
    def look(self):
        pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle-self.HFOV)*50),int(self.posy+math.cos(self.angle-self.HFOV)*50)),1)
        pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle+self.HFOV)*50),int(self.posy+math.cos(self.angle+self.HFOV)*50)),1)

    def move(self):
        self.speed=1*DELTA_TIME
        self.rot_speed=0.01*DELTA_TIME
        dx,dy=0,0
        keys=pg.key.get_pressed()

        if keys[pg.K_a]:self.angle-=self.rot_speed
        if keys[pg.K_d]:self.angle+=self.rot_speed

        if keys[pg.K_w]: 
            dx+=-math.sin(self.angle)*self.speed
            dy+=math.cos(self.angle)*self.speed
        if keys[pg.K_s]:
            dx-=-math.sin(self.angle)*self.speed
            dy-=math.cos(self.angle)*self.speed

        next_posx=self.posx+dx
        next_posy=self.posy+dy

        if not self.curmap.check_collision(next_posx, next_posy):
            self.posx = next_posx
            self.posy = next_posy    
    
    def get_pos(self):
        return self.posx,self.posy

    def get_angle(self):
        return self.angle
    
    def get_map_pos(self):
        return int(self.posx),int(self.posy)
    
    def update(self):
        self.move()
        self.draw()
        pass

if __name__=='__main__':
    print("Player Class")