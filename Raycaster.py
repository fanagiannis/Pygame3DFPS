import pygame as pg
import math
class Raycaster():
    def __init__(self,game):
        self.game=game
        self.CASTED_RAYS=int(self.game.SCREEN_WIDTH/5)
        self.MAX_DEPTH=int(self.game.SCREEN_WIDTH/2)
        self.TILE_SIZE=self.game.map.tilesize
        ####
        self.raycasting_result = []
        self.textures_to_render=[]
        self.textures=self.game.textureloader.walltextures

        ####


    def cast_rays(self): 
        SCALE = self.game.SCREEN_WIDTH//self.CASTED_RAYS
        STEP_ANGLE=(self.game.player.FOV)/self.CASTED_RAYS
        PLAYER_X,PLAYER_Y=self.game.player.Get_pos
        START_ANGLE = self.game.player.Get_angle - self.game.player.FOV/2
        
        for ray in range(self.CASTED_RAYS):
            for depth in range(self.MAX_DEPTH):
                TARGET_X= PLAYER_X + math.cos(START_ANGLE) * depth
                TARGET_Y = PLAYER_Y + math.sin(START_ANGLE) * depth

                row = int(TARGET_Y / self.TILE_SIZE)
                col = int(TARGET_X / self.TILE_SIZE)
                #pg.draw.line(self.game.DISPLAY,'yellow',(self.game.player.Get_pos),(TARGET_X,TARGET_Y),2)
                if self.game.map.mini_map[row][col] != 0:
                    texture = self.textures[self.game.map.mini_map[row][col]]
                    texture_x = int((TARGET_X % self.TILE_SIZE) / self.TILE_SIZE* (texture.get_width()))
                    texture_y = int((TARGET_Y % self.TILE_SIZE) / self.TILE_SIZE* (texture.get_height()))
                    
                    depth *= math.cos(self.game.player.ANGLE - START_ANGLE)
                    wall_height = 42000 / (depth + 0.0001)
                    wall_height = min(wall_height, self.game.SCREEN_HEIGHT)
                    
                    texture_slice = texture.subsurface(texture_x, 0,1, texture.get_height())
                    texture_slice = pg.transform.scale(texture_slice, (SCALE, int(wall_height)))
                    
                    self.game.DISPLAY.blit(texture_slice, (ray * SCALE, self.game.SCREEN_HEIGHT / 2 - wall_height / 2))
                    break

                    # color = 255 / (1 + depth * depth * 0.0001)
                    # pg.draw.rect(self.game.DISPLAY, (color, color, color), (ray * SCALE, self.game.SCREEN_HEIGHT / 2 - wall_height / 2, SCALE, wall_height))  #wallheigh/2 is the height of our perspective
            START_ANGLE+=STEP_ANGLE
    
    def Update(self):
        self.cast_rays()