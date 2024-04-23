import pygame as pg

from Settings import*
from Player import*

pg.init()
pg.display.set_caption("-")

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()

    P.draw()
    pg.display.flip()
    CLOCK.tick(FPS)
        
        
                        