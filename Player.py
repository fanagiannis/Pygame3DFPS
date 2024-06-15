from Settings import *
import pygame as pg
import math

class PlayerStats():
    def __init__(self,game,maxhp,maxstamina,mana):
        self.game=game
        self.maxhp=maxhp
        self.maxstamina=maxstamina
        self.maxmana=mana
        self.HP=self.maxhp
        self.Stamina=self.maxstamina
        self.Mana=self.maxmana
        self.IsDead=False

    #HEALTH
    def TakeDamage(self,dmg): 
        if self.HP<=self.maxhp: self.HP-=dmg
        
    def Heal(self,value): 
        if self.HP<=self.maxhp and self.HP>=0: self.HP+=value

    def IncMaxHP(self,value):
        if self.maxhp<1000: self.maxhp+=value
        else: self.maxhp=1000
        
    def Death(self):
        if self.HP<=0: self.IsDead=True
        else: self.IsDead=False
        return self.IsDead
    
    #STAMINA
    def DecStamina(self,value):
        if self.Stamina<=self.maxstamina: self.Stamina-=value
    
    def IncStamina(self,value):
        if self.Stamina<=self.maxstamina and self.Stamina>=0: self.Stamina+=value

    #MANA
    def DecMana(self,value): 
        if self.Mana<=self.maxmana and self.Mana>=0: self.Mana-=value
        
    def IncMana(self,value):
        if self.Mana<=self.maxmana and self.Mana>=0: self.Mana+=value
        elif self.Mana<0: self.Mana=0
        elif self.Mana>self.maxmana: self.Mana=self.maxmana

    def StatsReset(self):
        if self.HP<0: self.HP=0
        if self.HP>self.maxhp: self.HP=self.maxhp
        if self.Stamina<0: self.Stamina=0
        if self.Stamina>self.maxstamina: self.Stamina=self.maxstamina
        if self.Mana<0: self.Mana=0
        if self.Mana>self.maxmana: self.Mana=self.maxmana
    
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
        self.stats=PlayerStats(self.game,100,100,100)

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
        if not self.stats.Death(): self.movement(),self.stats.Update()
        else: 
            text_Death=FONT_DEATH.render("YOU DIED",False,'red') 
            self.game.DISPLAY.blit(text_Death,(self.game.SCREEN_WIDTH//2-100,self.game.SCREEN_HEIGHT//2))

    @property
    def pos(self):
        return self.posx, self.posy

    @property
    def map_pos(self):
        return int(self.posx), int(self.posy)