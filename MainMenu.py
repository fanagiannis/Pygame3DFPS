import pygame as pg
import pygame_menu 
import random
from pygame_menu.examples import create_example_window

from Settings import *

class MainMenu():
    def __init__(self,game):
        self.game=game
        self.BackgroundImages()
        menu_theme=pygame_menu.themes.THEME_DARK.copy()
        menu_theme.title_background_color=(0,0,0,0)
        menu_theme.background_color=self.bgimages[random.randrange(0,len(self.bgimages))]
       # menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
        menu_theme.title_font=FONT_DEATH
        menu_theme.title_font_color='orange'
        menu_theme.widget_font=FONT_RPG
        menu_theme.widget_font_color='yellow'
        menu_title="THE OLDER PAPERS"
        self.menu=pygame_menu.Menu(menu_title,self.game.SCREEN_WIDTH,self.game.SCREEN_HEIGHT,theme=menu_theme)

        #menu_theme.add.Label('THE OLDER PAPERS',background_color='#333',background_inflate=(30, 0),float=True).translate()

        menu_theme.widget_margin=(-600,0)
        
        self.button_play=self.menu.add.button(" Play ",self.DungeonSelection)                                 #LOAD MAIN MENU
        self.button_quit=self.menu.add.button(" Quit ",exit)                                 #LOAD MAIN MENU

        self.dungeon_descs={
            'The Rat King': 'Start the game.',
            'Lair Of The Necromancer': 'Quit the game.',
            'Undead Legion':'C'
        }

    def BackgroundImages(self):
        self.bgimages=[
            pygame_menu.BaseImage('Assets/Images/Wallpapers/CastleVillage.png'),
            pygame_menu.BaseImage('Assets/Images/Wallpapers/RiverVillage.png'),
            pygame_menu.BaseImage('Assets/Images/Wallpapers/SnowyVillage.png'),
            pygame_menu.BaseImage('Assets/Images/Wallpapers/RockyVillage.png')
        ]

    def DungeonImaged(self):
        self.dungeonImages=[]

    def DungeonSelection(self):
        self.button_play._visible=False
        self.button_quit._visible=False
        self.button_play1=self.menu.add.button(" The Rat King ",self.RunGame)
        self.button_play2=self.menu.add.button(" Necromancer's Lair ",self.RunGame)
        self.button_play3=self.menu.add.button(" Undead Legion ",self.game.Run)


    def change_background(self, index):
        self.current_bg = self.bgimages[index]
        self.menu.get_theme().background_color = self.current_bg
        self.menu.full_reset()   
    
    def RunGame(self):
        self.game.Run()

    def Update(self):
        self.menu.mainloop(self.game.DISPLAY)   #SET MAIN MENU LOOP
