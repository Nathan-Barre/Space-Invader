import pygame
import random

BOUNDARY_LEFT = 0
BOUNDARY_RIGHT = 736
BOUNDARY_UP = 0
BOUNDARY_DOWN = 536

ENEMY_SPEED_X: float = 1
ENEMY_SPEED_Y: float = 32

PLAYER_SPEED: float = 1.5

BULLET_SPEED: float = 2

def fire_bullet( p_bullet_img, p_bullet_x: float, p_bullet_y: float ):
    global l_bullet_state
    l_bullet_state = "fire"
    l_window.blit( p_bullet_img, (p_bullet_x + 16, p_bullet_y + 20) )

def player( p_player_img, p_player_x: float, p_player_y: float ):
    l_window.blit( p_player_img, (p_player_x, p_player_y) )

def enemy( p_enemy_img, p_enemy_x: float, p_enemy_y: float ):
    l_window.blit( p_enemy_img, (p_enemy_x, p_enemy_y) )

if __name__ == '__main__':
    # init du jeu
    pygame.init()

    # init la fenetre de jeu
    l_window = pygame.display.set_mode( (800, 600) )

    # windows name and logo
    l_icon = pygame.image.load( "resources/vaisseau-spatial.png" )
    pygame.display.set_caption( "Space Invader" )
    pygame.display.set_icon( l_icon )

    # Background
    l_bg = pygame.image.load( "resources/space_bg.png" )

    # Player
    l_player_img = pygame.image.load( "resources/vaisseau-spatial-joueur.png" )
    l_player_x: float = 370
    l_player_y: float = 480
    l_player_x_speed: float = 0

    # Enemy
    l_enemy_img = pygame.image.load( "resources/ovni.png" )
    l_enemy_x: float = random.randint( BOUNDARY_LEFT, BOUNDARY_RIGHT )
    l_enemy_y: float = random.randint( BOUNDARY_UP, 150 )
    l_enemy_x_speed: float = ENEMY_SPEED_X

    # Bullet
    l_bullet_img = pygame.image.load( "resources/bullet.png" )
    l_bullet_x: float = 0
    l_bullet_y: float = 480
    l_bullet_x_speed: float = 0
    l_bullet_y_speed: float = BULLET_SPEED
    l_bullet_state: str = "ready"

    # game loop
    l_running = True
    while l_running:

        # RGB
        l_window.fill( (0, 0, 0) )
        # Background
        l_window.blit( l_bg, (0, 0) )

        for l_event in pygame.event.get():
            if l_event.type == pygame.QUIT:
                l_running = False
            if l_event.type == pygame.KEYDOWN:
                if l_event.key == pygame.K_LEFT:
                    l_player_x_speed -= PLAYER_SPEED
                if l_event.key == pygame.K_RIGHT:
                    l_player_x_speed += PLAYER_SPEED
                if l_event.key == pygame.K_SPACE:
                    if l_bullet_state == "ready":
                        l_bullet_x = l_player_x
                        fire_bullet( l_bullet_img, l_bullet_x, l_player_y )
            if l_event.type == pygame.KEYUP:
                if l_event.key == pygame.K_LEFT or l_event.key == pygame.K_RIGHT:
                    l_player_x_speed = 0

        # check player pos
        l_player_x += l_player_x_speed
        if l_player_x <= BOUNDARY_LEFT:
            l_player_x = BOUNDARY_LEFT
        elif l_player_x >= BOUNDARY_RIGHT:
            l_player_x = BOUNDARY_RIGHT

        # check player pos X
        l_enemy_x += l_enemy_x_speed
        if l_enemy_x <= BOUNDARY_LEFT:
            l_enemy_x += ENEMY_SPEED_X
            l_enemy_x_speed *= -1
            l_enemy_y += ENEMY_SPEED_Y
        elif l_enemy_x >= BOUNDARY_RIGHT:
            l_enemy_x -= ENEMY_SPEED_X
            l_enemy_x_speed *= -1
            l_enemy_y += ENEMY_SPEED_Y

        # check bullet pos
        if l_bullet_y <= 0:
            l_bullet_y = 480
            l_bullet_state = "ready"

        if l_bullet_state == "fire":
            fire_bullet( l_bullet_img, l_bullet_x, l_bullet_y )
            l_bullet_y -= l_bullet_y_speed

        # Player Enemy
        player( l_player_img, l_player_x, l_player_y )
        enemy( l_enemy_img, l_enemy_x, l_enemy_y )
        pygame.display.update()
