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
        self.Unarmed=Weapon(self.game,path='Assets/Sprites/Weapons/Unarmed/Idle.png',scale=0.4)
        self.Sword=Weapon(self.game,path='Assets/Sprites/Weapons/SteelSword/Idle.png',scale=0.5)

    #DEBUG
    def List(self):
        self.WeaponList()
        self.AddWeapon(self.Unarmed)
        self.AddWeapon(self.Sword)
    #DEBUG

    def AddWeapon(self,weapon):
        self.inventory.append(weapon)
    
    def GetSelectedWeapon(self):
        return self.inventory[self.selectedweapon]

    def Update(self):
        self.inventory[self.selectedweapon].Update()
      