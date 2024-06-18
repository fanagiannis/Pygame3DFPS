import pygame as pg
import time

from SpriteRenderer import AnimatedSprite

class Enemy(AnimatedSprite):
    def __init__(self, game, Level, Value, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.Level=Level
        self.posx,self.posy=pos
        self.Value=Value+10*self.Level
        self.HP=50+10*self.Level
        self.Damage=20+10*self.Level
        self.visionradius=200
        self.IsDead=False

        self.hitbox=pg.Rect((self.posx-0.15)*100,(self.posy-0.15)*100,self.posx+25,self.posy+25)
       
    
    def TakeDamage(self):
        self.HP=self.HP-(self.game.player.DealDamage-2*self.Level)
        return (self.game.player.DealDamage-2*self.Level)
    
    def Death(self):
        if self.HP<=0: self.IsDead=True
        else: self.IsDead=False
        return self.IsDead
    
    def Draw(self):
        pg.draw.circle(self.game.DISPLAY, 'red', (self.posx*100,self.posy*100), 15)
        pg.draw.rect(self.game.DISPLAY,'blue',self.hitbox,1)
    
    def Vision(self):
        self.vision=pg.draw.circle(self.game.DISPLAY, 'orange', (self.posx*100,self.posy*100), radius=self.visionradius,width=1)
        if self.vision.colliderect(self.game.player.collisionbox): print("Spotted")

    def Hit(self):
        if self.hitbox.colliderect(self.game.player.collisionbox):
           self.game.player.vitalitystats.TakeDamage(self.Damage)
        if self.game.player.hitbox.IsActive and self.hitbox.colliderect(self.game.player.hitbox.rect) :
            print(self.Damage)
            self.TakeDamage()

    def Update(self):
        super().Update()
        #DEBUG
        self.Vision()
        self.Hit()
        self.Draw()
       
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