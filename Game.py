import pygame as pg

from Settings import *

from Scripts.Map import *
from Scripts.Player import *
from Scripts.SoundMixer import *
from Scripts.MainMenu import *

from Scripts.Raycasting.SpriteLoader import *
from Scripts.Raycasting.Raycaster import *
from Scripts.Raycasting.TextureRenderer import*
from Scripts.Raycasting.Floorcaster import * 
from Scripts.Arsenal.Weapon import*
from Scripts.Arsenal.Arsenal import*
from Scripts.Enemies.Pathfinding import *


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
        self.map_selected=None  
        self.menu=MainMenu(self)

    def Menu_Objects(self):
        self.Soundmixer=SoundMixer()
        self.player = Player(self)
        self.map_rat_king = Map(self, MAP_RAT_KING, difficulty=1)
        self.map_legion = Map(self, MAP_LEGION, difficulty=2)

    def Game_Objects(self):
        self.running=True
        self.map = self.map_selected
        self.Texturerenderer = TextureRenderer(self)
        self.Raycaster = RayCaster(self)
        self.Floorcaster=Floorcaster(self)
        self.Soundmixer=SoundMixer()
        self.Pathfinding=PathFinding(self)
        self.Arsenal=Arsenal(self)
        self.Sprites=SpriteLoader(self,self.Arsenal,self.Raycaster)
        
    def MainMenu(self):
        icon = pg.image.load('Assets/Sprites/Animated/Skeleton/Idle/1.png')
        pg.display.set_icon(icon)
        pg.display.set_caption("The Elder Falls")
        self.Menu_Objects()
        self.Soundmixer.PlayMenuTheme()
        self.menu.Update()

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
        self.ReturnMainMenu()
        pg.display.flip()
        self.DELTA_TIME=self.CLOCK.tick(self.FPS)
        
    def ShowFPS(self):
        pg.display.set_caption(f'{self.CLOCK.get_fps():.1f}')

    def Restart(self):
        self.Game_Objects()
        self.Run()

    def ReturnMainMenu(self):
        if self.player.vitalitystats.IsDead or self.map.GetClear: 
            if self.player.vitalitystats.IsDead:
                text_Death=FONT_DEATH.render("YOU DIED",False,'red') 
                self.DISPLAY.blit(text_Death,(self.SCREEN_WIDTH//2-100,self.SCREEN_HEIGHT//2))
            elif self.map.GetClear: 
                text_win=FONT_DEATH.render("DUNGEON CLEARED",False,'orange') 
                self.DISPLAY.blit(text_win,(self.SCREEN_WIDTH//2-200,self.SCREEN_HEIGHT//2+100))
            self.timer+=self.DELTA_TIME
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
        

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.MainMenu() 


