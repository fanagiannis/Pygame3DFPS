import pygame as pg
import math


class RayCaster():
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.textureloader.walltextures
        self.NUM_RAYS=self.game.SCREEN_WIDTH//2

    # def get_objects_to_render(self):
    #     self.objects_to_render = []
        
    #     SCALE=self.game.SCREEN_WIDTH/self.NUM_RAYS

    #     for ray, values in enumerate(self.ray_casting_result):
    #         depth, proj_height, texture, offset = values

    #         if proj_height < self.game.SCREEN_HEIGHT:
    #             wall_column = self.textures[texture].subsurface(
    #                 offset * (self.game.textureloader.TEXTURE_SIZE - SCALE), 0, SCALE, self.game.textureloader.TEXTURE_SIZE
    #             )
    #             wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
    #             wall_pos = (ray * SCALE, self.game.SCREEN_HEIGHT//2 - proj_height // 2)
    #         else:
    #             texture_height = self.game.textureloader.TEXTURE_SIZE * self.game.SCREEN_HEIGHT / proj_height
    #             wall_column = self.textures[texture].subsurface(
    #                 offset * (self.game.textureloader.TEXTURE_SIZE - SCALE), self.game.textureloader.TEXTURE_SIZE//2 - texture_height // 2,
    #                 SCALE, texture_height
    #             )
    #             wall_column = pg.transform.scale(wall_column, (SCALE, self.game.SCREEN_HEIGHT))
    #             wall_pos = (ray * SCALE, 0)

    #         self.objects_to_render.append((depth, wall_column, wall_pos))

    # def ray_cast(self):
    #     self.ray_casting_result = []
    #     texture_vert, texture_hor = 1, 1
    #     ox, oy = self.game.player.posx,self.game.player.posy
    #     x_map, y_map = self.game.player.map_pos
        
    #     DELTA_ANGLE=self.game.player.FOV/self.NUM_RAYS
    #     MAX_DEPTH=20
    #     SCREEN_DIST=(self.game.SCREEN_WIDTH/2)/math.tan(self.game.player.FOV/2)

    #     ray_angle = self.game.player.ANGLE- self.game.player.FOV//2 + 0.0001
    #     for ray in range(self.NUM_RAYS):
    #         sin_a = math.sin(ray_angle)
    #         cos_a = math.cos(ray_angle)

    #         # horizontals
    #         y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

    #         depth_hor = (y_hor - oy) / sin_a
    #         x_hor = ox + depth_hor * cos_a

    #         delta_depth = dy / sin_a
    #         dx = delta_depth * cos_a

    #         for i in range(MAX_DEPTH):
    #             tile_hor = int(x_hor), int(y_hor)
    #             if tile_hor in self.game.map.world_map:
    #                 texture_hor = self.game.map.world_map[tile_hor]
    #                 break
    #             x_hor += dx
    #             y_hor += dy
    #             depth_hor += delta_depth

    #         # verticals
    #         x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

    #         depth_vert = (x_vert - ox) / cos_a
    #         y_vert = oy + depth_vert * sin_a

    #         delta_depth = dx / cos_a
    #         dy = delta_depth * sin_a

    #         for i in range(MAX_DEPTH):
    #             tile_vert = int(x_vert), int(y_vert)
    #             if tile_vert in self.game.map.world_map:
    #                 texture_vert = self.game.map.world_map[tile_vert]
    #                 break
    #             x_vert += dx
    #             y_vert += dy
    #             depth_vert += delta_depth

    #         # depth, texture offset
    #         if depth_vert < depth_hor:
    #             depth, texture = depth_vert, texture_vert
    #             y_vert %= 1
    #             offset = y_vert if cos_a > 0 else (1 - y_vert)
    #         else:
    #             depth, texture = depth_hor, texture_hor
    #             x_hor %= 1
    #             offset = (1 - x_hor) if sin_a > 0 else x_hor

    #         # remove fishbowl effect
    #         depth *= math.cos(self.game.player.ANGLE - ray_angle)

    #         # projection
    #         proj_height = SCREEN_DIST / (depth + 0.0001)

    #         # ray casting result
    #         self.ray_casting_result.append((depth, proj_height, texture, offset))

    #         pg.draw.line(self.game.DISPLAY,'yellow',(self.game.player.Get_pos),(x_hor,y_hor),2)

    #         ray_angle += DELTA_ANGLE
            

    def render_game_objects(self):
        list_objects = sorted(self.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.game.DISPLAY.blit(image, pos)
    
    def draw(self):
        self.render_game_objects()

    def Update(self):
        #self.ray_cast()
        self.cast_rays()
        #self.get_objects_to_render()
        #self.draw()
# import pygame as pg
# import math
# class Raycaster():
#     def __init__(self,game):
#         self.game=game
#         self.NUM_RAYS=int(self.game.SCREEN_WIDTH/5)
#         self.MAX_DEPTH=int(self.game.SCREEN_WIDTH/2)
#         self.TILE_SIZE=self.game.map.tilesize
#         ####
#         self.raycasting_result = []
#         self.textures_to_render=[]
#         self.textures=self.game.textureloader.walltextures

#         ####

#     def get_objects_to_render(self):
#         self.objects_to_render = []
        
#         SCALE=self.game.SCREEN_WIDTH/self.NUM_RAYS

#         for ray, values in enumerate(self.ray_casting_result):
#             depth, proj_height, texture, offset = values

#             if proj_height < self.game.SCREEN_HEIGHT:
#                 wall_column = self.textures[texture].subsurface(
#                     offset * (self.game.textureloader.TEXTURE_SIZE - SCALE), 0, SCALE, self.game.textureloader.TEXTURE_SIZE
#                 )
#                 wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
#                 wall_pos = (ray * SCALE, self.game.SCREEN_HEIGHT//2 - proj_height // 2)
#             else:
#                 texture_height = self.game.textureloader.TEXTURE_SIZE * self.game.SCREEN_HEIGHT / proj_height
#                 wall_column = self.textures[texture].subsurface(
#                     offset * (self.game.textureloader.TEXTURE_SIZE - SCALE), self.game.textureloader.TEXTURE_SIZE//2 - texture_height // 2,
#                     SCALE, texture_height
#                 )
#                 wall_column = pg.transform.scale(wall_column, (SCALE, self.game.SCREEN_HEIGHT))
#                 wall_pos = (ray * SCALE, 0)

#             self.objects_to_render.append((depth, wall_column, wall_pos))

#     def cast_rays(self): 
#         SCALE = self.game.SCREEN_WIDTH//self.NUM_RAYS
#         STEP_ANGLE=(self.game.player.FOV)/self.NUM_RAYS
#         PLAYER_X,PLAYER_Y=self.game.player.Get_pos
#         START_ANGLE = self.game.player.Get_angle - self.game.player.FOV/2
        
#         for ray in range(self.NUM_RAYS):
#             for depth in range(self.MAX_DEPTH):
#                 TARGET_X= PLAYER_X + math.cos(START_ANGLE) * depth
#                 TARGET_Y = PLAYER_Y + math.sin(START_ANGLE) * depth

#                 row = int(TARGET_Y / self.TILE_SIZE)
#                 col = int(TARGET_X / self.TILE_SIZE)
#                 #pg.draw.line(self.game.DISPLAY,'yellow',(self.game.player.Get_pos),(TARGET_X,TARGET_Y),2)
#                 if self.game.map.mini_map[row][col] != 0:
#                     texture = self.textures[self.game.map.mini_map[row][col]]
#                     texture_x = int((TARGET_X % self.TILE_SIZE) / self.TILE_SIZE* (texture.get_width()))
#                     texture_y = int((TARGET_Y % self.TILE_SIZE) / self.TILE_SIZE* (texture.get_height()))
                    
#                     depth *= math.cos(self.game.player.ANGLE - START_ANGLE)
#                     wall_height = 42000 / (depth + 0.0001)
#                     wall_height = min(wall_height, self.game.SCREEN_HEIGHT)
                    
#                     texture_slice = texture.subsurface(texture_x, 0,1, texture.get_height())
#                     texture_slice = pg.transform.scale(texture_slice, (SCALE, int(wall_height)))
                    
#                     self.game.DISPLAY.blit(texture_slice, (ray * SCALE, self.game.SCREEN_HEIGHT / 2 - wall_height / 2))
#                     break

#                     # color = 255 / (1 + depth * depth * 0.0001)
#                     # pg.draw.rect(self.game.DISPLAY, (color, color, color), (ray * SCALE, self.game.SCREEN_HEIGHT / 2 - wall_height / 2, SCALE, wall_height))  #wallheigh/2 is the height of our perspective
#             START_ANGLE+=STEP_ANGLE

#     # def better_cast_rays(self):
#     #     self.ray_casting_result = []
#     #     TEXTURE_VERT, TEXTURE_HOR = 1, 1

#     #     SCALE = self.game.SCREEN_WIDTH//self.NUM_RAYS
#     #     SCREEN_DIST=(self.game.SCREEN_WIDTH/2)/math.tan(self.game.player.FOV/2)
#     #     STEP_ANGLE=(self.game.player.FOV)/self.NUM_RAYS
#     #     PLAYER_X,PLAYER_Y=self.game.player.Get_pos
#     #     START_ANGLE = self.game.player.Get_angle - self.game.player.FOV/2
        
#     #     for ray in range(self.NUM_RAYS):
#     #         sin_a=math.sin(self.game.player.ANGLE)
#     #         cos_a=math.cos(self.game.player.ANGLE)
#     #         #HORIZONTALS
#     #         Y_HOR,DY=(int(self.game.player.posy)+1),1 if sin_a>0 else (int(self.game.player.posy)-(1e-6)),-1

#     #         DEPTH_HOR=(Y_HOR-self.game.player.posy)/sin_a

#     #         X_HOR=self.game.player.posx+DEPTH_HOR*cos_a

#     #         DELTA_DEPTH=DY/sin_a
#     #         DX=DELTA_DEPTH*cos_a

#     #         for i in range(self.MAX_DEPTH):
#     #             TILE_HOR=int(X_HOR),int(Y_HOR)
#     #             if TILE_HOR in self.game.map.world_map:
#     #                 TEXTURE_HOR = self.game.map.world_map[TILE_HOR]
#     #                 break
#     #             X_HOR+=DX
#     #             Y_HOR+=DY
#     #             DEPTH_HOR += DELTA_DEPTH
            
     

            
            
#     #         #VERTICALS

#     #         X_VERT,DX=(int(self.game.player.posx)+1,1) if cos_a>0 else (int(self.game.player.posx)-1e-6,-1)
#     #         DEPTH_VERT=(X_VERT-self.game.player.posx)/cos_a

#     #         Y_VERT=X_VERT-self.game.player.posy + DEPTH_VERT*sin_a

#     #         DELTA_DEPTH=DX/cos_a
#     #         DY=DELTA_DEPTH*sin_a

#     #         for i in range(self.MAX_DEPTH):
#     #             TILE_VERT=int(X_VERT),int(Y_VERT)
#     #             if TILE_VERT in self.game.map.world_map:
#     #                 TEXTURE_VERT=self.game.map.world_map[TILE_VERT]
#     #                 break
#     #             X_VERT+=DX
#     #             Y_VERT+=DY
#     #             DEPTH_VERT+=DELTA_DEPTH
            
#     #         #DEPTH,TEXTURE

#     #         if DEPTH_VERT<DEPTH_HOR:
#     #             DEPTH,TEXTURE=DEPTH_VERT,TEXTURE_VERT
#     #             Y_VERT%=1
#     #             OFFSET=Y_VERT if cos_a>0 else (1-Y_VERT)
#     #         else:
#     #             DEPTH,TEXTURE=DEPTH_HOR,TEXTURE_HOR
#     #             X_HOR%=1
#     #             OFFSET=(1-X_HOR) if sin_a>0 else X_HOR

#     #         #FISHEYE

#     #         DEPTH*=math.cos(self.game.play.ANGLE-START_ANGLE)

#     #         PROJ_HEIGHT=SCREEN_DIST/(DEPTH+0.0001)

#     #         self.ray_casting_result.append((DEPTH,PROJ_HEIGHT,TEXTURE,OFFSET))

#     #         START_ANGLE+=STEP_ANGLE          
#     #     pass
    
#     def Update(self):
#         self.cast_rays()
#         self.get_objects_to_render()