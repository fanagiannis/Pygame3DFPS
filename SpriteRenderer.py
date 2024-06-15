import pygame as pg 
import numpy as np
import math

from Settings import *

class Sprite:
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png',
                 pos=(10.5, 3.5), scale=0.7, shift=0.27):
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

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

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
        self.get_sprite()
# class Sprite():
#     def __init__(self,game,spritepath,pos):
#         self.game=game
#         self.sprite=pg.image.load(spritepath).convert_alpha()
#         self.sprite_size=np.asarray(self.sprite.get_size())
#         self.pos=np.array(pos)
#         pass
    # def position_calculation(self):
    #     player_pos=self.game.player.pos
    #     player_angle=self.game.player.angle

    #     self.dist=np.linalg.norm(self.pos,player_pos)    #CALCULATE DISTANCE FROM PLAYER

    #     delta_x=self.pos[0]-player_pos[0]               #CALCULATE SPRITE ANGLE RELATIVE TO PLAYERS VIEW ANGLE
    #     delta_y=self.pos[1]-player_pos[1]
    #     self.angle=math.atan2(delta_y,delta_x)
    #     rel_angle=self.angle-player_angle

    #     if rel_angle<-math.pi:                          #CHECK IF SPRITE IS WITHIN THE FOV
    #         rel_angle+=2*math.pi
    #     if rel_angle>math.pi:
    #         rel_angle-=2*math.pi
        
    #     return rel_angle

    # def projection(self):
    #     rel_angle=self.position_calculation()

    #     if abs(rel_angle)>FOV:
    #         return None
        
    #     proj_height=int(SCREEN_DIST/(self.dist+0.0001))
    #     proj_width=int(proj_height*(self.sprite_size[0]/self.sprite_size[1]))

    #     screen_x=int((HALF_WIDTH+rel_angle*NUM_RAYS*SCALE-proj_width/2))
    #     screen_y = int(HALF_HEIGHT - proj_height / 2)
    #     scaled_image = pg.transform.scale(self.image, (proj_width, proj_height))

    #     return self.dist, scaled_image, (screen_x, screen_y)
    #     pass
    

    # def Draw(self):
    #     mouse_pos=pg.mouse.get_pos()
    #     angle=np.arctan((self.mapposy-self.game.player.posy)/(self.mapposx-self.game.player.posx))
    #     if abs(self.game.player.posx+np.cos(angle)-self.mapposx)> abs(self.game.player.posx-self.mapposx):
    #         angle=(angle-np.pi)%(2*np.pi)
    #     anglediff=(self.game.player.angle-angle)%(2*np.pi)
    #     if anglediff>11*np.pi/6 or anglediff < np.pi/6:
    #         dist=np.sqrt((self.game.player.posx-self.mapposx)**2+(self.game.player.posy-self.mapposy)**2)
    #         cos2=np.cos(anglediff)
    #         self.scale=10*min(1/dist,2)#/cos2
    #         vert=300*self.scale - self.scale*self.sprite_size[1]/2
    #         hor=400-800*np.sin(anglediff) - self.scale*self.sprite_size[0]/2
    #         #self.scale=self.sprite_size*abs((mouse_pos[1]-300)/300)
    #         self.surf=pg.transform.scale(self.sprite,self.scale*self.sprite_size)
    #         #self.game.Raycaster.objects_to_render.append(self.surf)
    #         self.game.DISPLAY.blit(self.surf,(hor,vert))

        

    # def Update(self):
    #     self.Draw()