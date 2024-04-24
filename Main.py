import pygame as pg

from Settings import*
from Player import*
from Map import*
from Raycaster import*


pg.init()

while True:
    
    DISPLAY.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()


    map_s.draw()
    RayCaster.update()
    P.update()
    
    pg.display.set_caption(f'{CLOCK.get_fps():.1f}')
    pg.display.flip()
    
    DELTA_TIME=CLOCK.tick(FPS)
        
        
                        