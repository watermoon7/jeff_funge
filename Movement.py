import pygame
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
        

    def enemy_movement(self, blocks, dis, dt):
        for block in blocks:
             if pygame.Rect.colliderect(self.obj.rect, block.rect):
                 if self.obj.rect.right > block.rect.left and self.obj.direction[0] == 1:
                     self.obj.rect.x -= 0.88*dis
                 elif self.obj.rect.left < block.rect.right and self.obj.direction[0] == -1:
                     self.obj.rect.x += 1.12*dis

        self.obj.vy += 0.1 * dt
        if self.obj.vy > 0:
            self.obj.direction[1] = -1  
            if self.obj.vy > 20:
                self.obj.vy = 20
        self.obj.rect.y += self.obj.vy

        for block in blocks:
            if pygame.Rect.colliderect(self.obj.rect, block.rect):
                self.obj.vy = 0
                if self.obj.rect.bottom > block.rect.top and self.obj.direction[1] == -1:
                    self.obj.stationary = 1
                    self.obj.rect.bottom = block.rect.top
                    self.obj.direction[1] = 0
                elif self.obj.rect.top < block.rect.bottom and self.obj.direction[1] == 1:
                    self.obj.rect.top = block.rect.bottom
