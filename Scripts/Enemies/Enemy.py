import pygame as pg
import time

from Settings import*

from Scripts.Raycasting.SpriteRenderer import AnimatedSprite
from Scripts.Enemies.Pathfinding import * 

class Enemy(AnimatedSprite):
    def __init__(self, game, Level, Value, HP, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.Level=Level
        self.x,self.y=pos
        self.size=100
        self.Value=Value+10*self.Level
        self.HP=HP+20*self.Level
        self.Damage=20+10*self.Level
        self.visionradius=200
        self.attackradius=100
        self.IsDead=False
        self.player_spotted=False
        self.attacking=False
        self.hit=False
        self.death_animation_played=False
        self.speed=0.01
        self.hitbox=pg.Rect((self.x-0.15)*100,(self.y-0.15)*100,self.x+25,self.y+25)
        #ATTACK
        self.attackcooldown=1000
        self.attacktime=0
        self.hitcooldown=5000
        self.hittime=0
        self.framecounter=0
        #ANIMATIONS
        self.images_idle=self.get_images('Assets/Sprites/Animated/Rat/Idle')  
        self.images_walking=self.get_images('Assets/Sprites/Animated/Rat/Walk')
        self.images_attack=self.get_images('Assets/Sprites/Animated/Rat/Attack')
        self.images_death=self.get_images('Assets/Sprites/Animated/Rat/Death')
        self.images_hit=self.get_images('Assets/Sprites/Animated/Rat/Hit')
       
    def TakeDamage(self):
        self.HP=self.HP-(self.game.player.DealDamage-2*self.Level)
        self.game.Soundmixer.PlaySound(self.game.Soundmixer.Hitsound)
        return (self.game.player.DealDamage-2*self.Level)
    
    def Death(self):
        if self.HP<=0: self.IsDead=True
        else: self.IsDead=False
        return self.IsDead
    
    def Draw(self):
        pg.draw.circle(self.game.DISPLAY, 'yellow', (self.x*100,self.y*100), 15)       #BODY
        self.attackvision=pg.Rect(((self.x-0.625)*100,(self.y-0.625)*100,125,125))
        pg.draw.rect(self.game.DISPLAY,'blue',self.attackvision,2)          #ATTACK RANGE
        pg.draw.rect(self.game.DISPLAY,'blue',self.hitbox,1)              #HITBOX
        pg.draw.rect(self.game.DISPLAY,'blue',self.vision,2)             #VISION
    
    def Vision(self):
        self.vision=pg.Rect(((self.x-2.5)*100,(self.y-2.5)*100,500,500))
        if self.vision.colliderect(self.game.player.collisionbox): return True
        return False

    def Attack(self):
        timer=pg.time.get_ticks() 
        self.attackvision=pg.Rect(((self.x-0.7)*100,(self.y-0.7)*100,125,125))
        if self.attackvision.colliderect(self.game.player.collisionbox): 
            self.attacking=True
            if timer-self.attacktime>=self.attackcooldown and not self.game.player.vitalitystats.Death():
                self.game.player.vitalitystats.TakeDamage(self.Damage)
                self.attacktime = timer  
        else:
            self.attacking=False

    def Hit(self):
        if self.game.player.hitbox.IsActive and self.hitbox.colliderect(self.game.player.hitbox.rect) :
            self.TakeDamage()
            self.hit=True
        if self.hit:
            self.framecounter+=0.1
            if self.framecounter>len(self.images_hit):
                self.framecounter=0 
                self.hit=False
    
    def AnimationStates(self):
        self.animate(self.images_idle)
        if self.player_spotted and not self.attacking : self.animate(self.images_walking)
        if self.hit : self.animate(self.images_hit)
        if self.attacking : self.animate(self.images_attack)
        if self.Vision():
            self.player_spotted=True
        if self.player_spotted and not self.attacking:
            self.Movement()
    
    def DeathAnimation(self):
        self.game.player.stats.GainXP(self.Value) 
        self.game.map.enemies.remove(self)

    def Update(self):
        self.hitbox=pg.Rect((self.x-0.15)*100,(self.y-0.15)*100,self.x+25,self.y+25)
        self.images=self.images_walking
        if self.Death(): 
            self.DeathAnimation()
        elif not self.Death():
            self.AnimationStates()
        self.check_animation_time()
        self.get_sprite()  
        #self.draw_ray_cast()
        #self.ray_cast_value=self.ray_cast_player_npc()
        self.Vision()    #USED TO DETECT PLAYER
        self.Attack()
        self.Hit()
        keys=pg.key.get_pressed()
        # if keys[pg.K_r]:
        #     self.TakeDamage()
        #     time.sleep(0.1)
        #self.Draw()
        
    #MOVEMENT
    @property
    def map_pos(self):
        return int(self.x),int(self.y)
    
    def Movement(self):
        next_pos=self.game.Pathfinding.get_path(self.map_pos,self.game.player.movement.map_pos)
        next_x,next_y=next_pos
        angle=math.atan2(next_y+0.5-self.y,next_x+0.5-self.x)
        dx=math.cos(angle)*self.speed
        dy=math.sin(angle)*self.speed
        self.check_wall_collision(dx,dy)
        self.get_sprite()
        pass
    
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx*self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy*self.size)):
            self.y += dy
    
class Rat(Enemy):
    def __init__(self, game, Level, Value, HP, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=0.4, shift=0.7, animation_time=120):
        super().__init__(game, Level, Value, HP, path, pos, scale, shift, animation_time)
    def Update(self):
        return super().Update()

class Skeleton(Enemy):
    def __init__(self, game, Level, Value, HP, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=0.6, shift=0.3, animation_time=120):
        super().__init__(game, Level, Value, HP, path, pos, scale, shift, animation_time)
        #ANIMATIONS
        self.images_idle=self.get_images('Assets/Sprites/Animated/Skeleton/Idle')  
        self.images_walking=self.get_images('Assets/Sprites/Animated/Skeleton/Walk')
        self.images_attack=self.get_images('Assets/Sprites/Animated/Skeleton/Attack')
        self.images_death=self.get_images('Assets/Sprites/Animated/Skeleton/Death')
        self.images_hit=self.get_images('Assets/Sprites/Animated/Skeleton/Hit')
    def Update(self):
        return super().Update()

class Wereboar(Enemy):
    def __init__(self, game, Level, Value, HP, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=1, shift=0.2, animation_time=120):
        super().__init__(game, Level, Value, HP, path, pos, scale, shift, animation_time)
        #ANIMATIONS
        self.images_idle=self.get_images('Assets/Sprites/Animated/Wereboar/Idle')  
        self.images_walking=self.get_images('Assets/Sprites/Animated/Wereboar/Walk')
        self.images_attack=self.get_images('Assets/Sprites/Animated/Wereboar/Attack')
        self.images_death=self.get_images('Assets/Sprites/Animated/Wereboar/Death')
        self.images_hit=self.get_images('Assets/Sprites/Animated/Wereboar/Hit')
    def Update(self):
        return super().Update()

class Zombie(Enemy):
    def __init__(self, game, Level, Value, HP, path='resources/sprites/animated_sprites/green_light/0.png', pos=..., scale=0.7, shift=0.2, animation_time=120):
        super().__init__(game, Level, Value, HP, path, pos, scale, shift, animation_time)
        #ANIMATIONS
        self.images_idle=self.get_images('Assets/Sprites/Animated/Zombie/Idle')  
        self.images_walking=self.get_images('Assets/Sprites/Animated/Zombie/Walk')
        self.images_attack=self.get_images('Assets/Sprites/Animated/Zombie/Attack')
        self.images_death=self.get_images('Assets/Sprites/Animated/Zombie/Death')
        self.images_hit=self.get_images('Assets/Sprites/Animated/Zombie/Hit')
    def Update(self):
        return super().Update()
