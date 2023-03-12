import pygame
from sound.sound import Sound
from sprite.sprite import Sprite
class Enemy:
    def __init__( self ):
        self.sound: Sound
        self.sprite: Sprite
        self.hp: int
        self.speed_x: float
        self.speed_y: float

        # Todo