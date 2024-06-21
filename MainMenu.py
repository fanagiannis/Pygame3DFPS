import pygame as pg
import pygame_menu 
from pygame_menu.examples import create_example_window

from Settings import *

class MainMenu():
    def __init__(self,game):
        self.game=game
        menu_theme=pygame_menu.themes.THEME_DARK.copy()
        menu_theme.title_background_color=(0,0,0,0)
        menu_theme.background_color=pygame_menu.BaseImage('Assets/Images/Wallpapers/CastleVillage.png')
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
    
    def DungeonSelection(self):
        self.button_play._visible=False
        self.button_quit._visible=False
        self.button_play=self.menu.add.button(" Play ",self.DungeonSelection) 
        self.button_play=self.menu.add.button(" Play ",self.DungeonSelection) 
        self.button_play=self.menu.add.button(" Play ",self.DungeonSelection) 

    def RunGame(self):
        self.game.Run()

    def Update(self):
        self.menu.mainloop(self.game.DISPLAY)   #SET MAIN MENU LOOP
