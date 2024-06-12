import pygame as pg

from Settings import *
from Player import *
from Map import *
from Raycaster import *
from Floorcaster import *

class Game:
    def __init__(self):
        pg.mouse.set_visible(False)
        self.running=True
        self.LoadMaps()
        self.player=Player(self.selectedmap)
        self.RayCaster=Raycaster(self)
        self.FloorCaster=Floorcaster()
        pass

    def Run(self):
        pg.init()
        while self.running:
            self.Events()
            
            pg.display.set_caption(f'{CLOCK.get_fps():.1f}')
            pg.display.flip()
            
            DELTA_TIME=CLOCK.tick(FPS)
            self.Update()
            pg.display.update()
            DISPLAY.fill((0,0,0))

    def Events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT :
                pg.quit()    
    
    def LoadMaps(self):
        self.map=Map(self,MAP)
        #self.map2=Map(self,MAP2)
        #self.map_m=Map(MAP_MED)
        self.selectedmap=self.map

    def Update(self):
        self.player.update()
        self.RayCaster.update()
        #self.map.draw()
        
        
        

if __name__=='__main__':
    print("Game Class")
