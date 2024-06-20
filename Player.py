from Settings import *
import pygame as pg
import math
import time



class Player():
    def __init__(self,game):
        self.game=game
        self.movement=PlayerMovement(self.game)
        self.stats=PlayerStats(self.game,1,1,1,1,1)
        self.vitalitystats=PlayerVitality(self.game,100,100,100,20,self)
        
        self.collisionbox=pg.Rect((self.movement.posx*100,self.movement.posy*100,50,50))
        self.hitbox=PlayerHitbox(self)
        self.crosshair=pg.image.load("Assets/Crosshair/Crosshair.png").convert_alpha()
        self.hitbox=PlayerHitbox(self)
        self.crosshair=pg.image.load("Assets/Crosshair/Crosshair.png").convert_alpha()
        self.attackcooldown=1000
        self.playerattacktime=0
        self.UpdateStats()

    def Draw(self):
        #COLLISION BOX
        pg.draw.rect(self.game.DISPLAY,'blue',self.collisionbox,1)

        #BODY
        pg.draw.line(self.game.DISPLAY, 'yellow', (self.movement.posx * 100, self.movement.posy * 100),
                    (self.movement.posx * 100 + WIDTH * math.cos(self.movement.angle),
                     self.movement.posy * 100 + WIDTH * math. sin(self.movement.angle)), 2)
        pg.draw.circle(self.game.DISPLAY, 'green', (self.movement.posx * 100, self.movement.posy * 100), 15)

    def Hitbox(self): 
        self.collisionbox=pg.Rect(((self.movement.posx-0.2)*100,(self.movement.posy-0.2)*100,40,40))
    
    def Crosshair(self):
        self.game.DISPLAY.blit(self.crosshair,(self.game.SCREEN_WIDTH//2-self.crosshair.get_width()//2,self.game.SCREEN_HEIGHT//2-self.crosshair.get_height()//2))
      
    def Update(self):
        self.Hitbox()
        #self.Draw()
        self.hitbox.Update()
        self.movement.Update()
        if not self.vitalitystats.IsDead:
            self.Crosshair()
            self.vitalitystats.Update()
            self.stats.Update()
            self.UpdateStats()
        
    
    def UpdateStats(self):
        self.vitalitystats.maxhp=self.vitalitystats.basehp+50*self.stats.Get_Endurance
        self.vitalitystats.maxstamina=self.vitalitystats.basestamina+50*self.stats.Get_Dexterity
        self.vitalitystats.maxmana=self.vitalitystats.basemana+50*self.stats.Get_Mind
        self.vitalitystats.maxmp=self.vitalitystats.basemp+20*self.stats.Get_Intelligence

    @property
    def GetHP(self): return self.vitalitystats.vitality_stats['HP']['value']
    @property
    def GetStamina(self): return self.vitalitystats.vitality_stats['STAMINA']['value']
    @property
    def GetMana(self): return self.vitalitystats.vitality_stats['MANA']['value']
    @property 
    def DealDamage(self):
        return 30+10*self.stats.stats['Level']['value']+10*self.stats.Get_Strength
    @property 
    def DealMagicDamage(self):
        return 30+10*self.stats.stats['Level']['value']+10*self.stats.Get_Intelligence

class PlayerHitbox():
    def __init__(self, player):
        self.player = player
        self.active = False
        self.duration = 5  # hitbox life
        self.timer=0
        self.hitcollision=pg.Rect(((self.player.movement.posx+math.cos(self.player.movement.angle)-0.25)*100,(self.player.movement.posy+math.sin(self.player.movement.angle)-0.25)*100,50,50))

    def Activate(self):
        timer=pg.time.get_ticks()
        if timer-self.player.playerattacktime>=self.player.attackcooldown and self.player.GetStamina>10 and self.player.GetStamina>10:
            self.active = True
            self.player.vitalitystats.DecStamina(20)
            self.timer=timer
            self.player.playerattacktime=timer
            self.player.game.sword.attack=True

    def Draw(self):
        self.hitcollision=pg.Rect(((self.player.movement.posx+math.cos(self.player.movement.angle)-0.25)*100,(self.player.movement.posy+math.sin(self.player.movement.angle)-0.25)*100,50,50))  #(,,hitboxsizex,hitboxsizey)
        ##pg.draw.rect(self.player.game.DISPLAY,'blue',self.hitcollision,1) #DEBUG #DEBUG

    def Update(self):
        if self.active:
            current_time = pg.time.get_ticks()
            if current_time - self.timer > self.duration:
                self.active = False
            else:
                self.Draw()

    @property
    def IsActive(self): return self.active
    @property
    def rect(self): return self.hitcollision

class PlayerMovement:
    def __init__(self, game):
        self.game = game
        self.posx, self.posy = (1.5,5)
        self.angle = 0
        self.scale=60
        self.speed=0.004

    def Movement(self):
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

    def Update(self):
        if not self.game.player.vitalitystats.Death(): self.Movement()
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
    def __init__(self,game,maxhp,maxstamina,maxmana,maxmp,player):
        self.game=game
        self.player=player
        self.maxhp=maxhp
        self.maxstamina=maxstamina
        self.maxmana=maxmana
        self.maxmp=maxmp
        
        self.basehp=self.maxhp#+50*self.player.stats.Get_Endurance
        self.basestamina=self.maxstamina#+50*self.player.stats.Get_Dexterity
        self.basemana=self.maxmana#+50*self.player.stats.Get_Mind
        self.basemp=self.maxmp#+20*self.player.stats.Get_Intelligence

        self.MagicPower=self.maxmp

        #STAMINA 
        #self.Stamina=self.maxstamina
        self.Staminaregentime=0

        self.vitality_stats={
            'HP': {'value':self.basehp,'color':'orange','pos':(0,0)},
            'STAMINA': {'value':self.basestamina,'color':'orange','pos':(0,18)},
            'MANA': {'value':self.basemana,'color':'orange','pos':(0,36)}
        }
        self.IsDead=False

    #HEALTH
    def TakeDamage(self,dmg): 
        if self.vitality_stats['HP']['value']<=self.maxhp: 
            self.game.DISPLAY.fill('red')
            self.vitality_stats['HP']['value']-=dmg 
            self.game.Soundmixer.PlaySound(self.game.Soundmixer.Hurtsound)
            print(dmg)
        
    def Heal(self,value): 
        if self.vitality_stats['HP']['value']<=self.maxhp and self.vitality_stats['HP']['value']>=0: self.vitality_stats['HP']['value']+=value

    def IncMaxHP(self,value):
        if self.maxhp<1000: self.maxhp+=value
        else: self.maxhp=1000
        
    def Death(self):
        if self.vitality_stats['HP']['value']<=0: 
            self.game.Soundmixer.PlayDeathSound()
            self.IsDead=True
        if self.vitality_stats['HP']['value']<=0: 
            self.game.Soundmixer.PlayDeathSound()
            self.IsDead=True
        else: self.IsDead=False
        return self.IsDead
    
    #STAMINA
    def DecStamina(self,value):
        if self.vitality_stats['STAMINA']['value']<=self.maxstamina: self.vitality_stats['STAMINA']['value']-=value
    
    def IncStamina(self,value):
        if self.vitality_stats['STAMINA']['value']<=self.maxstamina and self.vitality_stats['STAMINA']['value']>=0: self.vitality_stats['STAMINA']['value']+=value
    
    def StaminaRegen(self):
        timer=pg.time.get_ticks()
        if timer-self.Staminaregentime>=250:
            self.Staminaregentime=timer
            if self.vitality_stats['STAMINA']['value']<100: 
                self.IncStamina(1)
    
    def StaminaRegen(self):
        timer=pg.time.get_ticks()
        if timer-self.Staminaregentime>=250:
            self.Staminaregentime=timer
            if self.vitality_stats['STAMINA']['value']<100: 
                self.IncStamina(1)

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
        self.StaminaRegen()
        self.StaminaRegen()
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
        if self.stats['XP']['value']>=self.XPthreshhold:
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
        self.LevelUP()
        if pg.key.get_pressed()[pg.K_f]: self.LevelUP(), self.GainXP(1)
    
    @property
    def Get_Strength(self): return self.stats['Strength']['value']
    @property
    def Get_Endurance(self): return self.stats['Endurance']['value']
    @property
    def Get_Dexterity(self): return self.stats['Dexterity']['value']
    @property
    def Get_Mind(self): return self.stats['Mind']['value']
    @property
    def Get_Intelligence(self): return self.stats['Intelligence']['value']
    
    
