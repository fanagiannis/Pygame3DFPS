import pygame as pg

from Settings import*

MAP_SIZE=8
MAP_DEF=(
    "########"
    "#      #"
    "#      #"
    "#      #"
    "#      #"
    "#   #  #"
    "#      #"
    "########"
)


class Map:
    def __init__(self,size,map):
        self.size=size
        self.map=map
        self.tile_size=int((SCREEN_WIDTH)/(self.size*2))
    def draw(self):
        for row in range(self.size):
            for column in range(self.size):
                square= row*self.size + column
                rect=(column*self.tile_size,row*self.tile_size,self.tile_size-1,self.tile_size-1)
                pg.draw.rect(DISPLAY,(100,100,100) if self.map[square]=='#' else (0,0,0),rect)
    def get_map(self):
        return self.map

map_default=Map(MAP_SIZE,MAP_DEF)
