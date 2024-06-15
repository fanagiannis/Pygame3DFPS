import pygame as pg
import sys
from Settings import *
from Map import *
from Player import *
from Raycaster import *
from TextureRenderer import*
from Floorcaster import * 
from SpriteRenderer import *


class Game:
    def __init__(self):
        self.SCREEN_WIDTH=1600
        self.SCREEN_HEIGHT=900
        self.DISPLAY=pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.CLOCK=pg.time.Clock()
        self.FPS=60
        self.DELTA_TIME=1
        self.running=True
        print("Game Created!")
        pass

    def Game_Objects(self):
        self.map = Map(self,MAP)
        self.player = Player(self)
        self.Texturerenderer = TextureRenderer(self)
        self.Raycaster = RayCaster(self)
        self.Floorcaster=Floorcaster(self)
        self.Sprite1=Sprite(self,'Assets/Sprites/test.png')#,(5,5))
        self.Sprite2=Sprite(self,'Assets/Sprites/test.png',(5,5))
    
    def Run(self):
        self.Game_Objects()
        while True:
            self.Events()
            self.Update()

    def Events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT :
                pg.quit()    

    def Cycle(self): 
        self.ShowFPS()
        pg.display.update()
        pg.display.flip()
        self.DISPLAY.fill((0,0,0))
        self.DELTA_TIME=self.CLOCK.tick(self.FPS)
        
    def ShowFPS(self):
        pg.display.set_caption(f'{self.CLOCK.get_fps():.1f}')
        # fps = str(int(self.CLOCK.get_fps()))
        # font = pg.font.SysFont('Monospace Regular', 30)
        # text_surface = font.render(fps, False, 'yellow')
        # self.DISPLAY.blit(text_surface,(0,0))

    def Update(self):
        self.DISPLAY.fill('black')
        #self.map.draw()
        self.Floorcaster.Update()
        self.Texturerenderer.Update()
        self.player.Update()
        self.Raycaster.update()
        self.Sprite1.update()
        self.Sprite2.update()
        self.Cycle()


