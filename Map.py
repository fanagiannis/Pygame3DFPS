import pygame as pg
import math

from Settings import*
from Maps import*

class Map:
    def __init__(self,map):
        self.map=map
        self.map_open=False
        self.size=int(math.sqrt((self.map.__len__())))
        self.tile_size=int((SCREEN_WIDTH/2)/(self.size))
        print(self.size)
    def draw(self):
        for row in range(self.size):
            for column in range(self.size):
                square= row*self.size + column
                rect=(column*self.tile_size,row*self.tile_size,self.tile_size,self.tile_size)
                pg.draw.rect(DISPLAY,(100,100,100) if self.map[square]=='#' else (0,0,0),rect)
    def map_control(self):
        pass
    def get_map(self):
        return self.map
    def update(self):
        self.map_control()
        if self.map_open:
            self.draw()

if __name__=='__main__':
    print("Map Class")
