import pygame as pg

from SpriteRenderer import*
from Enemy import*

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
        enemy=Enemy(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=(5,5),Level=1,Value=100)
        self.enemies.append(enemy)
        enemy2=Enemy(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=(8,8),Level=1,Value=80)
        self.enemies.append(enemy2)

    def Update(self):
        self.enemies_pos= {enemy.map_pos for enemy in self.enemies if not enemy.IsDead}
        [staticsprite.Update() for staticsprite in self.sprites]
        [lightsprite.Update() for lightsprite in self.light_sprites]
        [animsprite.Update() for animsprite in self.animated_sprites]
        [enemy.Update() for enemy in self.enemies]
        
       