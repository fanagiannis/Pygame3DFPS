import pygame as pg
from Map import*


class Dungeon:
    def __init__(self,game,map):
        self.game=game
        self.map=Map(self.game,map)

    def Update(self):
        self.map.Update()