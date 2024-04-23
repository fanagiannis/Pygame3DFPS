import pygame as pg

from Settings import*
from Player import*

pg.init()
pg.display.set_caption("-")

while True:
    DISPLAY.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()

    P.draw()
    P.update()
    pg.display.flip()
    CLOCK.tick(FPS)
        
        
                        