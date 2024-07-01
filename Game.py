import pygame as pg
import sys
from Settings import *
from Map import *
from Player import *
from Raycaster import *
from TextureRenderer import*
from Floorcaster import * 
from SpriteLoader import *
from SoundMixer import *
from Pathfinding import *
from Weapon import*
from Arsenal import*

from MainMenu import *

class Game:
    def __init__(self):
        self.SCREEN_WIDTH=1600
        self.SCREEN_HEIGHT=900
        self.DISPLAY=pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT),pg.SRCALPHA)
        self.CLOCK=pg.time.Clock()
        self.FPS=60
        self.DELTA_TIME=1
        self.running=True
        self.timer=0
        print("Game Created!")
        self.menu=MainMenu(self)
        pass

    def Game_Objects(self):
        self.running=True
        self.player = Player(self)
        self.map_rat_king = Map(self, MAP_RAT_KING, difficulty=1)
        self.map_legion = Map(self, MAP_LEGION, difficulty=2)
        self.map = self.map_rat_king
        self.Texturerenderer = TextureRenderer(self)
        self.Raycaster = RayCaster(self)
        self.Floorcaster=Floorcaster(self)
        self.Soundmixer=SoundMixer()
        self.Pathfinding=PathFinding(self)
        self.Arsenal=Arsenal(self)
        self.Sprites=SpriteLoader(self,self.Arsenal,self.Raycaster)
        
    def MainMenu(self):
        self.Game_Objects()
        self.Soundmixer.PlayMenuTheme()
        self.menu.Update()
        pass

    def Run(self):
        self.Soundmixer.StopMenuTheme()
        self.Game_Objects()
        while self.running:
            self.Events()
            self.Update()
        self.Restart()

    def Events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT :
                pg.quit() 
            if self.player.vitalitystats.IsDead and pg.key.get_pressed()[pg.K_TAB]:
                self.running=False
            if self.map.GetClear and pg.key.get_pressed()[pg.K_TAB]:
                self.running=False
            if event.type==pg.KEYUP and not self.player.vitalitystats.IsDead:
                if event.key==pg.K_SPACE: 
                    self.player.hitbox.Activate()
                if event.key==pg.K_h:
                    self.player.Heal(self.player.vitalitystats.MagicPower)
                    


    def Cycle(self): 
        self.ShowFPS()
        #pg.display.update()
        pg.display.flip()
        #self.DISPLAY.fill((0,0,0,0))
        self.DELTA_TIME=self.CLOCK.tick(self.FPS)
        
    def ShowFPS(self):
        pg.display.set_caption(f'{self.CLOCK.get_fps():.1f}')

    def Restart(self):
        self.Game_Objects()
        self.Run()

    def ReturnMainMenu(self):
        if self.player.vitalitystats.IsDead or self.map.GetClear:
            
            self.timer+=self.DELTA_TIME
            print(self.timer)
            if self.timer>=200:
                self.running = False
                self.MainMenu() 
                self.timer=0

    def Update(self):
        self.DISPLAY.fill((0,0,0,0))
        self.Floorcaster.Update()
        self.Texturerenderer.Update()
        self.Arsenal.Update()
        self.player.Update()
        self.Raycaster.Update()
        self.Sprites.Update()     
        self.map.Update()
        #self.map.draw()
        self.Cycle()

        self.ReturnMainMenu()

if __name__ == '__main__':

    pg.init()
    game = Game()
    game.MainMenu() 


