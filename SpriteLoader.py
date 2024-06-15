import pygame as pg

from SpriteRenderer import*

class SpriteLoader():
    def __init__(self,game):
        self.game=game
        self.player=self.game.player
        self.sprites=[]
        self.light_sprites=[]
        self.animated_sprites=[]

        #CREATE SPRITES
        self.StaticSprites()
        self.LightSprites()
        self.AnimatedSprites()

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

    def Update(self):
        [staticsprite.Update() for staticsprite in self.sprites]
        [lightsprite.Update() for lightsprite in self.light_sprites]
        [animsprite.Update() for animsprite in self.animated_sprites]
       