import pygame as pg
import pygame_menu 
import random

from Settings import *

class MainMenu():
    def __init__(self,game):
        self.game=game
        self.BackgroundImages()
        menu_theme=pygame_menu.themes.THEME_DARK.copy()
        menu_theme.title_background_color=(0,0,0,0)
        menu_theme.background_color=self.bgimages[random.randrange(0,len(self.bgimages))]
        menu_theme.title_font=FONT_DEATH
        menu_theme.title_font_color='orange'
        menu_theme.widget_font=FONT_RPG
        menu_theme.widget_font_color='yellow'
        menu_title="The Elder Falls"
        self.menu=pygame_menu.Menu(menu_title,self.game.SCREEN_WIDTH,self.game.SCREEN_HEIGHT,theme=menu_theme)

        menu_theme.widget_margin=(-600,0)
        
        self.button_play=self.menu.add.button(" Play ",self.DungeonSelection)                              
        self.button_play=self.menu.add.button(" How To Play ",self.Guide)                              
        self.button_quit=self.menu.add.button(" Quit ",exit)                               

    def BackgroundImages(self):
        self.bgimages=[
            pygame_menu.BaseImage('Assets/Images/Wallpapers/CastleVillage.png'),
            pygame_menu.BaseImage('Assets/Images/Wallpapers/RiverVillage.png'),
            pygame_menu.BaseImage('Assets/Images/Wallpapers/SnowyVillage.png'),
            pygame_menu.BaseImage('Assets/Images/Wallpapers/RockyVillage.png')
        ]

    def DungeonSelection(self):
        self.menu.clear()
        self.button_play1=self.menu.add.button(" The Rat King ",self.RunGameRK)
        self.button_play2=self.menu.add.button(" Undead Legion ",self.RunGameL)
        self.button_play3=self.menu.add.button(" Back ",self.Back)

    def change_background(self, index):
        self.current_bg = self.bgimages[index]
        self.menu.get_theme().background_color = self.current_bg
        self.menu.full_reset()   
    
    def RunGameRK(self):
        self.game.map_selected=self.game.map_rat_king
        self.game.Run()

    def RunGameL(self):
        self.game.map_selected=self.game.map_legion
        self.game.Run()

    def Guide(self):
        self.menu.clear()
        self.menu.add.label("Guide")
        self.menu.add.label("WASD to move.")
        self.menu.add.label("Left and Right arrow keys to look around.")
        self.menu.add.label("Press Space to attack.")
        self.menu.add.label("Press H to heal.")
        self.menu.add.label("                      ")
        self.menu.add.label("-------QUEST-------")
        self.menu.add.label("Clear the dungeon to win!")
        self.menu.add.label("                      ")
        self.menu.add.button(" Back ", self.Back)

    def Back(self):
        self.menu.clear()
        self.button_play=self.menu.add.button(" Play ",self.DungeonSelection)                              
        self.button_play=self.menu.add.button(" How To Play ",self.Guide)                              
        self.button_quit=self.menu.add.button(" Quit ",exit)   

    def Update(self):
        self.menu.mainloop(self.game.DISPLAY)   #SET MAIN MENU LOOP
