import pygame as pg 
import math

from Settings import *
from Map import*

class Player:
    def __init__(self,game,map):
        self.game=game
        self.speed=0.1
        self.pos=((int(SCREEN_WIDTH/2)/2),(int(SCREEN_WIDTH/2)/2))
        self.posx,self.posy=self.pos
        
        self.angle=math.pi
        self.FOV=math.pi/3
        self.HFOV=self.FOV/2
        self.forward=False

        self.curmap=map
        print(self.game.map.worldmap)

        
    
    def draw(self):
        self.look()  
        pg.draw.circle(DISPLAY,(255,0,0),(int(self.posx),int(self.posy)),8)
        pass
    
    def look(self):
        #pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle-self.HFOV)*50),int(self.posy+math.cos(self.angle-self.HFOV)*50)),1)
        #pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle+self.HFOV)*50),int(self.posy+math.cos(self.angle+self.HFOV)*50)),1)
        pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle)*50),int(self.posy+math.cos(self.angle)*50)),1)

    def move(self):
        keys=pg.key.get_pressed()
        #self.map_collision(self.posx,self.posy)
        

        dx,dy=0,0
        
        if keys[pg.K_w]:
            self.forward=True
            dx+=-math.sin(self.angle)*self.speed*self.game.DELTA_TIME
            dy+=math.cos(self.angle)*self.speed*self.game.DELTA_TIME
        if keys[pg.K_s]:
            self.forward=False
            dx-=-math.sin(self.angle)*self.speed*self.game.DELTA_TIME
            dy-=math.cos(self.angle)*self.speed*self.game.DELTA_TIME
        #print(self.check_wall(self.posx,self.posy))
        self.map_collision(dx,dy)

        if keys[pg.K_a]:self.angle-=0.01*self.game.DELTA_TIME
        if keys[pg.K_d]:self.angle+=0.01*self.game.DELTA_TIME
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
        pass

    def get_pos(self):
        return self.posx,self.posy

    def get_angle(self):
        return self.angle
    
    def get_map_pos(self):
        return int(self.posx),int(self.posy)
    
    def update(self):
        #self.map_collision()
        self.move()
        #self.mousecontrol()
        self.draw()
        pass

if __name__=='__main__':
    print("Player Class")