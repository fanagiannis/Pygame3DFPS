import pygame as pg

from Settings import *
from Player import *
from Map import *
from Raycaster import *
from Floorcaster import *

class Game:
    def __init__(self):
        self.running=True
        self.LoadMaps()
        self.player=Player(self.selectedmap)
        self.RayCaster=Raycaster(80,self.player,self.map_s)
        self.FloorCaster=Floorcaster()
        pass

    def Run(self):
        pg.init()
        while self.running:
            self.Events()
            pg.display.set_caption(f'{CLOCK.get_fps():.1f}')
            pg.display.flip()
            DISPLAY.fill((0,0,0))
            DELTA_TIME=CLOCK.tick(FPS)
            self.Update()
            pg.display.update()

    def Events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT :
                pg.quit()    
    
    def LoadMaps(self):
        self.map_s=Map(MAP_SMALL)
        self.map_m=Map(MAP_MED)
        self.selectedmap=self.map_s

    def Update(self):
        self.FloorCaster.Update(self.player)
        self.RayCaster.update()
        self.map_s.update()
        self.player.update()
        

if __name__=='__main__':
    print("Game Class")
