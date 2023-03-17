import pygame
from src.window.window import Window

class Player:
    PLAYER_SPEED: float = 3

    BULLET_SPEED: float = 4
    MAX_AMMO: int = 10

    def __init__( self, p_path_img_player: str, p_path_img_bullet: str, p_pos_x: float, p_pos_y: float ) -> None:
        self._img_player: any = pygame.image.load( p_path_img_player )
        self._img_bullet: any = pygame.image.load( p_path_img_bullet )
        self._pos_x: float = p_pos_x
        self._pos_y: float = p_pos_y
        self._speed: float = 0
        self._ammo: int = self.MAX_AMMO
        self._bullets: list[ list ] = [ ]

    def event_player( self, p_event ):
        if p_event.type == pygame.KEYDOWN:
            if p_event.key == pygame.K_LEFT:
                self.start_move_left()
            if p_event.key == pygame.K_RIGHT:
                self.start_move_right()
            if p_event.key == pygame.K_SPACE:
                if self.get_ammo() > 0:
                    self.fire()
        if p_event.type == pygame.KEYUP:
            if p_event.key == pygame.K_LEFT:
                self.stop_move_left()
            if p_event.key == pygame.K_RIGHT:
                self.stop_move_right()

    def start_move_left( self ) -> None:
        self._speed -= self.PLAYER_SPEED

    def stop_move_left( self ) -> None:
        self._speed += self.PLAYER_SPEED

    def start_move_right( self ) -> None:
        self._speed += self.PLAYER_SPEED

    def stop_move_right( self ) -> None:
        self._speed -= self.PLAYER_SPEED

    def fire( self ) -> None:
        self._bullets.append( [ self._pos_x, self._pos_y ] )
        self._ammo -= 1

    def reload( self ) -> None:
        if self._ammo < self.MAX_AMMO:
            self._ammo += 1

    def get_ammo( self ) -> int:
        return self._ammo

    def draw_player( self, p_window: Window ) -> None:
        self._pos_x += self._speed

        if self._pos_x <= p_window.get_boundary_left():
            self._pos_x = p_window.get_boundary_left()
        elif self._pos_x >= p_window.get_boundary_right():
            self._pos_x = p_window.get_boundary_right()

        p_window.draw( self._img_player, self._pos_x, self._pos_y )

    def draw_bullet( self, p_window: Window ):
        l_index: int = 0

        for l_bullet in self._bullets:
            l_bullet_pos_x: float = l_bullet[ 0 ]
            l_bullet_pos_y: float = l_bullet[ 1 ] - self.BULLET_SPEED
            p_window.draw( self._img_bullet, l_bullet_pos_x + 16, l_bullet_pos_y + 16 )
            self._bullets[ l_index ][ 1 ] -= self.BULLET_SPEED
            l_index += 1

    def check_bullet_out( self ):
        l_index: int = 0
        l_bullets = self._bullets

        for l_bullet in l_bullets:
            if l_bullet[ 1 ] <= 0:
                self.reload()
                del self._bullets[ l_index ]
            l_index += 1
