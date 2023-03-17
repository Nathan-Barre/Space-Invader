import pygame
from src.sound.sound import Sound
from src.window.window import Window

class Enemy:
    SPEED_X: float = 2
    SPEED_Y: float = 32

    def __init__( self, p_path_enemy_img: str, p_hp: int, p_pos_x: float, p_pos_y: float ) -> None:
        self._sound: Sound
        self._img: str = p_path_enemy_img
        self._hp: int = p_hp
        self._speed_x: float = self.SPEED_X
        self._speed_y: float = self.SPEED_Y
        self._pos_x: float = p_pos_x
        self._pos_y: float = p_pos_y
        self._direction: str = "right"

    def move( self ) -> None:
        self._pos_x += self._speed_x

    def check_boundary( self, p_window: Window ) -> bool:
        if self._pos_x <= p_window.get_boundary_left() or self._pos_x >= p_window.get_boundary_right():
            return True
        return False

    def change_move( self, p_window: Window ):
        self._speed_x *= -1

        if self._direction == "right":
            self._direction = "left"

            if self._pos_x >= p_window.get_boundary_right():
                self._pos_x -= self.SPEED_X
                self._pos_y += self._speed_y
        else:
            self._direction = "right"

            if self._pos_x <= p_window.get_boundary_left():
                self._pos_x += self.SPEED_X
                self._pos_y += self._speed_y

    def draw_player( self, p_window: Window ) -> None:
        p_window.draw( self._img, self._pos_x, self._pos_y )
