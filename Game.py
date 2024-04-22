import pygame as pg

from Settings import*

pg.init()

WIN=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("DOOM CLONE")
CLOCK=pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()

    pg.display.flip()
    CLOCK.tick(FPS)
        
        
                        