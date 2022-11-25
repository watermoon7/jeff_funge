import pygame
pygame.init()
w = 1080
h = 720
screen = pygame.display.set_mode((w, h))




''' IMGS '''
ground1 = [pygame.image.load('ground_plain.png')]

ground2_t = pygame.image.load('ground_top.png')
ground2_l = pygame.transform.rotate(pygame.image.load('ground_top.png'), 90)
ground2_b = pygame.transform.rotate(pygame.image.load('ground_top.png'), 180)
ground2_r = pygame.transform.rotate(pygame.image.load('ground_top.png'), 270)
ground2 = [ground2_t, ground2_l, ground2_b, ground2_r]

ground3_t = pygame.image.load('ground_top_side.png')
ground3_l = pygame.transform.rotate(pygame.image.load('ground_top_side.png'), 90)
ground3_b = pygame.transform.rotate(pygame.image.load('ground_top_side.png'), 180)
ground3_r = pygame.transform.rotate(pygame.image.load('ground_top_side.png'), 270)
ground3 = [ground3_t, ground3_l, ground3_b, ground3_r]

ground4_t = pygame.image.load('ground_side_top_side.png')
ground4_l = pygame.transform.rotate(pygame.image.load('ground_side_top_side.png'), 90)
ground4_b = pygame.transform.rotate(pygame.image.load('ground_side_top_side.png'), 180)
ground4_r = pygame.transform.rotate(pygame.image.load('ground_side_top_side.png'), 270)
ground4 = [ground4_t, ground4_l, ground4_b, ground4_r]

ground5 = [pygame.image.load('ground_full.png')]


coin = pygame.image.load('coin.png')
theo = pygame.image.load('theo.png')

still1 = pygame.transform.scale(pygame.image.load('player_1.png').convert_alpha(), (30, 50))
still2 = pygame.transform.scale(pygame.image.load('player_2.png').convert_alpha(), (30, 50))
still3 = pygame.transform.scale(pygame.image.load('player_3.png').convert_alpha(), (30, 50))
still4 = pygame.transform.scale(pygame.image.load('player_4.png').convert_alpha(), (30, 50))
still_imgs = [still1, still2, still3, still4]

left1 = pygame.transform.scale(pygame.image.load('player_left_1.png').convert_alpha(), (30, 50))
left2 = pygame.transform.scale(pygame.image.load('player_left_2.png').convert_alpha(), (30, 50))
left_imgs = [left1, left2]

right1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('player_left_1.png').convert_alpha(), (30, 50)), 1, 0)
right2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('player_left_2.png').convert_alpha(), (30, 50)), 1, 0)
right_imgs = [right1, right2]
