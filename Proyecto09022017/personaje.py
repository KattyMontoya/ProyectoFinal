import pygame
 
class Persona(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('Bomber.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 232, 57, 80), 1: (56, 232 ,56, 79), 2: (160, 232, 56, 80) }
        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
 
    def obt_marco(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def corte(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.obt_marco(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
       
    def update(self, direction):
        if direction == 'left':
            self.corte(self.left_states)
            self.rect.x -= 10
        if direction == 'right':
            self.corte(self.right_states)
            self.rect.x += 10
        if direction == 'up':
            self.corte(self.up_states)
            self.rect.y -= 10
        if direction == 'down':
            self.corte(self.down_states)
            self.rect.y += 10
 
        if direction == 'stand_left':
            self.corte(self.left_states[0])
        if direction == 'stand_right':
            self.corte(self.right_states[0])
        if direction == 'stand_up':
            self.corte(self.up_states[0])
        if direction == 'stand_down':
            self.corte(self.down_states[0])
 
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 
    def teclado(self, event):
        if event.type == pygame.QUIT:
            game_over = True
 
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
