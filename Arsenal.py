import pygame as pg 

from Weapon import *

class Arsenal:
    def __init__(self,game):
        self.game=game
        self.inventory=[]
        self.selectedweapon=1
        self.List()
        pass

    def WeaponList(self):
        self.Unarmed=Weapon(self.game,path='Assets/Sprites/Weapons/Unarmed/Idle.png',scale=0.4,damage=10)
        self.Sword=Weapon(self.game,path='Assets/Sprites/Weapons/SteelSword/Idle.png',scale=0.5,damage=40)

    #DEBUG
    def List(self):
        self.WeaponList()
        self.AddWeapon(self.Unarmed)
        self.AddWeapon(self.Sword)
    #DEBUG

    def SelectWeapon(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_1]: self.selectedweapon=0
        if keys[pg.K_2]: 
            if len(self.inventory)>1:self.selectedweapon=1
        if keys[pg.K_3]: 
            if len(self.inventory)>2:self.selectedweapon=2
        if keys[pg.K_4]:
            if len(self.inventory)>3:self.selectedweapon=3
        if keys[pg.K_5]:
            if len(self.inventory)>4:self.selectedweapon=4

    def AddWeapon(self,weapon):
        self.inventory.append(weapon)
    
    def GetSelectedWeapon(self):
        return self.inventory[self.selectedweapon]

    def Update(self):
        self.SelectWeapon()
        self.inventory[self.selectedweapon].Update()
    
    @property
    def GetDamage(self): return self.inventory[self.selectedweapon].damage
      