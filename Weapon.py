from collections import deque
import pygame as pg

from SpriteRenderer import AnimatedSprite

class Weapon(AnimatedSprite):
    def __init__(self, game, path='Assets/Sprites/Weapons', scale=0.5,animation_time=60,damage=10):
        super().__init__(game=game, path=path, scale=scale,animation_time=animation_time)
        self.images=deque(
            [pg.transform.smoothscale(img,(self.image.get_width()*scale,self.image.get_height()*scale))
             for img in self.images])
        self.pos=(self.game.SCREEN_WIDTH//2+self.images[0].get_width()//2,self.game.SCREEN_HEIGHT-self.images[0].get_height())
        self.attack=False
        self.frame_counter=0
        self.num_images=len(self.images)
        self.ticks=pg.time.get_ticks()
        self.damage=damage
    
    def Attack(self):
        if self.attack:
            timer=pg.time.get_ticks()
            if timer-self.ticks>self.animation_time:
                self.ticks=timer
                self.images.rotate(-1)
                self.image=self.images[0]
                self.frame_counter+=1
                if self.frame_counter==self.num_images:
                    self.attack=False
                    self.frame_counter=0
    
    def Update(self):
        self.game.DISPLAY.blit(self.images[0],self.pos)
        self.Attack()
    
    @property
    def GetAttack(self): return self.attack
