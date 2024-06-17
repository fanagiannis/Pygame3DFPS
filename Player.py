from Settings import *
import pygame as pg
import math
import time

class Player():
    def __init__(self,game):
        self.game=game
        self.movement=PlayerMovement(self.game)
        self.vitalitystats=PlayerVitality(self.game,100,100,100)
        self.stats=PlayerStats(self.game,1,1,1,1,1)
        self.hitbox=pg.Rect(((self.movement.posx+0.1)*100,(self.movement.posy-0.3)*100,self.movement.posx+80,self.movement.posy+50))

    def Input(self):
        mouse_input=pg.mouse.get_pressed()
        if mouse_input[0]:
            self.Hitbox()
            pass

    def Hitbox(self):
        self.hitbox=pg.Rect(((self.movement.posx+math.cos(self.movement.angle)-0.25)*100,(self.movement.posy+math.sin(self.movement.angle)-0.25)*100,50,50))  #(,,hitboxsizex,hitboxsizey)
        pg.draw.rect(self.game.DISPLAY,'blue',self.hitbox,1)
    
    def Update(self):
        self.Input()
        self.movement.Update()
        self.vitalitystats.Update()
        self.stats.Update()

    @property
    def GetHP(self): return self.vitalitystats.vitality_stats['HP']['value']
    @property
    def GetStamina(self): return self.vitalitystats.vitality_stats['STAMINA']['value']
    @property
    def GetMana(self): return self.vitalitystats.vitality_stats['MANA']['value']
    @property 
    def DealDamage(self):
        return 10+10*self.stats.stats['Level']['value']


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
                    (self.posx * 100 + WIDTH * math.cos(self.angle),
                     self.posy * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.DISPLAY, 'green', (self.posx * 100, self.posy * 100), 15)

    def Update(self):
        self.draw()
        if not self.game.player.vitalitystats.Death(): self.movement()
        else: 
            text_Death=FONT_DEATH.render("YOU DIED",False,'red') 
            self.game.DISPLAY.blit(text_Death,(self.game.SCREEN_WIDTH//2-100,self.game.SCREEN_HEIGHT//2))

    @property
    def pos(self):
        return self.posx, self.posy

    @property
    def map_pos(self):
        return int(self.posx), int(self.posy)
    
class PlayerVitality():
    def __init__(self,game,maxhp,maxstamina,mana):
        self.game=game
        self.maxhp=maxhp
        self.maxstamina=maxstamina
        self.maxmana=mana
        #self.HP=self.maxhp
        self.Stamina=self.maxstamina
        self.Mana=self.maxmana

        self.vitality_stats={
            'HP': {'value':self.maxhp,'color':'orange','pos':(0,0)},
            'STAMINA': {'value':self.maxstamina,'color':'orange','pos':(0,18)},
            'MANA': {'value':self.maxmana,'color':'orange','pos':(0,36)}
        }
        self.IsDead=False

    #HEALTH
    def TakeDamage(self,dmg): 
        if self.vitality_stats['HP']['value']<=self.maxhp: self.vitality_stats['HP']['value']-=dmg
        
    def Heal(self,value): 
        if self.vitality_stats['HP']['value']<=self.maxhp and self.vitality_stats['HP']['value']>=0: self.vitality_stats['HP']['value']+=value

    def IncMaxHP(self,value):
        if self.maxhp<1000: self.maxhp+=value
        else: self.maxhp=1000
        
    def Death(self):
        if self.vitality_stats['HP']['value']<=0: self.IsDead=True
        else: self.IsDead=False
        return self.IsDead
    
    #STAMINA
    def DecStamina(self,value):
        if self.vitality_stats['STAMINA']['value']<=self.maxstamina: self.vitality_stats['STAMINA']['value']-=value
    
    def IncStamina(self,value):
        if self.vitality_stats['STAMINA']['value']<=self.maxstamina and self.vitality_stats['STAMINA']['value']>=0: self.vitality_stats['STAMINA']['value']+=value

    #MANA
    def DecMana(self,value): 
        if self.vitality_stats['MANA']['value']<=self.maxmana and self.vitality_stats['MANA']['value']>=0: self.vitality_stats['MANA']['value']-=value
        
    def IncMana(self,value):
        if self.vitality_stats['MANA']['value']<=self.maxmana and self.vitality_stats['MANA']['value']>=0: self.vitality_stats['MANA']['value']+=value
        elif self.vitality_stats['MANA']['value']<0: self.vitality_stats['MANA']['value']=0
        elif self.vitality_stats['MANA']['value']>self.maxmana: self.vitality_stats['MANA']['value']=self.maxmana

    def StatsReset(self):
        if self.vitality_stats['HP']['value']<0: self.vitality_stats['HP']['value']=0
        if self.vitality_stats['HP']['value']>self.maxhp: self.vitality_stats['HP']['value']=self.maxhp
        if self.vitality_stats['STAMINA']['value']<0: self.vitality_stats['STAMINA']['value']=0
        if self.vitality_stats['STAMINA']['value']>self.maxstamina: self.vitality_stats['STAMINA']['value']=self.maxstamina
        if self.vitality_stats['MANA']['value']<0: self.vitality_stats['MANA']['value']=0
        if self.vitality_stats['MANA']['value']>self.maxmana: self.vitality_stats['MANA']['value']=self.maxmana
    
    def Fonts(self):
        text_HP = FONT_BASIC.render("HP", False, 'yellow')
        self.game.DISPLAY.blit(text_HP,(0,0))
        text_STAMINA = FONT_BASIC.render("STAMINA", False, 'yellow')
        self.game.DISPLAY.blit(text_STAMINA,(0,18))
        text_MANA = FONT_BASIC.render("MANA", False, 'yellow')
        self.game.DISPLAY.blit(text_MANA,(0,36))
    
    def Bars(self):
        pg.draw.rect(self.game.DISPLAY,'red',(20,3,self.vitality_stats['HP']['value'],10),self.vitality_stats['HP']['value']) #HP BAR
        pg.draw.rect(self.game.DISPLAY,'green',(60,20,self.vitality_stats['STAMINA']['value'],10),self.vitality_stats['STAMINA']['value']) #STAMINA BAR
        pg.draw.rect(self.game.DISPLAY,'blue',(40,38,self.vitality_stats['MANA']['value'],10),self.vitality_stats['MANA']['value']) #MANA BAR

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
    
class PlayerStats():
    def __init__(self,game,STR,END,DEX,MIND,INT):
        self.game = game
        self.stats = {
            'Level': {'value': 0, 'color': 'yellow', 'pos': (self.game.SCREEN_WIDTH - 150, 10)},
            'XP': {'value': 0, 'color': 'yellow', 'pos': (self.game.SCREEN_WIDTH - 150, 40)},
            'Strength': {'value': STR, 'color': 'orange', 'pos': (self.game.SCREEN_WIDTH - 150, 80)},
            'Endurance': {'value': END, 'color': 'orange', 'pos': (self.game.SCREEN_WIDTH - 150, 110)},
            'Dexterity': {'value': DEX, 'color': 'orange', 'pos': (self.game.SCREEN_WIDTH - 150, 140)},
            'Mind': {'value': MIND, 'color': 'orange', 'pos': (self.game.SCREEN_WIDTH - 150, 170)},
            'Intelligence': {'value': INT, 'color': 'orange', 'pos': (self.game.SCREEN_WIDTH - 150, 200)},
            'Token': {'value': 0, 'color': 'orange', 'pos': (self.game.SCREEN_WIDTH - 150, 280)},
        }
        self.XPthreshhold=100

    def UpgradeStat(self,stat):
        if self.stats['Token']['value']>0 and stat in self.stats:
            self.stats[stat]['value']+=1
            self.stats['Token']['value']-=1

    def GainXP(self,value):
        self.stats['XP']['value']+=value

    def LevelUP(self):
        if self.stats['XP']['value']>self.XPthreshhold:
            self.XPthreshhold*=2
            self.stats['Level']['value']+=1
            self.stats['Token']['value']+=1
    
    def DisplayStats(self):
        for stat,values in self.stats.items():
            if stat == 'Token' and values['value'] == 0: continue
            if self.stats['Token']['value']>0: self.game.DISPLAY.blit(FONT_STATS.render("LEVEL UP!", False, 'red'),(self.game.SCREEN_WIDTH-150,250))
            text = FONT_STATS.render(f"{stat} : {values['value']}", False, values['color'])
            self.game.DISPLAY.blit(text, values['pos'])

    def StatUpgrade(self):
        if self.stats['Token']['value']>0:
            for stat,values in self.stats.items():
                if stat in ['Token','Level','XP']: continue
                stat_btn=FONT_STATS.render(f"{stat} : {values['value']}", False, values['color'])
                text = stat_btn.get_rect(topleft=values['pos'])
                if text.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                    self.UpgradeStat(stat)
                    time.sleep(0.1)
                    break

    def Update(self):
        self.DisplayStats()
        self.StatUpgrade()
        if pg.key.get_pressed()[pg.K_f]: self.LevelUP(), self.GainXP(1)
