import pygame as pg 

from Scripts.Arsenal.Weapon import *

class Arsenal:
    def __init__(self,game):
        self.game=game
        self.inventory=[]
        self.selectedweapon=0
        self.List()
        pass

    def WeaponList(self):
        self.Unarmed=Weapon(self.game,path='Assets/Sprites/Weapons/Unarmed/Idle.png',scale=0.8,damage=10)
        self.Dagger=Weapon(self.game,path='Assets/Sprites/Weapons/Dagger/Idle.png',scale=0.8,damage=30)
        self.Flail=Weapon(self.game,path='Assets/Sprites/Weapons/Flail/Idle.png',scale=0.8,damage=40)
        self.Sword=Weapon(self.game,path='Assets/Sprites/Weapons/SteelSword/Idle.png',scale=0.5,damage=50)
        self.Mace=Weapon(self.game,path='Assets/Sprites/Weapons/Mace/Idle.png',scale=0.9,damage=60)
        self.Axe=Weapon(self.game,path='Assets/Sprites/Weapons/Axe/Idle.png',scale=0.8,damage=90)
        self.Warhammer=Weapon(self.game,path='Assets/Sprites/Weapons/Warhammer/Idle.png',scale=0.8,damage=110)
        self.weapons_dict = {
            'Dagger': self.Dagger,
            'Flail': self.Flail,
            'Sword': self.Sword,
            'Mace': self.Mace,
            'Axe': self.Axe,
            'Warhammer': self.Warhammer
        }

    def List(self):
        self.WeaponList()
        self.AddWeapon(self.Unarmed)

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
        if keys[pg.K_6]:
            if len(self.inventory)>5:self.selectedweapon=5
        if keys[pg.K_7]:
            if len(self.inventory)>6:self.selectedweapon=6

    def AddWeapon(self,weapon):
        if weapon not in self.inventory:
            self.inventory.append(weapon)
    
    def PickupWeapon(self,weapon_type):
        if weapon_type in self.weapons_dict:
            weapon=self.weapons_dict[weapon_type]
            self.AddWeapon(weapon)
    
    def GetSelectedWeapon(self):
        return self.inventory[self.selectedweapon]

    def Update(self):
        self.SelectWeapon()
        if self.inventory:
            self.inventory[self.selectedweapon].Update()
    
    @property
    def GetDamage(self): return self.inventory[self.selectedweapon].damage
      