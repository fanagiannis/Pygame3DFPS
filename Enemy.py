import pygame as pg
import time

from SpriteRenderer import AnimatedSprite

class Enemy(AnimatedSprite):
    def __init__(self, game, Level, Value, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.Level=Level
        self.Value=Value+10*self.Level
        self.HP=50+10*self.Level
        self.Damage=20+10*self.Level
        self.IsDead=False
    
    def TakeDamage(self):
        self.HP=self.HP-(self.game.player.DealDamage-2*self.Level)
        return (self.game.player.DealDamage-2*self.Level)
    
    def Death(self):
        if self.HP<=0: self.IsDead=True
        else: self.IsDead=False
        return self.IsDead

    def Update(self):
        super().Update()
        #DEBUG
        keys=pg.key.get_pressed()
        if keys[pg.K_r]:
            self.TakeDamage()
            print(self.TakeDamage())
            time.sleep(0.1)
        #DEBUG
        if self.Death(): 
            self.game.player.stats.GainXP(self.Value) 
            print("dead")
            self.game.Sprites.enemies.remove(self)
        pass