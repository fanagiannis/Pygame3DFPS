import pygame as pg

from Settings import*
from Player import*
from Map import*


pg.init()

map=Map(MAP_SIZE,MAP_DEF)

while True:
    DISPLAY.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()


    map.draw()
    P.draw()
    P.update()
    
    pg.display.set_caption(f'{CLOCK.get_fps():.1f}')
    pg.display.flip()
    CLOCK.tick(FPS)
        
        
                        