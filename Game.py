import pygame as pg

from numba import njit
from Player import *
from Map import *
from Raycaster import *
from Floorcaster import * 

class Game():
    def __init__(self):
        self.SCREEN_WIDTH=1600
        self.SCREEN_HEIGHT=900
        self.DISPLAY=pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.CLOCK=pg.time.Clock()
        self.FPS=60
        self.DELTA_TIME=0
        self.running=True
        print("Game Created!")
        pass
    
    def New_properties(self):
        self.map=Map(self,MAP2)
        self.player=Player(self,self.map)
        self.floorcaster=Floorcaster()
        self.raycaster=Raycaster(self)
        pass

    def Run(self):
        pg.init()
        self.New_properties()
        while self.running:
            self.Events()
            self.Cycle()
            self.Update()
        pass
    
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
        fps = str(int(self.CLOCK.get_fps()))
        font = pg.font.SysFont('Monospace Regular', 30)
        text_surface = font.render(fps, False, 'yellow')
        self.DISPLAY.blit(text_surface,(0,0))

    def Update(self):
        #self.map.Update()
        self.player.Update()
        self.floorcaster.Update()
        self.raycaster.Update()

if __name__=='__main__':
    game=Game()
    game.Run()