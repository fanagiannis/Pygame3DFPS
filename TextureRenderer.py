import pygame as pg
from Settings import *


class TextureRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.DISPLAY
        self.wall_textures = self.load_wall_textures()

    def render_textures(self):
        list_objects = sorted(self.game.Raycaster.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('Assets/Textures/Cave/1.png'),
            2: self.get_texture('Assets/Textures/Cave/2.png'),
            3: self.get_texture('Assets/Textures/Cave/3.png'),
            4: self.get_texture('Assets/Textures/Cave/4.png'),
            5: self.get_texture('Assets/Textures/Cave/5.png'),
            6: self.get_texture('Assets/Textures/Cave/6.png'),
        }
        #     2: self.get_texture('Assets/textures/2.png'),
        #     3: self.get_texture('Assets/textures/3.png'),
        #     4: self.get_texture('Assets/textures/4.png'),
        #     5: self.get_texture('Assets/textures/5.png'),
        # }

    def Update(self):
        self.render_textures()