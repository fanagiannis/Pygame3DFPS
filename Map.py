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

MAP_LEGION = [
    [15, 15, 15, 15, 15, 14, 15, 15, 15, 16, 16, 16, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
    [15, _,  _,  _,  _,  _,  _,  _,  15, _,  _,  _,  _,  _,  _,  _,  16, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [15, _,  _,  _,  _,  _,  _,  _,  15, _,  _,  _,  _,  _,  _,  _,  16, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [14, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [15, _,  _,  _,  _,  _,  _,  _,  15, _,  _,  _,  _,  _,  _,  _,  16, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  17, 11],
    [15, _,  _,  _,  _,  _,  _,  _,  15, _,  _,  _,  _,  _,  _,  _,  16, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [15, 15, 15, 15, _,  _, 15,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [13, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  17, 11],
    [13, _,  _,  _,  _,  _,  _,  _,  _,  16, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [13, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 16, 16, 16, 16, 16, 16, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  16, 11],
    [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, _,  13, 13, 13, 12, 13, 13, 13, _,  13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
    [20, 20, 20, 20, 20, 20, 20, 20, 20, 20,  13, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  20,  12, _,  20, 20, 21, 20, 20, _,  13, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  20,  13, _,  20, _,  _,  _,  _,  20, _,  13, _,  _,  _,  12, _,  12, _,  _,  _,  _,  _,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  20,  13, _,  20, _,  _,  _,  _,  20, _,  13, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20, 20, 20, 20, 20, 20, 20, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _, 11, 11, 11, 11, 11, 11,  _, 11, 11, 11,  11,11,  11],
    [20, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [20, 20, 20, _,  20, 20, _,  _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 20, _,  _,  _,  _,  20, _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 21, _,  _,  _,  _,  20, _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 21, _,  _,  _,  _,  20, _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 20, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 20, _,  _,  _,  _,  20, 20,20,  _,  _,  _,  _,  _,  _, _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,   21],
    [11, 19, 19, _,  19, 19, 19, 19,20,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 19, _,  _,  _,  _,  _,  19,20,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 19, _,  _,  _,  _,  _,  19,20,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 19, _,  _,  _,  _,  19, 19,20,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [11, 19, 19, 18, 19, 19, 19, 19,20,  _,  _,  _,  _,  _,  _, 20,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  20],
    [16, 16, 16, 16, 16, 16, 16, 16, 20,20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 20, 20, 20, 20, 20, 20, 21, 20, 20, 20, 20, 20,  20]
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
        self.items_pos=[]
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
        if self.difficulty==1: 
            self.items_pos=[(6,6),(17,7),(27,22),(30,5),(30,17)]
        elif self.difficulty==2:
            self.items_pos=[(5,4),(16,15),(27,3),(27,29),(13,3)]
        random.shuffle(self.items_pos)
        self.pickable_items=[
                PickableItem(self.game, type='Sword', pos=self.items_pos[0], scale=0.5),
                PickableItem(self.game, type='Dagger', pos=self.items_pos[1], scale=0.5),
                PickableItem(self.game, type='Flail', pos=self.items_pos[2], scale=0.5),
                PickableItem(self.game, type='Mace', pos=self.items_pos[3], scale=0.5),
                PickableItem(self.game, type='Axe', pos=self.items_pos[4], scale=0.5),
                PickableItem(self.game, type='Warhammer', pos=(6,29), scale=0.5)
            ]

    def Enemies(self):
        num_rats=random.randint(10,20) if self.difficulty==1 else random.randint(20,25) 
        num_skeletons=random.randint(10,15) if self.difficulty==1 else random.randint(25,30)
        num_wereboars=random.randint(0,6) if self.difficulty==1 else random.randint(6,12)
        num_zombies=1 if self.difficulty==1 else random.randint(30,35)

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
                rat=Rat(self.game,path='Assets/Sprites/Animated/Rat/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(4,8),Value=100*random.randint(3,4),HP=100*random.randint(1,3),scale=0.6)
                self.enemies.append(rat)
            for _ in range(num_skeletons):
                skeleton=Skeleton(self.game,path='Assets/Sprites/Animated/Skeleton/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(5,8),Value=200*random.randint(3,4),HP=200*random.randint(1,3),scale=0.7)
                self.enemies.append(skeleton)
            for _ in range(num_wereboars):
                wereboar= Wereboar(self.game,path='Assets/Sprites/Animated/Wereboar/Idle/1.png',pos=self.get_enemy_spawn(),Level=random.randint(5,8),Value=200*random.randint(3,4),HP=200*random.randint(1,3),scale=0.7)
                self.enemies.append(wereboar)
            for _ in range(num_zombies):
                zombie= Zombie(self.game,path='Assets/Sprites/Animated/Zombie/Idle/1.png',pos=self.get_enemy_spawn(),Level=20,Value=1000*random.randint(3,4),HP=400*random.randint(2,3),scale=0.7)
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

