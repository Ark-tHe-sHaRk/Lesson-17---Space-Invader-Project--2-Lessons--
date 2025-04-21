#Importing Nessesary Libraries
import pygame
import random
import math

#Creating the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

#Initializing the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

#Setting the background 
background = pygame.image.load('background.png')

#Setting the caption and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Creating the player
player_img = pygame.image.Load('player.png')
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0 

#Creating the enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

#Creating the bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = 'ready'

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    #Display the current score on the screen
    score = font.render('Score: ', + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    #Display the game over text
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text,(200, 250))

def enemy(x, y, i):
    #Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    #Fire a bullet fomr the player position
    global bullet_state
    bullet_state = 'Fire'
    screen.blit(bulletImg, (x + 16, y + 10))