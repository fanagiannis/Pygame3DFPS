import pygame as pg

from Settings import*
from Player import*


class Raycaster():
    def __init__(self,rays,player,map):
        self.player=player
        self.curmap=map
        self.rays_casted=rays
        self.step_angle=player.FOV/self.rays_casted
        #self.maxdepth=int(self.curmap.size*self.curmap.tile_size)
        self.scale=(SCREEN_WIDTH)//self.rays_casted
        
        
    def cast_rays(self):
        
        MAP=self.curmap.get_map() 
        PLAYER_X,PLAYER_Y=self.player.get_pos()
        PLAYER_MAPX,PLAYER_MAPY=self.player.get_map_pos()
        start_angle=self.player.get_angle()-self.player.HFOV+0.0001

        # for rays in range(self.rays_casted):
            
        #     Y_HOR,DY=(PLAYER_MAPY+1,1) if math.sin(start_angle)>0 else (PLAYER_MAPY-1e-6,-1)
        #     DEPTH_HOR=(Y_HOR-PLAYER_Y)/math.sin(start_angle)
        #     X_HOR= PLAYER_X + DEPTH_HOR*math.cos(start_angle)

        #     DELTA_DEPTH=DY/math.sin(start_angle)
        #     DX=DELTA_DEPTH*math.cos(start_angle)

        #     for i in range(self.maxdepth):
        #         TILE_HOR=int(X_HOR),int(Y_HOR)
        #         if MAP[i]=='#':
        #             break
        #         X_HOR+=DX
        #         Y_HOR+=DY
        #         DEPTH_HOR+=DELTA_DEPTH
            

        #     X_VERT,DX= (PLAYER_MAPX+1,1) if math.cos(start_angle)>0 else (PLAYER_MAPX-1e-6,-1)
        #     DEPTH_VERT=(X_VERT-PLAYER_X)/math.cos(start_angle)
        #     Y_VERT= PLAYER_Y+DEPTH_VERT*math.sin(start_angle)

        #     DELTA_DEPTH=DX/math.cos(start_angle)
        #     DY=DEPTH_VERT*math.sin(start_angle)

        #     for i in range(self.maxdepth):
        #         TILE_VERT=int(X_VERT),int(Y_VERT)
        #         if MAP[i]=='#':
        #             break
        #         X_VERT+=DX
        #         Y_VERT+=DY
        #         DEPTH_VERT+=DELTA_DEPTH


        #     if DEPTH_VERT<DEPTH_HOR:
        #         DEPTH=DEPTH_VERT
        #     else:
        #         DEPTH=DEPTH_HOR

        #     pg.draw.line(DISPLAY,(0,0,100),(100*PLAYER_X,100*PLAYER_Y),(100*PLAYER_X+100*DEPTH*math.cos(start_angle),100*PLAYER_Y+100*DEPTH*math.sin(start_angle)),2)

        #     start_angle+=self.step_angle
       
        for rays in range(self.rays_casted):   
            for depth in range(self.maxdepth):
                PLAYER_X,PLAYER_Y=self.player.get_pos()
                PLAYER_ANGLE=self.player.get_angle()
                TARGET_X=PLAYER_X-math.sin(start_angle)*depth
                TARGET_Y=PLAYER_Y+math.cos(start_angle)*depth
                #pg.draw.line(DISPLAY,(0,255,0),(PLAYER_X,PLAYER_Y),(TARGET_X,TARGET_Y),3)

                row=int(TARGET_Y/self.curmap.tile_size)
                column=int(TARGET_X/self.curmap.tile_size)
                square=square=row*self.curmap.size+column


                if MAP[square]=='#':
                    #pg.draw.rect(DISPLAY,(0,255,0),(column*self.curmap.tile_size,row*self.curmap.tile_size,self.curmap.tile_size,self.curmap.tile_size))
                    depth=depth*math.cos(PLAYER_ANGLE-start_angle)
                    
                    color= 255/(1+depth*depth*0.0001)
                    wallheight=21000/(depth+0.001)
                    
                    pg.draw.rect(DISPLAY,(color,color,color),(rays*self.scale,SCREEN_HEIGHT//2 - wallheight/2,self.scale,wallheight))
                    break
            start_angle+=self.step_angle
            pass
        pass
            

    def update(self):
        #self.cast_rays()
        pass

if __name__=='__main__':
    print("RayCaster")