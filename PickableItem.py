import pygame as pg

from SpriteRenderer import *
class PickableItem(Sprite):
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=..., scale=0.7, shift=0.27, castlight=False):
        super().__init__(game, path, pos, scale, shift, castlight)
        self.picked=False
        self.x,self.y=pos
        self.rect=pg.Rect((self.x-0.15)*100,(self.y-0.15)*100,self.x+25,self.y+25)
    def Update(self):
        if self.rect.colliderect(self.game.player.collisionbox):
            print(self.picked)
            #self.action
            self.picked=True
        if not self.picked:
            self.get_sprite()
        #return super().Update()
