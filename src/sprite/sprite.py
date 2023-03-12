import pygame

class Sprite:
    def __init__( self, p_path: str, p_nb_sprite: str, pos_x: float, pos_y: float ):
        self.index_max: int = 0
        self.index: int = 0
        self.img: list[ any ] = [ ]
        self.pos_x: float = 0
        self.pos_y: float = 0

        self.create_sprite( p_path, p_nb_sprite, pos_x, pos_y )

    def create_sprite( self, p_path: str, p_nb_sprite: str, pos_x: float, pos_y: float ):
        self.index_max = p_nb_sprite
        self.img = pygame.image.load( p_path )
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_pos_x( self, p_pos_x ):
        self.pos_x = p_pos_x

    def set_pos_y( self, p_pos_y ):
        self.pos_y = p_pos_y

    def set_index( self, p_index ):
        self.index = p_index

    def set_index_max( self, p_index_max ):
        self.index_max = p_index_max

    def set_img( self, p_img ):
        self.img = p_img

    def get_pos_x( self ):
        return self.pos_x

    def get_pos_y( self ):
        return self.pos_y

    def get_index( self ):
        if self.index >= self.index_max:
            self.index = 0
        return self.index

    def get_index_max( self ):
        return self.index_max

    def get_img( self ):
        return self.img
