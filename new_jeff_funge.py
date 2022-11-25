import pygame
from copy import deepcopy
from sys import exit
from Levels import *
from settings import *
from random import randint as r
pygame.init()

class Player():
    def __init__(self, rect):
        self.new = deepcopy(rect)
        self.rect = rect
        self.vx = 0.5
        self.vy = 0
        self.direction = [0,0]
        self.img = theo

    def draw(self, screen):
        if self.direction[0] == -1:
            screen.blit(left_imgs[r(0, len(left_imgs)-1)], self.rect)
        elif self.direction[0] == 1:
            screen.blit(right_imgs[r(0, len(right_imgs)-1)], self.rect)
        else:
            screen.blit(still_imgs[r(0, len(still_imgs)-1)], self.rect)
            
class Block():
    def __init__(self, x, y, image, b_id):
        self.b_id = b_id
        self.rect = pygame.Rect(x, y, 60, 60)
        self.image = image

def new_level(level):
    def check_rotation(pos, imgs):
        ### 0 = top, 1 = left, 2 = bottom, 3 = right
        pass

    blocks = []
    coins = []
    b_imgs = {'1':ground1, '2':ground2, '3':ground3, '4':ground4, '5':ground5, 'c':coin}
    for a, i in enumerate(level):
        for b, o in enumerate(i):
            if o == 'c':
                b_id = o
                coins.append(Block(b*60, a*60, b_imgs[b_id], b_id))
            elif o != ' ':
                b_id = o
                blocks.append(Block(b*60, a*60, b_imgs[b_id][0], b_id))

    return [blocks, coins]

def collided(blocks, player, extra = 0):
    if extra != 0:
        return True
    for block in blocks:
        if player.new.colliderect(block.rect):
            return True
    return False

def draw_lives(screen, lives):
    for i in range(lives):
        a = pygame.draw.rect(screen, (240, 20, 30), ((1030-i*40) ,20, 30, 30))


blocks, coins = new_level(level1)
player = Player(pygame.rect.Rect(540, 540, 30, 50))
jump = False
extra = 0


def reset():
    blocks = coins = []
    blocks, coins = new_level(level1)
    player = Player(pygame.rect.Rect(540, 540, 30, 50))
    jump = False
    extra = 0
    for i in dir(coins[0]):
        print(i, type(i))

lives = 3

running = True
clock = pygame.time.Clock()
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and jump:
                player.direction[1] = 1
                player.vy = -18
                jump = False
    
    pygame.display.set_caption(str(clock.get_fps()))
    dt = clock.tick(60)
    dis = player.vx * 16
    screen.fill((255, 255, 255))
    player.new = deepcopy(player.rect)
    draw_lives(screen, lives)
    
    extra = 0
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if player.rect.x > 880:
            extra = -dis
        player.new.x += dis
    elif keys[pygame.K_a]:
        if player.rect.x < 200:
            extra = dis
        player.new.x -= dis

    if not collided(blocks, player, extra):
        player.rect = deepcopy(player.new)
    if collided(blocks, player):
       extra = 0
        
    player.new = deepcopy(player.rect)
    
    player.new.y += player.vy
    player.vy += 0.98
    if player.vy > 20:
        player.vy = 20

    for block in blocks:
        block.rect.x += extra
        screen.blit(block.image, [block.rect.x, block.rect.y])

    
    for coin in coins:
        coin.rect.x += extra
        screen.blit(coin.image, [coin.rect.x, coin.rect.y])
        if player.rect.colliderect(coin.rect):
            coins.remove(coin)
    
    if not collided(blocks, player):
        player.rect = deepcopy(player.new)
    else:
        if player.vy > 0:
            jump = True
        player.vy = 0
        
        
    player.draw(screen)
    
    if jump:
        pygame.draw.circle(screen, (0, 255, 0), (50, 50), 30)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (50, 50), 30)
    
    pygame.display.update()
    
    if player.rect.y > 800: player.rect.y = -100; lives -= 1
    if lives == 0:
        pygame.quit()
        exit()
