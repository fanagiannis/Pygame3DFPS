import pygame as pg

class TextureLoader():
    def __init__(self):
        self.walltextures=self.LoadWalls()
        pass
    def GetTexture(self,path,resolution):
        texture=pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,resolution)
    def LoadWalls(self):
        return{
            1: self.GetTexture('Assets/Images/bricks.jpg',(300,300))
        }
    def update(self):
        pass