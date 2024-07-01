import pygame as pg

from SpriteRenderer import *
from Weapon import*

class PickableItem(Sprite):
    def __init__(self,game,type, path='resources/sprites/static_sprites/candlebra.png', pos=..., scale=0.7, shift=0.27, castlight=False):
        super().__init__(game, path, pos, scale, shift, castlight)
        self.game=game
        self.type=type
        self.picked=False
        self.x,self.y=pos
        self.rect=pg.Rect((self.x-0.15)*100,(self.y-0.15)*100,self.x+25,self.y+25)
    def Update(self):
        if self.rect.colliderect(self.game.player.collisionbox):
            self.Pickup()
            if not self.picked:
                self.game.DISPLAY.fill('yellow')
            #self.action
            self.picked=True
        if not self.picked:
            self.get_sprite()
        #return super().Update()
    def Pickup(self):
        self.game.Arsenal.PickupWeapon(self.type)