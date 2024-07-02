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
            7: self.get_texture('Assets/Textures/MossyCave/1.png'),
            8: self.get_texture('Assets/Textures/MossyCave/2.png'),
            9: self.get_texture('Assets/Textures/MossyCave/3.png'),
           10: self.get_texture('Assets/Textures/NL/1.png'),
           11: self.get_texture('Assets/Textures/NL/2.png'),
           12: self.get_texture('Assets/Textures/NL/3.png'),
           13: self.get_texture('Assets/Textures/NL/4.png'),
           14: self.get_texture('Assets/Textures/NL/5.png'),
           15: self.get_texture('Assets/Textures/NL/6.png'),
           16: self.get_texture('Assets/Textures/NL/7.png'),
           17: self.get_texture('Assets/Textures/NL/8.png'),
           18: self.get_texture('Assets/Textures/UL/1.png'),
           19: self.get_texture('Assets/Textures/UL/2.png'),
           20: self.get_texture('Assets/Textures/UL/3.png'),
           21: self.get_texture('Assets/Textures/UL/4.png')
        }
        #     2: self.get_texture('Assets/textures/2.png'),
        #     3: self.get_texture('Assets/textures/3.png'),
        #     4: self.get_texture('Assets/textures/4.png'),
        #     5: self.get_texture('Assets/textures/5.png'),
        # }

    def Update(self):
        self.render_textures()