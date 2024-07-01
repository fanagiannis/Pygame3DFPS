import pygame as pg
import random

from PickableItem import *
from Enemy import *

#   WALL         [1]*64,
#   SPACE        [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],

_ = False

MAP_RAT_KING=[
    [1]*32,
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
    [6]*32
]

MAP_LEGION=[
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
        self.cleared=False
        
        self.difficulty=difficulty
        self.pickable_items=[]
        self.enemies=[]
        self.enemies_pos={}
        self.Enemies()    
        self.PickableItems()

    def get_enemy_spawn(self):
        while True:
            x = random.randint(0, self.cols - 1)
            y = random.randint(0, self.rows - 1)
            if 0 <= y < self.rows and 0 <= x < self.cols:
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
        num_rats=10 if self.difficulty==1 else 15
        num_skeletons=2 if self.difficulty==1 else 6
        num_wereboars=0 if self.difficulty==1 else 5
        num_zombies=1 if self.difficulty==1 else 20

        if self.difficulty==1:
            for _ in range(num_rats):
                rat=Rat(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(1,5),Value=100*random.randint(1,2),HP=100*random.randint(1,3),scale=0.5)
                self.enemies.append(rat)
            for _ in range(num_skeletons):
                skeleton=Skeleton(self.game,path='Assets/Sprites/Animated/Skeleton/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(5,8),Value=200*random.randint(1,2),HP=200*random.randint(1,3),scale=0.7)
                self.enemies.append(skeleton)
            for _ in range(num_zombies):
                zombie= Zombie(self.game,path='Assets/Sprites/Animated/Zombie/Idle/1.png',pos=(6,27),Level=20,Value=1000,HP=500,scale=0.7)
                self.enemies.append(zombie)
        
        elif self.difficulty==2:
            for _ in range(num_rats):
                rat=Rat(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(1,5),Value=100*random.randint(1,2),HP=100*random.randint(1,3),scale=0.5)
                self.enemies.append(rat)
            for _ in range(num_skeletons):
                skeleton=Skeleton(self.game,path='Assets/Sprites/Animated/Skeleton/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(5,8),Value=200*random.randint(1,2),HP=200*random.randint(1,3),scale=0.7)
                self.enemies.append(skeleton)
            for _ in range(num_wereboars):
                wereboar= Wereboar(self.game,path='Assets/Sprites/Animated/Wereboar/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(5,8),Value=200*random.randint(1,2),HP=200*random.randint(1,3),scale=0.7)
                self.enemies.append(wereboar)
            for _ in range(num_zombies):
                zombie= Zombie(self.game,path='Assets/Sprites/Animated/Zombie/Idle/1.png',pos=self.get_enemy_spawn(),Level=15,Value=1000,HP=400,scale=0.7)
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

        if len(self.enemies)<=0: self.cleared=True
    
    @property
    def GetClear(self): return self.cleared

