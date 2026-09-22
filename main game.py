import pygame
import sys
import random


pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_background = pygame.image.load("Backgroundfloor.png")
pygame.display.set_caption("Chrome Dinosaur Game")
clock = pygame.time.Clock()

GREY = (32, 33, 36)
NARDO = (162, 164, 168)

player_width = 67
player_height = 72
player_x = 400
player_y = 850
player_speed = 60

player2_width = 90
player2_height = 47
player2_x = 400
player2_y = 850
player2_speed = 60

playerdeath_width = 64
playerdeath_height = 72
playerdeath_x = 400
playerdeath_y = 850

enemy_width = 26
enemy_height = 50
enemy_x = 850
enemy_y = 850
enemy_speed = 10

enemy2_width = 76
enemy2_height = 56
enemy2_x = 1650
enemy2_y = 750
enemy2_speed = 10

dino_img = pygame.image.load("Dino.png")
dinoduck_img = pygame.image.load("DinoDuck.png")
dinodeath_img = pygame.image.load("DinoDeath.png")
dino_gravity = 0
dino = pygame.transform.scale(dino_img, (player_width, player_height))
dinoduck = pygame.transform.scale(dinoduck_img, (player2_width, player2_height))
dinodeath = pygame.transform.scale(dinodeath_img, (playerdeath_width, playerdeath_height))

cactus_img = pygame.image.load("cactus.png")
cactus = pygame.transform.scale(cactus_img, (enemy_width, enemy_height))

ptero_img = pygame.image.load("ptero.png")
ptero = pygame.transform.scale(ptero_img,(enemy2_width,enemy2_height))

gameover_img = pygame.image.load("GameOver.png")
gameover_width = 257    
gameover_height = 72
gameover_x = 840
gameover_y = 550
gameover = pygame.transform.scale(gameover_img, (gameover_width, gameover_height))
gameover_rect = pygame.Rect(gameover_x, gameover_y, gameover_width, gameover_height)

start_ticks = pygame.time.get_ticks()
font = pygame.font.SysFont("Arial", 30, bold=True)
game_over = False
running = True
duck = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if ((keys[pygame.K_UP] or keys[pygame.K_SPACE])) and player_y >= 850:
            dino_gravity = -20
        duck = keys[pygame.K_DOWN] and player_y >= 850

    screen.fill(GREY)
    screen.blit(screen_background, (300,800))
    screen.blit(cactus, (enemy_x, enemy_y))
    screen.blit(ptero, (enemy2_x,enemy2_y))

    if not game_over:
        enemy_x -= enemy_speed
        if enemy_x < -enemy_width:
            enemy_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
        enemy_speed += 0.00001
        current_score = (pygame.time.get_ticks() - start_ticks) // 100
        
        if  current_score >= 450:
            enemy2_x -= enemy2_speed
            if enemy2_x < -enemy2_width:
                enemy2_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
                enemy2_y = random.randint(600,750)
            enemy2_speed += 0.0000000001

    player_rect = pygame.Rect(player_x,player_y,player_width,player_height)
    playerdeath_rect = pygame.Rect(playerdeath_x,playerdeath_y,playerdeath_width,playerdeath_height)
    enemy_rect = pygame.Rect(enemy_x,enemy_y,enemy_width,enemy_height)
    enemy2_rect = pygame.Rect(enemy2_x,enemy2_y,enemy2_width,enemy2_height)
    if player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy2_rect):
        game_over = True
    
    dino_gravity += 1
    player_y += dino_gravity
    if player_y >= 850:
        player_y = 850
        dino_gravity = 0
        
    if duck:
        duck_y = player_y + (player_height - player2_height)  # keep feet on the ground
        player_rect = pygame.Rect(player_x, duck_y, player2_width, player2_height)
        screen.blit(dinoduck, player_rect)
    else:
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        screen.blit(dino, player_rect)

    if not game_over:
        score_surf = font.render(f"{current_score}", True, NARDO)
        message_x = 1515
        message_y = 200
        over_surf = font.render(f"HI  {current_score}", True, NARDO)
        text_x = 1415
        text_y = 200
        screen.blit(over_surf, (text_x, text_y))
        screen.blit(score_surf, (message_x,message_y))
    else:
        screen.blit(over_surf, (text_x, text_y))
        screen.blit(score_surf, (message_x,message_y))
        screen.blit(dinodeath_img,playerdeath_rect)
        screen.blit(gameover, (gameover_x,gameover_y))
    

    if event.type == pygame.MOUSEBUTTONDOWN:
        if gameover_rect.collidepoint(960,600):
            player_x = 400
            player_y = 850
            enemy_x = 100
            enemy2_x = 1650
            enemy2_y = 750
            start_ticks = pygame.time.get_ticks()
            current_score = 0
            running = True
            game_over = False
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
