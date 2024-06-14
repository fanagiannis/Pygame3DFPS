import pygame as pg 
import numpy as np

class Sprite():
    def __init__(self,game,spritepath,pos):
        self.game=game
        self.sprite=pg.image.load(spritepath).convert_alpha()
        self.sprite_size=np.asarray(self.sprite.get_size())
        self.pos=np.array(pos)
        pass
    def Calculation(self):
        pass

    
    
    def Draw(self):
        pass# mouse_pos=pg.mouse.get_pos()
        # angle=np.arctan((self.mapposy-self.game.player.posy)/(self.mapposx-self.game.player.posx))
        # if abs(self.game.player.posx+np.cos(angle)-self.mapposx)> abs(self.game.player.posx-self.mapposx):
        #     angle=(angle-np.pi)%(2*np.pi)
        # anglediff=(self.game.player.angle-angle)%(2*np.pi)
        # if anglediff>11*np.pi/6 or anglediff < np.pi/6:
        #     dist=np.sqrt((self.game.player.posx-self.mapposx)**2+(self.game.player.posy-self.mapposy)**2)
        #     cos2=np.cos(anglediff)
        #     self.scale=10*min(1/dist,2)#/cos2
        #     vert=300*self.scale - self.scale*self.sprite_size[1]/2
        #     hor=400-800*np.sin(anglediff) - self.scale*self.sprite_size[0]/2
        # #self.scale=self.sprite_size*abs((mouse_pos[1]-300)/300)
        #     self.surf=pg.transform.scale(self.sprite,self.scale*self.sprite_size)
        #     #self.game.Raycaster.objects_to_render.append(self.surf)
        #     self.game.DISPLAY.blit(self.surf,(hor,vert))

        # return dist,self.surf,

    def Update(self):
        self.Draw()
        pass