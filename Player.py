import pygame as pg 
import math

from Settings import *
from Map import*

class Player:
    def __init__(self,game,map):
        self.game=game
        self.speed=0.1*self.game.DELTA_TIME
        self.pos=(10,60)
        self.posx,self.posy=self.pos
        
        self.angle=0
        self.FOV=math.pi/3
        self.HFOV=self.FOV/2
        self.forward=False

        self.curmap=map

        
    
    def draw(self):
        
        pg.draw.circle(self.game.DISPLAY,(255,0,0),(int(self.posx),int(self.posy)),1)
        pg.draw.line(self.game.DISPLAY,'yellow',(self.posx*50,self.posy*50),(self.posx*50+SCREEN_WIDTH,self.posy*50+SCREEN_WIDTH),2)
        pass

    def move(self):
        keys=pg.key.get_pressed()
        #self.map_collision(self.posx,self.posy)
        
        sin_a=math.sin(self.angle)
        cos_a=math.cos(self.angle)

        dx,dy=0,0
        self.speed=0.1*self.game.DELTA_TIME
        if keys[pg.K_w]:
            dx+=self.speed*cos_a
            dy+=self.speed*sin_a
        if keys[pg.K_s]:
            dx+=-self.speed*cos_a
            dy+=-self.speed*sin_a
        if keys[pg.K_a]:
            dx+=self.speed*sin_a
            dy+=-self.speed*cos_a
        if keys[pg.K_d]:
            dx+=-self.speed*sin_a
            dy+=self.speed*cos_a

        self.posx+=dx
        self.posy+=dy
        # if keys[pg.K_w]:
        #     self.forward=True
        #     dx+=-math.sin(self.angle)*self.speed*self.game.DELTA_TIME
        #     dy+=math.cos(self.angle)*self.speed*self.game.DELTA_TIME
        # if keys[pg.K_s]:
        #     self.forward=False
        #     dx-=-math.sin(self.angle)*self.speed*self.game.DELTA_TIME
        #     dy-=math.cos(self.angle)*self.speed*self.game.DELTA_TIME
        #print(self.check_wall(self.posx,self.posy))
        #self.map_collision(dx,dy)

        if keys[pg.K_LEFT]:self.angle-=0.01*self.game.DELTA_TIME
        if keys[pg.K_RIGHT]:self.angle+=0.01*self.game.DELTA_TIME
        self.angle%=math.tau

    def check_wall(self,x,y):
        return(x,y) not in self.game.map.worldmap
    
    def map_collision(self,dx,dy):
        if self.check_wall(int(self.posx+dx),int(self.posy)):
            self.posx+=dx
        if self.check_wall(int(self.posx),int(self.posy+dy)):
            self.posy+=dy
        # column=int(self.posx/self.curmap.tile_size)
        # row=int(self.posy/self.curmap.tile_size)
        # square=row*self.curmap+column
        # if self.curmap.get_map()[square]=='#':
        #     if self.forward:
        #         self.posx-=-math.sin(self.angle)*self.speed*DELTA_TIME
        #         self.posy-=math.cos(self.angle)*self.speed*DELTA_TIME
        #     else:
        #         self.posx+=-math.sin(self.angle)*self.speed*DELTA_TIME
        #         self.posy+=math.cos(self.angle)*self.speed*DELTA_TIME

    @property
    def get_pos(self):
        return self.posx,self.posy
    @property
    def get_angle(self):
        return self.angle
    @property
    def get_map_pos(self):
        return int(self.posx),int(self.posy)
    
    def update(self):
        #self.map_collision()
        self.move()
        #self.mousecontrol()    
        pass

if __name__=='__main__':
    print("Player Class")