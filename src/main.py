import pygame
from src.window.window import Window
from src.player.player import Player

def main() -> int:
    l_running: bool = True
    pygame.init()

    l_window: Window = Window( 600, 800 )
    l_window.set_icon( "resources/images/vaisseau-spatial.png" )
    l_window.set_title( "Space Invader" )
    l_window.set_background( "resources/images/space_bg.png" )

    l_player: Player = Player( "resources/images/vaisseau-spatial-joueur.png", "resources/images/bullet.png", 370, 480 )

    while l_running:
        l_window.reset_window()
        l_window.draw_background()

        for l_event in pygame.event.get():
            l_running = l_window.event_window( l_event )
            l_player.event_player( l_event )
            if l_event.type == pygame.KEYDOWN:
                if l_event.key == pygame.K_SPACE:
                    if l_player.get_ammo() > 0:
                        l_player.fire()

        l_player.draw_player( l_window )
        l_player.draw_bullet( l_window )
        l_player.check_bullet_out()

        l_window.update_window()

    return 0
