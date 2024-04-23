import pygame as pg

from Settings import*

MAP_SIZE=16

MAP_DEF=(
    "################"
    "#              #"
    "#              #"
    "#              #"
    "#              #"
    "#   #          #"
    "#              #"
    "################"
    "#              #"
    "#              #"
    "#              #"
    "#              #"
    "#              #"
    "#              #"
    "#              #"
    "################"
)

class Map:
    def __init__(self,size,map):
        self.size=size
        self.map=map
        self.tile_size=int((SCREEN_WIDTH)/self.size)
    def draw(self):
        for row in range(self.size):
            for column in range(self.size):
                square= row*self.size + column
                rect=(column*self.tile_size,row*self.tile_size,self.tile_size-2,self.tile_size-2)
                pg.draw.rect(DISPLAY,(200,200,200) if self.map[square]=='#' else (100,100,100),rect)
