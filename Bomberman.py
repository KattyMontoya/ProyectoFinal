import pygame
import sys
  
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (125, 125, 125)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
VIOLETA = (255, 0, 255)
  
##class Bomba(pygame.sprite.Sprite):
##
##    def __init__(self, event):
##
##        super().__init__()
##
##        self.sheet = pygame.image.load('bomb.png')
 
class Pared(pygame.sprite.Sprite):
    """Esta clase representa la barra inferior que controla el protagonista """
     
    def __init__(self, x, y, largo, alto, color):
        """ Función Constructor """
         
        # Llama al constructor padre
        super().__init__()
  
        # Crea una pared AZUL, con las dimensiones especificadas en los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
  
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el 
    protagonista """
     
    # Establecemos el vector velocidad
    cambio_x = 0
    cambio_y = 0
  
    def __init__(self, position):
        cambio_x = 0
        cambio_y = 0
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

        """ Función Constructor """
 
        # Llama al constructor padre
        super().__init__()

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
            self.rect.x -= 5
        if direction == 'right':
            self.corte(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.corte(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.corte(self.down_states)
            self.rect.y += 5
 
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
        #if event.type == pygame.QUIT:
         #   game_over = True
 
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
            if event.key == ord('a'):
                pygame.image.load('bomb.png')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
            if event.key == ord('a'):
                pygame.image.load('bomb.png')
       
    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. Es llamada con una pulsación del teclado. """
        self.cambio_x += x
        self.cambio_y += y
          
    def mover(self, paredes):
        """ Encuentra una nueva posición para el protagonista """
         
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
         
        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, paredes, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado.
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            else:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
  
        # Desplazar arriba/izquierda
        self.rect.y += self.cambio_y
          
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, paredes, False) 
        for bloque in lista_impactos_bloques:
                 
            # Reseteamos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            else:
                self.rect.top = bloque.rect.bottom            
  

    
