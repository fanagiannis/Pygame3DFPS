import pygame as pg 

class Player():
    def __init__(self,game):
        self.game=game
        self.SPEED=1*self.game.DELTA_TIME
        self.pos=(self.game.SCREEN_WIDTH//2,self.game.SCREEN_HEIGHT//2)
        self.posx,self.posy=self.pos
        print("Player Created!")
        pass
    
    def Move(self):
        pass
    
    def Draw(self):
        pg.draw.circle(self.game.DISPLAY,(255,0,255),(int(self.posx),int(self.posy)),3)
        print(self.posx,self.posy)
        pass    
    
    def Update(self):
        self.Draw()
        pass