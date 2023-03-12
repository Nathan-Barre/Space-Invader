import pygame

class Window:
    BASIC_HEIGHT: float = 600
    BASIC_WIDTH: float = 800
    RGB_BLACK: tuple[ int ] = (0, 0, 0)

    def __init__( self, p_height: float, p_width: float ) -> None:
        self.icon: any = None
        self.title: str
        self.window: any = self.create_window( p_height, p_width )

    def create_window( self, p_height: float = 0, p_width: float = 0 ):
        if p_width == p_width == 0:
            p_width = self.BASIC_WIDTH
            p_height = self.BASIC_HEIGHT
        return pygame.display.set_mode( (p_width, p_height) )

    def reset_window( self ) -> None:
        self.color_window( self.RGB_BLACK )

    def color_window( self, p_rgb ) -> None:
        self.window.fill( p_rgb )

    def draw( self, p_element: any, p_pos_x: float, p_pos_y: float ) -> None:
        self.window.blit( p_element, (p_pos_x, p_pos_y) )

    def set_icon( self, p_path: str ) -> None:
        self.icon = pygame.image.load( p_path )
        pygame.display.set_icon( self.icon )

    def set_title( self, p_title: str ):
        self.title = p_title
        pygame.display.set_caption( p_title )
