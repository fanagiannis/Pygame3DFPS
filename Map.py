import pygame as pg
import math

from Settings import*
from Maps import*

class Map:
    def __init__(self,map):
        self.mini_map=map
        self.map={}
        self.get_map()
        #self.size=int(math.sqrt((self.map.__len__())))
        #self.tile_size=int((SCREEN_WIDTH/2)/(self.size))
    def draw(self):
        [pg.draw.rect(DISPLAY,'darkgray',(pos[0]*100,pos[1]*100,100,100),2)
        for pos in self.map]
        # for row in range(self.size):
        #     for column in range(self.size):
        #         square= row*self.size + column
        #         rect=(column*self.tile_size,row*self.tile_size,self.tile_size,self.tile_size)
        #         pg.draw.rect(DISPLAY,(100,100,100) if self.map[square]=='#' else (0,0,0),rect)
    def get_map(self):
        for j,row in enumerate(self.mini_map):
            for i,value in enumerate(row):
                if value:
                    self.map[(i,j)]=value
    def update(self):
        self.draw()

if __name__=='__main__':
    print("Map Class")
