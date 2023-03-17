import pygame
from src.window.window import Window
from src.player.player import Player
from src.enemy.enemy import Enemy

def make_enemies(
        p_path_enemy_img: str, p_nb_enemies: int, p_hp: int, p_height: int, p_width: int, p_window: Window
        ) -> list[ Enemy ]:
    l_enemies: list[ Enemy ] = [ ]
    l_enemy_pos_x: int = 0
    l_enemy_pos_y: int = 0 - p_height

    for l_index in range( p_nb_enemies ):
        l_enemies.append(
                Enemy( p_path_enemy_img, p_hp, l_enemy_pos_x, l_enemy_pos_y )
                )

    return l_enemies

def main() -> int:
    l_running: bool = True
    pygame.init()

    l_window: Window = Window( 600, 800 )
    l_window.set_icon( "resources/images/vaisseau-spatial.png" )
    l_window.set_title( "Space Invader" )
    l_window.set_background( "resources/images/space_bg.png" )

    l_player: Player = Player( "resources/images/vaisseau-spatial-joueur.png", "resources/images/bullet.png", 370, 480 )
    l_enemies: list[ Enemy ] = make_enemies( "resources/images/ovni.png", 3, 1, 64, 64, l_window )

    while l_running:
        l_window.reset_window()
        l_window.draw_background()

        for l_event in pygame.event.get():
            l_running = l_window.event_window( l_event )
            l_player.event_player( l_event )

        l_player.draw_player( l_window )
        l_player.draw_bullet( l_window )
        l_player.check_bullet_out()

        l_window.update_window()

    return 0
