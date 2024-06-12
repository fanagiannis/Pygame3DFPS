import pygame as pg
import math

from Settings import *


class Raycaster:
    def __init__(self, game):
        self.game = game
        self.rays_casted = SCREEN_WIDTH
        self.FOV = math.pi / 3
        self.HALF_FOV = self.FOV / 2
        self.DELTA_ANGLE = self.FOV / self.rays_casted

    def cast_rays(self):
        pass

    def update(self):
        self.cast_rays()