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
            pg.mixer.Sound(self.assetpath+"Hit/HIT05.WAV"),
            pg.mixer.Sound(self.assetpath+"Hit/HIT06.WAV")
        ]
        self.Deathsound=[
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt1.mp3"),
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt2.mp3"),
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt3.mp3"),
            pg.mixer.Sound(self.assetpath+"Hurt/Hurt4.mp3")
        ]
    def PlaySound(self,soundarray):
        sound=random.choice(soundarray)
        sound.play()

    def PlayDeathSound(self):
        if self.deathsound_played:
            self.PlaySound(self.Deathsound)
            self.deathsound_played=False