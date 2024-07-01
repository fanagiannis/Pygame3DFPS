import pygame as pg
import random

class SoundMixer():
    def __init__(self):
        pg.mixer.init()
        self.assetpath="Assets/Sounds/"
        self.deathsound_played=True
        self.menutheme=pg.mixer.Sound(self.assetpath+'MainMenu/MainMenuTheme.mp3')
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
        self.Swingsound=[
            pg.mixer.Sound(self.assetpath+"Swing/SWING01.wav"),
            pg.mixer.Sound(self.assetpath+"Swing/SWING02.wav"),
            pg.mixer.Sound(self.assetpath+"Swing/SWING03.wav"),
            pg.mixer.Sound(self.assetpath+"Swing/SWING04.wav"),
        ]
        self.Levelupsound=pg.mixer.Sound(self.assetpath+"Levelup.wav")
        self.Enchantsound=pg.mixer.Sound(self.assetpath+"Enchant.wav")
        self.Selectsound=pg.mixer.Sound(self.assetpath+"Select.wav")
        self.WeaponPickup=pg.mixer.Sound(self.assetpath+"Weild.wav")
        self.Deathsound=pg.mixer.Sound(self.assetpath+"Death.wav")

    def Play(self,sound):
        sound.play()

    def PlaySound(self,soundarray):
        sound=random.choice(soundarray)
        sound.play()

    def PlayDeathSound(self):
        if self.deathsound_played:
            self.Deathsound.play()#self.PlaySound(self.Deathsound)
            self.deathsound_played=False
    
    def PlayMenuTheme(self):
        self.menutheme.play()
    def StopMenuTheme(self):
        self.menutheme.stop()