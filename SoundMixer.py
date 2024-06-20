import pygame as pg
import random

class SoundMixer():
    def __init__(self):
        pg.mixer.init()
        self.assetpath="Assets/Sounds/"
        self.deathsound_played=True
        self.Hitsound=[
            pg.mixer.Sound(self.assetpath+"Hit/HIT01.WAV"),
            pg.mixer.Sound(self.assetpath+"Hit/HIT02.WAV"),
            pg.mixer.Sound(self.assetpath+"Hit/HIT03.WAV"),
            pg.mixer.Sound(self.assetpath+"Hit/HIT04.WAV"),
            pg.mixer.Sound(self.assetpath+"Hit/HIT05.WAV")
        ]
        self.Hurtsound=[
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt1.wav"),
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt2.wav"),
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt3.wav"),
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt4.wav")
        ]
        self.Deathsound=pg.mixer.Sound(self.assetpath+"Death.wav")
    def PlaySound(self,soundarray):
        sound=random.choice(soundarray)
        sound.play()

    def PlayDeathSound(self):
        if self.deathsound_played:
            self.Deathsound.play()#self.PlaySound(self.Deathsound)
            self.deathsound_played=False
    
    def PlayTheme(self,theme):
        sound=theme
        sound.play()