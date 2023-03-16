import pygame

class Window:
    BASIC_HEIGHT: float = 600
    BASIC_WIDTH: float = 800
    RGB_BLACK: tuple[ int ] = (0, 0, 0)

    def __init__( self, p_height: float, p_width: float ) -> None:
        self._bg: any = None
        self._icon: any = None
        self._title: str = ""
        self._boundary_left: int = 0
        self._boundary_right: int = 735
        self._boundary_up: int = 0
        self._boundary_down: int = 535
        self._window: any = self.create_window( p_height, p_width )

    def create_window( self, p_height: float = 0, p_width: float = 0 ) -> any:
        if p_width == p_width == 0:
            p_width = self.BASIC_WIDTH
            p_height = self.BASIC_HEIGHT
        return pygame.display.set_mode( (p_width, p_height) )

    def reset_window( self ) -> None:
        self.color_window( self.RGB_BLACK )

    def update_window( self ) -> None:
        pygame.display.update()

    def color_window( self, p_rgb ) -> None:
        self._window.fill( p_rgb )

    def draw( self, p_element: any, p_pos_x: float, p_pos_y: float ) -> None:
        self._window.blit( p_element, (p_pos_x, p_pos_y) )

    def draw_background( self ):
        self.draw( self._bg, 0, 0 )

    def event_window( self, p_event ):
        if p_event.type == pygame.QUIT:
            return False
        return True

    def set_icon( self, p_path: str ) -> None:
        self._icon = pygame.image.load( p_path )
        pygame.display.set_icon( self._icon )

    def set_background( self, p_path: str ) -> None:
        self._bg = pygame.image.load( p_path )

    def set_title( self, p_title: str ) -> None:
        self._title = p_title
        pygame.display.set_caption( p_title )

    def get_boundary_left( self ) -> int:
        return self._boundary_left

    def get_boundary_right( self ) -> int:
        return self._boundary_right

    def get_boundary_up( self ) -> int:
        return self._boundary_up

    def get_boundary_down( self ) -> int:
        return self._boundary_down
