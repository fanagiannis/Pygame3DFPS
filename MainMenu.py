import pygame as pg
import pygame_menu 

from Settings import *

class MainMenu():
    def __init__(self,game):
        self.game=game
        menu_theme=pygame_menu.themes.THEME_DARK
       # menu_theme.background_color=pygame_menu.BaseImage(LINK_ASSETS_BACKGROUND)
        menu_theme.title_font=FONT_DEATH
        menu_theme.title_font_color='orange'
        menu_theme.widget_font=FONT_RPG
        menu_theme.widget_font_color='yellow'
        menu_title="THE OLDER PAPERS"
        self.menu=pygame_menu.Menu(menu_title,self.game.SCREEN_WIDTH,self.game.SCREEN_HEIGHT,theme=menu_theme)

        menu_theme.widget_margin=(-600,0)
        global button_username,button_username2
        
        button_username=self.menu.add.text_input(" Enter Username : ",default="Player",maxchar=12)
        button_username2=self.menu.add.text_input(" Enter Username 2: ",default="Player2",maxchar=12)
        
        # button_startgame_solo=menu.add.button(" Singleplayer ",maingame_solo)
        # button_startgame_multi=menu.add.button(" Multiplayer ",maingame_multiplayer)
        self.menu.add.button(" Quit ",exit)                                 #LOAD MAIN MENU

    def Update(self):
        self.menu.mainloop(self.game.DISPLAY)   #SET MAIN MENU LOOP
