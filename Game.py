import pygame as pg

from Settings import *
from Player import *
from Map import *
from Raycaster import *
from Floorcaster import *
from TextureLoader import *

class Game:
    def __init__(self):
        
        self.DISPLAY=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.running=True
        self.clock=pg.time.Clock()
        self.DELTA_TIME=self.clock.tick(FPS)
        self.map=Map(self,MAP_SMALL)
        #self.LoadMaps()
        self.player=Player(self,self.map)
        self.RayCaster=Raycaster(self,80,self.player,self.map)
        self.FloorCaster=Floorcaster(self)
        self.Textureloader=TextureLoader()
        
    def Run(self):
        pg.init()
        while self.running:
            self.Events()
            self.draw()
            self.Update()

    def draw(self):
        self.DISPLAY.fill('black')
        self.player.draw()
        self.map.draw()

    def Events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT :
                pg.quit()    
    
    def GetMap(self):
        return self.map

    def Update(self):
        pg.display.flip()
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')  
        self.DELTA_TIME=self.clock.tick(FPS)
        #self.FloorCaster.Update(self.player)
        #self.RayCaster.update()
        #self.map.update()
        self.player.update()
        #self.Textureloader.update()
        pass
        

if __name__=='__main__':
    print("Game Class")
