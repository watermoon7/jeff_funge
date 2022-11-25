import pygame, sys, threading, time
from sys import exit
from Camera import Camera
from shop_menu import run
from random import randint as r
from Levels import *
from Inbound import *
pygame.init()

class Movement():
    def __init__(self, obj):
        self.obj = obj

    def horizontal_collision(self, blocks, dis):
            for block in blocks:
                if pygame.Rect.colliderect(self.obj.rect, block.rect):
                    if self.obj.rect.right > block.rect.left and self.obj.direction[0] == 1:
                         self.obj.rect.x -= 0.88*dis
                    elif self.obj.rect.left < block.rect.right and self.obj.direction[0] == -1:
                         self.obj.rect.x += 1.12*dis

    def vertical_collision(self, blocks, dis):
        for block in blocks:
            if pygame.Rect.colliderect(self.obj.rect, block.rect):
                if self.obj.rect.bottom > block.rect.top and self.obj.direction[1] == -1:
                    self.obj.rect.bottom = block.rect.top
                    self.obj.direction[1] = 0
                    self.obj.stationary = 1
                    self.obj.vy = 0
                elif self.obj.rect.top < block.rect.bottom and self.obj.direction[1] == 1:
                    self.obj.rect.top = block.rect.bottom
                    self.obj.vy = 0
    
    def player_movement(self, blocks, dis, dt, offset):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.obj.rect.x += dis - offset
                self.obj.direction[0] = 1
            elif keys[pygame.K_a]:
                self.obj.rect.x -= dis + offset
                self.obj.direction[0] = -1
            else:
                self.obj.direction[0] = 0
            self.horizontal_collision(blocks, dis)
            
            self.obj.vy += 0.1 * dt
            if self.obj.vy > 0:
                self.obj.direction[1] = -1  
                if self.obj.vy > 20:
                    self.obj.vy = 20
            self.obj.rect.y += self.obj.vy
            self.vertical_collision(blocks, dis)

class playerClass(Movement):
    def __init__(self, rect):
        self.rect = rect
        self.vx = 0.4
        self.vy = 0
        self.direction = [0,0]
        
        still1 = pygame.transform.scale(pygame.image.load('player_1.png').convert_alpha(), (30, 50))
        still2 = pygame.transform.scale(pygame.image.load('player_2.png').convert_alpha(), (30, 50))
        still3 = pygame.transform.scale(pygame.image.load('player_3.png').convert_alpha(), (30, 50))
        still4 = pygame.transform.scale(pygame.image.load('player_4.png').convert_alpha(), (30, 50))
        self.stillimgs = [still1, still2, still3, still4]

        left1 = pygame.transform.scale(pygame.image.load('player_left_1.png').convert_alpha(), (30, 50))
        left2 = pygame.transform.scale(pygame.image.load('player_left_2.png').convert_alpha(), (30, 50))
        self.leftimgs = [left1, left2]

        right1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('player_left_1.png').convert_alpha(), (30, 50)), 1, 0)
        right2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('player_left_2.png').convert_alpha(), (30, 50)), 1, 0)
        self.rightimgs = [right1, right2]
                
        self.stationary = 1
        super().__init__(self)

    def draw(self, screen):
        if self.direction[0] == -1:
            screen.blit(self.leftimgs[r(0, len(self.leftimgs)-1)], self.rect)
        elif self.direction[0] == 1:
            screen.blit(self.rightimgs[r(0, len(self.rightimgs)-1)], self.rect)
        else:
            screen.blit(self.stillimgs[r(0, len(self.stillimgs)-1)], self.rect)

class blockClass():
    def __init__(self, x, y, image, btype, enemy = False):
        self.btype = btype
        self.rect = pygame.Rect(x, y, 60, 60)
        self.image = image
        self.pos = [x, y]
        self.x = x
        self.y = y
        self.enemy = enemy

class enemy():
    def __init__(self, rect, x, y, hp):
        self.rect = rect

class coinClass():
    def __init__(self, x, y, image):
        self.rect = pygame.Rect(x, y, 60, 60)
        self.image = image
        self.pos = [x, y]
        self.x = x
        self.y = y
        self.collected = False

w = 1080
h = 720
screen = pygame.display.set_mode((w, h))

offset = 0


player = playerClass(pygame.rect.Rect(540, 540, 30, 50))

level = 0
levels = [level1, level2, level3, level4]

ground1 = pygame.image.load('ground1.png')
ground2 = pygame.image.load('ground 4.png')
ground3 = pygame.image.load('ground3.png')
coin1 = pygame.image.load('coin.png')
theo = pygame.image.load('theo.png')

bc = 0
cc = 0

def get_blocks(level):
    global bc, cc
    blocks = []
    coins = []
    for i in range(len(list(level))):
        for o in range(len(level[0])):
            if level[i][o] == 'b':
                globals()['block{}_platform'.format(bc)] = blockClass(o*60, i*60, ground2, 'b')
                blocks.append(globals()['block{}_platform'.format(bc)])
                bc += 1
            elif level[i][o] == '1':
                globals()['block{}_overground'.format(bc)] = blockClass(o*60, i*60, ground3, '1')
                blocks.append(globals()['block{}_overground'.format(bc)])
                bc += 1
            elif level[i][o] == '#':
                globals()['block{}_underground'.format(bc)] = blockClass(o*60, i*60, ground2, '#')
                blocks.append(globals()['block{}_underground'.format(bc)])
                bc += 1
            elif level[i][o] == 'c':
                globals()['block{}_underground'.format(cc)] = coinClass(o*60, i*60, coin1)
                coins.append(globals()['block{}_underground'.format(cc)])
                cc += 1
    return (blocks, coins)

def new_level(level):
    global blocks, coins
    blocks, coins = get_blocks(level)
    
blocks = coins = []

clock = pygame.time.Clock()
running = True
run()
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and player.vy == 0:
                player.vy = -26
                player.direction[1] = 1
                player.stationary = 0
    
    dt = clock.tick(60)            
    screen.fill((255, 255, 255))
    dis = player.vx * dt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        offset = dis
        for block in blocks:
            block.rect.x -= offset
        for coin in coins:
            coin.rect.x -= offset
    elif keys[pygame.K_a]:
        offset = -dis
        for block in blocks:
            block.rect.x -= offset
        for coin in coins:
            coin.rect.x -= offset
            
    player.player_movement(blocks, dis, dt, offset)
    
    for block in blocks:
        screen.blit(block.image, [block.rect.x, block.rect.y])
    
    for i, coin in enumerate(coins):
        screen.blit(coin.image, [coin.rect.x, coin.rect.y])
        if pygame.Rect.colliderect(player.rect, coin.rect):
            coins.pop(i)
    
    player.draw(screen)
    pygame.display.update()

    if len(coins) == 0:
        try:
            new_level(levels[level])
        except:
            new_level(levele)
        level += 1
            
    
    
