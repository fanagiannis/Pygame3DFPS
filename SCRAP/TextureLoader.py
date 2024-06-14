import pygame as pg

class TextureLoader():
    def __init__(self,game):
        self.game=game
        self.TEXTURE_SIZE=256
        self.TEXTURE_RES=(self.TEXTURE_SIZE,self.TEXTURE_SIZE)
        self.walltextures=self.LoadWalls()
        pass
    def GetTexture(self,path):
        texture=pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,self.TEXTURE_RES)
    def LoadWalls(self):
        return{
            1: self.GetTexture('Assets/Textures/1.png'),
            2: self.GetTexture('Assets/Textures/2.png'),
            3: self.GetTexture('Assets/Textures/3.png'),
            4: self.GetTexture('Assets/Textures/4.png'),
            5: self.GetTexture('Assets/Textures/5.png'),
        }
    def update(self):
        pass