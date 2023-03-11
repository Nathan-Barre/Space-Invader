import pygame
import random
import math
from pygame import mixer

BOUNDARY_LEFT = 0
BOUNDARY_RIGHT = 735
BOUNDARY_UP = 0
BOUNDARY_DOWN = 535

ENEMY_SPEED_X: float = 1
ENEMY_SPEED_Y: float = 32

PLAYER_SPEED: float = 1.5

BULLET_SPEED: float = 2

def game_over_text( p_pos_x, p_pos_y, p_font ):
    l_game_over = p_font.render( "GAME OVER", True, (255, 255, 255) )
    l_window.blit( l_game_over, (p_pos_x, p_pos_y) )

def show_score( p_pos_x, p_pos_y, p_font, p_score_value ):
    l_score = p_font.render( "Score : " + str( p_score_value ), True, (255, 255, 255) )
    l_window.blit( l_score, (p_pos_x, p_pos_y) )

def fire_bullet( p_bullet_img, p_bullet_x: float, p_bullet_y: float ):
    global l_bullet_state
    l_bullet_state = "fire"
    l_window.blit( p_bullet_img, (p_bullet_x + 16, p_bullet_y + 20) )

def player( p_player_img, p_player_x: float, p_player_y: float ):
    l_window.blit( p_player_img, (p_player_x, p_player_y) )

def enemy( p_enemy_img, p_enemy_x: float, p_enemy_y: float ):
    l_window.blit( p_enemy_img, (p_enemy_x, p_enemy_y) )

def is_collision( p_enemy_x: float, p_enemy_y: float, p_bullet_x: float, p_bullet_y: float ):
    l_range = math.sqrt( (math.pow( p_enemy_x - p_bullet_x, 2 )) + (math.pow( p_enemy_y - p_bullet_y, 2 )) )
    if l_range < 27:
        return True
    return False

if __name__ == '__main__':
    # init du jeu
    pygame.init()

    # init la fenetre de jeu
    l_window = pygame.display.set_mode( (800, 600) )

    # windows name and logo
    l_icon = pygame.image.load( "resources/images/vaisseau-spatial.png" )
    pygame.display.set_caption( "Space Invader" )
    pygame.display.set_icon( l_icon )

    # Background
    l_bg = pygame.image.load( "resources/images/space_bg.png" )
    mixer.music.load( "resources/sounds/background.wav" )
    mixer.music.play( -1 )

    # Player
    l_player_img = pygame.image.load( "resources/images/vaisseau-spatial-joueur.png" )
    l_player_x: float = 370
    l_player_y: float = 480
    l_player_x_speed: float = 0

    # Enemy
    l_enemies_img: list = [ ]
    l_enemies_x: list = [ ]
    l_enemies_y: list = [ ]
    l_enemies_x_speed: list = [ ]
    l_enemies_number: int = 6

    for i in range( l_enemies_number ):
        l_enemies_img.append( pygame.image.load( "resources/images/ovni.png" ) )
        l_enemies_x.append( random.randint( BOUNDARY_LEFT, BOUNDARY_RIGHT ) )
        l_enemies_y.append( random.randint( BOUNDARY_UP, 150 ) )
        l_enemies_x_speed.append( ENEMY_SPEED_X )

    # Bullet
    l_bullet_img = pygame.image.load( "resources/images/bullet.png" )
    l_bullet_x: float = 0
    l_bullet_y: float = 480
    l_bullet_x_speed: float = 0
    l_bullet_y_speed: float = BULLET_SPEED
    l_bullet_state: str = "ready"

    # Score
    l_score_value: int = 0
    l_score_font = pygame.font.Font( "freesansbold.ttf", 32 )
    l_score_pos_x: float = 10
    l_score_pos_y: float = 10

    # Game Over
    l_game_over_font = pygame.font.Font( "freesansbold.ttf", 64 )

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
                        l_bullet_sound = mixer.Sound( "resources/sounds/laser.wav" )
                        l_bullet_sound.play()
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

        # Enemies
        for i in range( l_enemies_number ):
            # Game Over
            if l_enemies_y[ i ] > 440:
                for j in range( l_enemies_number ):
                    l_enemies_y[ j ] = 2000
                game_over_text( 200, 250, l_game_over_font )
                break

            # check enemies pos
            l_enemies_x[ i ] += l_enemies_x_speed[ i ]
            if l_enemies_x[ i ] <= BOUNDARY_LEFT:
                l_enemies_x[ i ] += ENEMY_SPEED_X
                l_enemies_x_speed[ i ] *= -1
                l_enemies_y[ i ] += ENEMY_SPEED_Y
            elif l_enemies_x[ i ] >= BOUNDARY_RIGHT:
                l_enemies_x[ i ] -= ENEMY_SPEED_X
                l_enemies_x_speed[ i ] *= -1
                l_enemies_y[ i ] += ENEMY_SPEED_Y

            # Collision
            l_collision = is_collision( l_enemies_x[ i ], l_enemies_y[ i ], l_bullet_x, l_bullet_y )
            if l_collision:
                l_explosion_sound = mixer.Sound( "resources/sounds/explosion.wav" )
                l_explosion_sound.play()
                l_bullet_y = 480
                l_bullet_state = "ready"
                l_score_value += 1
                l_enemies_x[ i ] = random.randint( BOUNDARY_LEFT, BOUNDARY_RIGHT )
                l_enemies_y[ i ] = random.randint( BOUNDARY_UP, 150 )

        # check bullet pos
        if l_bullet_y <= 0:
            l_bullet_y = 480
            l_bullet_state = "ready"

        if l_bullet_state == "fire":
            fire_bullet( l_bullet_img, l_bullet_x, l_bullet_y )
            l_bullet_y -= l_bullet_y_speed

        # Player Enemy
        show_score( l_score_pos_x, l_score_pos_y, l_score_font, l_score_value )
        player( l_player_img, l_player_x, l_player_y )
        for i in range( l_enemies_number ):
            enemy( l_enemies_img[ i ], l_enemies_x[ i ], l_enemies_y[ i ] )
        pygame.display.update()
