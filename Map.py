import pygame as pg
import math

from Settings import*
from Maps import*

class Map:
    def __init__(self,game,map):
        self.game=game
        self.mini_map=map
        self.worldmap={}
        self.get_map()
    
    def draw(self):
        [pg.draw.rect(DISPLAY,'darkgray',(pos[0]*100,pos[1]*100,100,100),2)
        for pos in self.worldmap]
        # for row in range(self.size):
        #     for column in range(self.size):
        #         square= row*self.size + column
        #         rect=(column*self.tile_size,row*self.tile_size,self.tile_size,self.tile_size)
        #         pg.draw.rect(DISPLAY,(100,100,100) if self.map[square]=='#' else (0,0,0),rect)
    def get_map(self):
        for j,row in enumerate(self.mini_map):
            for i,value in enumerate(row):
                if value:
                    self.worldmap[(i,j)]=value
    
    def update(self):
        self.draw()

if __name__=='__main__':
    print("Map Class")
