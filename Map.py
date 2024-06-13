import pygame as pg

from Settings import*

_=False
MAP=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,1,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

MAP2=[
    [1,1,1,1,1,1,1],
    [1,_,_,_,_,_,1],
    [1,_,3,_,_,_,1],
    [1,_,_,_,4,_,1],
    [1,_,2,_,_,_,1],
    [1,_,_,_,5,_,1],
    [1,_,1,_,_,_,1],
    [1,_,_,_,_,_,1],
    [1,1,1,1,1,1,1],
]

class Map:
    def __init__(self,game,map):
        self.game=game
        self.mini_map=map
        self.world_map={}
        self.rows=len(self.mini_map)
        self.cols=len(self.mini_map[0])
        self.get_map()
        self.tilesize=100
        
    def draw(self):
        [pg.draw.rect(DISPLAY,(100,100,100),(pos[0] * self.tilesize, pos[1] * self.tilesize, self.tilesize, self.tilesize)) for pos in self.world_map]

    def get_map(self):
        for j,row in enumerate(self.mini_map):
            for i,value in enumerate(row):
                if value:
                    self.world_map[(i,j)]=value

    def check_collision(self,x,y):
        tile_x,tile_y = int(x//self.tilesize),int(y//self.tilesize)
        if 0 <= tile_x < self.cols and 0 <= tile_y < self.rows:
            return self.mini_map[tile_y][tile_x] != 0
        return False
    
    @property
    def Mapsize(self):
        return self.rows*self.cols

    def Update(self):
        self.get_map()
        self.draw()

if __name__=='__main__':
    print("Map Class")
