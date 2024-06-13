import pygame as pg 
import math

class Player():
    def __init__(self,game):
        self.game=game
        self.SPEED=0.1
        self.ROT_SPEED=0.01
        self.ANGLE=0
        self.FOV=math.pi/4
        self.pos=(self.game.SCREEN_WIDTH//2,self.game.SCREEN_HEIGHT//2)
        self.posx,self.posy=self.pos
        print("Player Created!")
        pass
    
    def Move(self):
        self.SPEED=0.1*self.game.DELTA_TIME
        self.ROT_SPEED=0.001*self.game.DELTA_TIME
        keys=pg.key.get_pressed()
        dx,dy=0,0
        if keys[pg.K_d]: self.ANGLE+=self.ROT_SPEED*self.game.DELTA_TIME
        if keys[pg.K_a]: self.ANGLE-=self.ROT_SPEED*self.game.DELTA_TIME
        if keys[pg.K_w] : 
            dx= math.cos(self.ANGLE) *self.SPEED
            dy= math.sin(self.ANGLE) *self.SPEED
            
        if keys[pg.K_s] : 
            dx= -math.cos(self.ANGLE) * self.SPEED
            dy= -math.sin(self.ANGLE) * self.SPEED

        if not self.game.map.check_collision(self.posx+dx,self.posy+dy):
            self.posx+=dx
            self.posy+=dy   
        
        
        
        pass
    
    def Draw(self):
        #FOV
        pg.draw.line(self.game.DISPLAY,(0,255,0),(self.posx,self.posy),(int(self.posx-math.sin(self.ANGLE-self.FOV/2)*50),int(self.posy+math.cos(self.ANGLE-self.FOV/2)*50)),1)
        pg.draw.line(self.game.DISPLAY,(0,255,0),(self.posx,self.posy),(int(self.posx+math.sin(self.ANGLE+self.FOV/2)*50),int(self.posy-math.cos(self.ANGLE+self.FOV/2)*50)),1)
        #pg.draw.line(DISPLAY,(0,255,0),(self.get_pos()),(int(self.posx-math.sin(self.angle+self.HFOV)*50),int(self.posy+math.cos(self.angle+self.HFOV)*50)),1)
        
        pg.draw.circle(self.game.DISPLAY,(255,0,255),(int(self.posx),int(self.posy)),3)
        pass    
    
    def Update(self):
        self.Move()
        self.Draw()
        
        pass
