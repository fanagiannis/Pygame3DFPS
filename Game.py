import pygame as pg

from Settings import*

pg.init()

DISPLAY=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
CLOCK=pg.time.Clock()
pg.display.set_caption("-")

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()

    pg.display.flip()
    CLOCK.tick(FPS)
        
        
                        