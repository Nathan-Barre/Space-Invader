import pygame

class Score:
    def __init__( self ):
        self.font = pygame.font.Font( "freesansbold.ttf", 32 )
        self.score: int = 0
        self.pos_x: float =
        self.pos_y: float =

    def display_score( self, p_window ):
        l_score = self.font.render( "Score : " + str( self.score ), True, (255, 255, 255) )
        p_window.draw( l_score, self.pos_x, self.pos_y )
