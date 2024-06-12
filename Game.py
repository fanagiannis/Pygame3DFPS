import pygame as pg

class Game():
    def __init__(self):
        self.SCREEN_WIDTH=1600
        self.SCREEN_HEIGHT=900
        self.DISPLAY=pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.CLOCK=pg.time.Clock()
        self.FPS=60
        self.running=True
        pass
    
    def Run(self):
        pg.init()
        while self.running:
            self.Events()
            self.Cycle()
            self.Update()
        pass
    
    def Events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT :
                pg.quit()    

    def Cycle(self): 
        self.DISPLAY.fill((0,0,0))
        self.ShowFPS()
        pg.display.flip()
        self.DELTA_TIME=self.CLOCK.tick(self.FPS)
        
    def ShowFPS(self):
        pg.display.set_caption(f'{self.CLOCK.get_fps():.1f}')
        fps = str(int(self.CLOCK.get_fps()))
        font = pg.font.SysFont('Monospace Regular', 30)
        text_surface = font.render(fps, False, 'yellow')
        self.DISPLAY.blit(text_surface,(0,0))

    def Update(self):
        
        pass