import pygame as pg 
import numpy as np
import math

from Settings import *

class Sprite:
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png',
                 pos=(10.5, 3.5), scale=0.7, shift=0.27,castlight=False):
        self.game = game
        self.player = self.game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

        #LIGHT
        self.castlight=castlight

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        if not self.castlight:
            shading = max(0.1, min(1, 1 / (self.norm_dist * 0.9)))
            #shade_image=image.copy()
            shaded_surface = pg.Surface(image.get_size(), flags=pg.SRCALPHA)
            shaded_surface.fill((0, 0, 0, int((1 - shading) * 255)))
            image.blit(shaded_surface, (0, 0), special_flags=pg.BLEND_RGBA_SUB)
        # shade_image=image.fill((shading*255,shading*255,shading*255),special_flags=pg.BLEND_MULT) 
        # # shade_image = pg.transform.scale(shade_image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

        self.game.Raycaster.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.posx
        dy = self.y - self.player.posy
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        print(self.castlight)
        self.get_sprite()

class LightSource(Sprite):
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=(10.5, 3.5), scale=0.7, shift=0.27, castlight=True):
        super().__init__(game, path, pos, scale, shift, castlight)
    def update(self):
        return super().update()