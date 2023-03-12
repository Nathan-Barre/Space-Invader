import pygame
from pygame import mixer

class Sound:
    def __init__( self, p_path: str ):
        self.sound = mixer.Sound( p_path )

    def play( self ):
        self.sound.play()

    def play_loop( self ):
        self.sound.play( -1 )
