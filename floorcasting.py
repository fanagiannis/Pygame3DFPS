import pygame as pg
import numpy as np


def main():
    pg.init()
    SCREEN = pg.display.set_mode((800,600))
    HRES=120
    VERTICAL=200
    HALFRES=int(VERTICAL/2)
    MOD = HALFRES/60
    POSX,POSY,ROT= 0,0,0
    FRAME = np.random.uniform(0,1,(HRES,VERTICAL,3))

    sky=pg.image.load('Assets/Images/skybox.jpg')
    sky=pg.surfarray.array3d(pg.transform.scale(sky,(36),HALFRES*2))

    running = True
    while running:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
        #similar raycasting
        for i in range (HRES):
            ROT_i = ROT + np.deg2rad(i/MOD-30)
            sin,cos= np.sin(ROT_i),np.cos(ROT_i)

            FRAME[i][:]=sky[int(np.rad2deg(ROT_i)%360)][:]/255

            for j in range (HALFRES):
                n=HALFRES / (HALFRES- j)
                x,y= POSX+cos*n,POSY +sin*n

                if int(x)%2 ==int(y)%2:
                    FRAME[i][HALFRES*2-j-1]=[0,0,0]
                else:
                    FRAME[i][HALFRES*2-j-1]=[1,1,1]


        surf = pg.surfarray.make_surface(FRAME*255)
        surf= pg.transform.scale(surf,(800,600))
        SCREEN.blit(surf,(0,0))
        pg.display.update()
        POSX,POSY,ROT=movement(POSX,POSY,ROT,pg.key.get_pressed())

def movement(POSX,POSY,ROT,KEYS):
    if KEYS[pg.K_LEFT] or KEYS[ord('a')]:
        ROT=ROT-0.1
    if KEYS[pg.K_RIGHT] or KEYS[ord('d')]:
        ROT=ROT+0.1
    if KEYS[pg.K_UP] or KEYS[ord('w')]:
        POSX,POSY=POSX+np.cos(ROT)*0.1,POSY+np.sin(ROT)*0.1
    if KEYS[pg.K_DOWN] or KEYS[ord('s')]:
        POSX,POSY=POSX-np.cos(ROT)*0.1,POSY-np.sin(ROT)*0.1
    return POSX,POSY,ROT

if __name__=='__main__':
    main()
    pg.quit()
