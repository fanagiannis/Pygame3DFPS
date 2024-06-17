import pygame as pg

class Hitbox():
    def __init__(self,game,pos,size=(50,50),active=True):
        self.game=game
        self.posx,self.posy=pos
        self.sizex,self.sizey=size
        self.active=active
        # self.rect=pg.Rect((self.posx*100,self.posy*100,self.sizex,self.sizey))
    
    def Draw(self):
        self.rect=pg.Rect((self.posx*100,self.posy*100,self.sizex,self.sizey))
        pg.draw.rect(self.game.DISPLAY,'blue',self.rect,1)
    
    def SetActive(self): self.active=True
    def ResetActive(self): self.active=False
    
    def Update(self):
        if(self.active):
            print("active")
            self.Draw()