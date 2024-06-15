from Settings import *
import pygame as pg
import math

class PlayerStats():
    def __init__(self,game,hp,stamina,mana):
        self.game=game
        self.HP=hp
        self.Stamina=stamina
        self.Mana=mana
        self.IsDead=False

        self.UIstartPos=(0+20,self.game.SCREEN_HEIGHT-10)
        self.UIendPos=self.UIstartPos+(0,30)

    #HEALTH
    def TakeDamage(self,dmg): 
        if self.HP<=100: self.HP-=dmg
        
    def Heal(self,value): 
        if self.HP<=100 and self.HP>=0: self.HP+=value
        
    def Death(self):
        if self.HP<=0: return True
        else: return False
    
    #STAMINA
    def DecStamina(self,value):
        if self.Stamina<=100: self.Stamina-=value
    
    def IncStamina(self,value):
        if self.Stamina<=100 and self.Stamina>=0: self.Stamina+=value

    #MANA
    def DecMana(self,value):
        if self.Mana<=100 and self.Mana>=0: self.Mana-=value
        
    def IncMana(self,value):
        if self.Mana<=100 and self.Mana>=0: self.Mana+=value
        elif self.Mana<0: self.Mana=0
        elif self.Mana>100: self.Mana=100

    def StatsReset(self):
        if self.HP<0: self.HP=0
        if self.HP>100: self.HP=100
        if self.Stamina<0: self.Stamina=0
        if self.Stamina>100: self.Stamina=100
        if self.Mana<0: self.Mana=0
        if self.Mana>100: self.Mana=100
    
    def Fonts(self):
        text_HP = FONT_BASIC.render("HP", False, 'yellow')
        self.game.DISPLAY.blit(text_HP,(0,0))
        text_STAMINA = FONT_BASIC.render("STAMINA", False, 'yellow')
        self.game.DISPLAY.blit(text_STAMINA,(0,18))
        text_MANA = FONT_BASIC.render("MANA", False, 'yellow')
        self.game.DISPLAY.blit(text_MANA,(0,36))
    
    def Bars(self):
        pg.draw.rect(self.game.DISPLAY,'red',(20,3,self.HP,10),self.HP) #HP BAR
        pg.draw.rect(self.game.DISPLAY,'green',(60,20,self.Stamina,10),self.Stamina) #STAMINA BAR
        pg.draw.rect(self.game.DISPLAY,'blue',(40,38,self.Mana,10),self.Mana) #MANA BAR
        #pg.draw.line(self.game.DISPLAY,'green',(25,self.game.SCREEN_HEIGHT-10),(25,self.game.SCREEN_HEIGHT-10-self.Stamina),5) #STAMINA
        #pg.draw.line(self.game.DISPLAY,'blue',(40,self.game.SCREEN_HEIGHT-10),(40,self.game.SCREEN_HEIGHT-10-self.Mana),5) #MANA

    def Update(self):
        self.Bars()
        self.StatsReset()
        self.Fonts()
        #DEBUG
        keys=pg.key.get_pressed()
        if keys[pg.K_1]: self.Heal(1)
        if keys[pg.K_2]: self.TakeDamage(1)
        if keys[pg.K_3]: self.IncStamina(1)
        if keys[pg.K_4]: self.DecStamina(1)
        if keys[pg.K_5]: self.IncMana(1)
        if keys[pg.K_6]: self.DecMana(1)
        #DEBUG

class PlayerMovement:
    def __init__(self, game):
        self.game = game
        self.posx, self.posy = (1.5,5)
        self.angle = 0
        self.scale=60
        self.speed=0.004

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = self.speed * self.game.DELTA_TIME
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()

        #ANGLE 
        if keys[pg.K_LEFT]:
            self.angle-=0.001*self.game.DELTA_TIME
        if keys[pg.K_RIGHT]:
            self.angle+=0.001*self.game.DELTA_TIME

        #MOVEMENT
        if keys[pg.K_w]:   
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]: 
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = self.scale / self.game.DELTA_TIME
        if self.check_wall(int(self.posx + dx * scale), int(self.posy)):
            self.posx += dx
        if self.check_wall(int(self.posx), int(self.posy + dy * scale)):
            self.posy += dy

    def draw(self):
        pg.draw.line(self.game.DISPLAY, 'yellow', (self.posx * 100, self.posy * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angle),
                     self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.DISPLAY, 'green', (self.posx * 100, self.posy * 100), 15)

    def Update(self):
        #self.draw()
        self.movement()

    @property
    def pos(self):
        return self.posx, self.posy

    @property
    def map_pos(self):
        return int(self.posx), int(self.posy)