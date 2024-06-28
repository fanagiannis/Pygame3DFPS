import pygame as pg

from SpriteRenderer import*
from Enemy import *

class SpriteLoader():
    def __init__(self,game):
        self.game=game
        self.player=self.game.player
        self.sprites=[]
        self.light_sprites=[]
        self.animated_sprites=[]
        self.enemies=[]
        self.enemies_pos={}
        #CREATE SPRITES
        #self.StaticSprites()
        #self.LightSprites()
        #self.AnimatedSprites()
        self.Enemies()

    def Create_Sprite(self,Sprite):
        self.sprites.append(Sprite)

    def StaticSprites(self):
        Skeleton=Sprite(self.game,'Assets/Sprites/test.png')
        self.sprites.append(Skeleton)

    def LightSprites(self):
        LightSkeleton=LightSource(self.game,'Assets/Sprites/test.png',(5,5))
        self.light_sprites.append(LightSkeleton)

    def AnimatedSprites(self):
        Rat=AnimatedSprite(self.game,'Assets/Sprites/Animated/1.png',(10,10))
        self.animated_sprites.append(Rat)
    
    def Enemies(self):
        rat=Rat(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=(10,5),Level=1,Value=100,HP=100,scale=0.5)
        self.enemies.append(rat)
        skeleton=Skeleton(self.game,path='Assets/Sprites/Animated/Skeleton/Idle/1.png',pos=(10,10),Level=5,Value=200,HP=200,scale=0.7)
        self.enemies.append(skeleton)
        wereboar= Wereboar(self.game,path='Assets/Sprites/Animated/Wereboar/Idle/1.png',pos=(12,12),Level=5,Value=200,HP=200,scale=0.7)
        self.enemies.append(wereboar)
        zombie= Zombie(self.game,path='Assets/Sprites/Animated/Zombie/Idle/1.png',pos=(5,5),Level=10,Value=500,HP=300,scale=0.7)
        self.enemies.append(zombie)

    def Update(self):
        self.enemies_pos= {enemy.map_pos for enemy in self.enemies if not enemy.IsDead}
        [staticsprite.Update() for staticsprite in self.sprites]
        [lightsprite.Update() for lightsprite in self.light_sprites]
        [animsprite.Update() for animsprite in self.animated_sprites]
        [enemy.Update() for enemy in self.enemies]
        
       