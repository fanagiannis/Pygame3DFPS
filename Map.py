import pygame as pg
import random

from PickableItem import *
from Enemy import *

#   WALL         [1]*64,
#   SPACE        [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],

_ = False

MAP_RAT_KING=[
    [1]*35,
    [4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2],
    [4,_,_,_,_,_,_,_,_,4,1,_,_,_,_,_,_,_,_,_,_,_,1,2,_,_,_,_,_,_,_,2],
    [4,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1,2,_,_,_,1,_,_,_,2],
    [4,_,_,_,_,_,_,_,_,4,1,_,_,_,2,2,2,2,_,_,_,_,1,2,_,_,_,1,_,_,_,2],
    [4,_,_,_,_,_,_,_,_,4,1,_,_,_,_,2,_,_,_,_,_,_,1,2,_,_,_,1,_,_,_,2],
    [4,_,_,_,_,_,_,_,_,4,1,_,_,_,_,_,_,_,_,_,_,_,1,2,_,_,_,_,_,_,_,2],
    [4,4,_,_,_,_,_,_,_,4,1,_,_,_,_,_,_,_,_,_,_,_,1,2,_,_,_,1,_,_,_,2],
    [4,4,4,4,4,4,_,_,4,4,1,_,_,_,2,2,_,_,_,1,1,1,1,2,_,_,_,_,_,_,_,2],
    [8,8,8,8,8,8,_,_,8,8,1,_,_,_,2,2,_,_,_,1,3,3,3,3,3,3,3,3,3,3,_,3],
    [8,_,_,_,_,_,_,_,_,8,1,_,_,_,_,_,_,_,_,1,3,_,_,_,_,_,_,_,_,_,_,3],
    [8,_,_,_,_,_,_,_,_,8,4,4,_,4,4,4,4,4,_,4,4,3,_,_,_,_,_,_,_,_,_,3],
    [8,_,_,_,8,8,_,_,_,8,4,_,_,_,_,_,_,_,_,_,4,3,_,_,_,2,2,2,_,_,_,3],
    [8,_,_,_,8,8,_,_,_,8,4,_,4,4,4,5,4,4,4,_,4,3,_,_,_,2,_,_,_,_,_,3],
    [8,_,_,_,8,8,_,_,8,8,4,_,4,_,_,_,_,_,4,_,4,3,_,_,_,_,_,_,_,_,_,3],
    [8,_,_,_,8,8,_,_,8,_,_,_,4,_,_,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,3],
    [8,_,_,_,8,8,_,_,_,_,4,_,_,_,_,_,_,_,_,_,4,3,_,_,_,_,2,_,_,_,_,1],
    [8,_,_,_,_,_,_,_,_,_,4,4,4,4,4,4,4,4,4,4,4,3,_,_,_,_,2,_,_,_,_,1],
    [8,_,_,_,_,_,_,_,_,_,_,4,_,_,_,_,_,_,_,_,4,3,_,_,_,_,_,_,_,_,_,1],
    [7,7,7,7,7,7,7,7,7,7,_,_,_,4,4,4,4,4,4,_,_,4,3,_,_,_,_,_,_,_,_,1],
    [7,_,_,_,_,_,_,_,_,_,_,4,_,4,_,_,_,_,4,3,_,3,1,1,1,1,1,1,1,1,_,1],
    [7,_,_,_,_,_,_,_,_,_,_,4,_,_,_,_,_,_,4,3,_,3,_,_,_,_,_,_,_,_,_,1],
    [7,_,_,9,_,_,9,_,_,_,_,4,_,4,_,_,_,_,4,3,_,3,_,_,_,_,6,_,_,_,_,1],
    [7,9,9,9,_,_,9,9,9,4,_,4,_,4,_,_,_,_,4,_,_,3,_,_,_,_,6,_,_,_,_,1],
    [1,9,9,9,_,_,9,9,9,4,_,4,_,4,_,_,_,_,4,3,_,3,_,_,_,_,_,_,_,_,_,1],
    [1,9,9,9,_,_,9,9,4,4,_,4,_,_,_,_,_,_,4,3,_,3,_,_,_,_,6,_,_,_,_,1],
    [1,9,9,_,_,_,_,9,9,4,_,4,_,4,_,_,_,_,4,3,_,3,_,_,_,_,_,_,_,_,_,1],
    [1,9,_,_,_,_,_,_,9,4,_,4,4,4,_,_,_,_,4,3,_,3,3,3,3,3,3,3,3,3,_,6],
    [1,9,9,_,_,_,_,9,9,4,_,_,_,4,_,_,_,_,4,6,_,_,_,_,_,_,_,_,_,_,_,6],
    [1,9,9,_,_,_,_,9,4,4,_,_,_,_,_,_,_,_,4,6,_,_,6,_,6,_,6,_,6,_,_,6],
    [4,9,9,9,9,9,9,9,4,4,4,4,4,4,4,4,4,4,4,6,_,_,_,_,_,_,_,_,_,_,6,6],
    [6]*35
]

MAP_NECROMANCERS_LAIR=[
    [11]*5,
    [11,_,_,_,_,11],
    [11,_,_,_,_,11],
    [11,_,_,_,_,11],
    [11,_,_,_,_,11],
    [11,_,_,_,_,11],
    [11]*5
]

class Map:
    def __init__(self,game,map,difficulty):
        self.game = game
        self.mini_map = map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()
        
        self.difficulty=difficulty
        self.pickable_items=[]
        self.enemies=[]
        self.enemies_pos={}
        self.Enemies()    
        self.PickableItems()

    def get_enemy_spawn(self):
        while True:
            x=random.randint(0,self.cols-1)
            y=random.randint(0,self.rows-1)
            if self.mini_map[y][x] == _:
                return (x, y)

    def PickableItems(self):
        self.pickable_items=[
            PickableItem(self.game,type='Sword',pos=(1,0),scale=0.5),
            PickableItem(self.game,type='Dagger',pos=(2,0),scale=0.5),
            PickableItem(self.game,type='Flail',pos=(3,0),scale=0.5),
            PickableItem(self.game,type='Mace',pos=(4,0),scale=0.5),
            PickableItem(self.game,type='Axe',pos=(5,0),scale=0.5),
            PickableItem(self.game,type='Warhammer',pos=(6,29),scale=0.5)
        ]

    def Enemies(self):
        rat=Rat(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=self.get_enemy_spawn(),Level=1,Value=100,HP=100,scale=0.5)
        self.enemies.append(rat)
        skeleton=Skeleton(self.game,path='Assets/Sprites/Animated/Skeleton/Idle/1.png',pos=(8,6),Level=5,Value=200,HP=200,scale=0.7)
        self.enemies.append(skeleton)
        wereboar= Wereboar(self.game,path='Assets/Sprites/Animated/Wereboar/Idle/1.png',pos=(12,12),Level=5,Value=200,HP=200,scale=0.7)
        self.enemies.append(wereboar)
        zombie= Zombie(self.game,path='Assets/Sprites/Animated/Zombie/Idle/1.png',pos=(5,5),Level=10,Value=500,HP=300,scale=0.7)
        self.enemies.append(zombie)
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.DISPLAY, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
        
    def Update(self):
        self.enemies_pos= {enemy.map_pos for enemy in self.enemies if not enemy.IsDead}
        [pickableitem.Update() for pickableitem in self.pickable_items]
        [enemy.Update() for enemy in self.enemies]

