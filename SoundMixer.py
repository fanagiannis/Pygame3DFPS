import pygame as pg
import random

class SoundMixer():
    def __init__(self):
        pg.mixer.init()
        self.deathsound_played=True
        self.Hitsound=[
            pg.mixer.Sound("Assets/Sounds/Hurt1.mp3"),
            pg.mixer.Sound("Assets/Sounds/Hurt2.mp3"),
            pg.mixer.Sound("Assets/Sounds/Hurt3.mp3")
        ]
        self.Deathsound=[
            pg.mixer.Sound("Assets/Sounds/Hurt4.mp3"),
        ]
    def PlaySound(self,soundarray):
        sound=random.choice(soundarray)
        sound.play()

    def PlayDeathSound(self):
        if self.deathsound_played:
            self.PlaySound(self.Deathsound)
            self.deathsound_played=False