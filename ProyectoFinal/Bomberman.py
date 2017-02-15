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

class Cuarto():
    """ Clase base para todos los cuartos. """
     
    #Cada cuarto tiene una lista de paredes, y de los sprites enemigos.
    pared_lista = None
    sprites_enemigos = None
     
    def __init__(self):
        """ Constructor, creamos nuestras listas. """
        self.pared_lista = pygame.sprite.Group()
        self.sprites_enemigos = pygame.sprite.Group()
     
class Cuarto1(Cuarto):
    """Esto crea todas las paredes del cuarto 1"""
    def __init__(self):
        super().__init__()
        # Crear las paredes. (x_pos, y_pos, largo, alto)
         
        # Esta es la lista de las paredes. Cada una se especifica de la forma [x, y, largo, alto]
        paredes = [ [0,0,1151,30,ROJO],
                  [1121,0,30,225,ROJO],
                  [1121,325,30,250,ROJO],
                  [0,0,30,225,ROJO],
                  [0,325,30,212,ROJO],
                  [390,200,30,100,GRIS],
                  [170,200,30,100,GRIS],
                  [280,200,30,100,GRIS],
                  [500,200,30,100,GRIS],
                  [610,200,30,100,GRIS],
                  [720,200,30,100,GRIS],
                  [830,200,30,100,GRIS],
                  [940,200,30,100,GRIS],
                  [150,395,900,20,AZUL],
                  [150,100,900,20,AZUL],
                  [0,507,1151,30,ROJO],  
                ]
         
        # Iteramos a través de la lista. Creamos la pared y la añadimos a la lista.
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
         
class Cuarto2(Cuarto):
    """Esto crea todas las paredes del cuarto 2"""
    def __init__(self):
        super().__init__()
         
        paredes = [ [0,0,1151,30,ROJO],
                  [1121,0,30,225,ROJO],
                  [1121,325,30,250,ROJO],
                  [0,507,1151,30,ROJO],
                  [0,0,30,225,ROJO],
                  [0,325,30,212,ROJO],
                  [250,150,20,250,VERDE],
                  [500,150,20,250,VERDE],
                  [750,150,20,250,VERDE]  
                ]
         
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
               
  

class Cuarto3(Cuarto):
    """Esto crea todas las paredes del cuarto 3"""
    def __init__(self):
        super().__init__()
     
        paredes = [ [0,0,1151,30,ROJO],
                  [1121,0,30,225,ROJO],
                  [1121,325,30,250,ROJO],
                  [0,507,1151,30,ROJO],
                  [0,0,30,225,ROJO],
                  [0,325,30,212,ROJO],
                ]
         
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
         
        '''for x in range(250,1200, 250):
            for y in range(150, 750, 250):
                pared = Pared(x, y, 20, 150,VIOLETA)
                self.pared_lista.add(pared)'''
         
        for x in range(250,1000, 150):
            pared = Pared(x, 200, 20, 150,NEGRO)
            self.pared_lista.add(pared)
 
def main():
    """ Programa Principal """
     
    # Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
    pygame.init()

    #Usamos una biblioteca de pygame para poner la musica
    pygame.mixer.init()
    pygame.mixer.music.load("sonidos/leveltheme.wav")
    pygame.mixer.music.play(3)
      
    # Creamos una pantalla de 800x600
    pantalla = pygame.display.set_mode([1151, 537])
      
    # Creamos el título de la ventana
    pygame.display.set_caption('BOMBERMAN')
      
    # Creamos al objeto pala protagonista
    protagonista = Protagonista((50, 50))
    desplazarsprites = pygame.sprite.Group()
    desplazarsprites.add(protagonista)
      
    cuartos = []
     
    cuarto = Cuarto1()
    cuartos.append(cuarto)
     
    cuarto = Cuarto2()
    cuartos.append(cuarto)
     
    cuarto = Cuarto3()
    cuartos.append(cuarto)
     
    cuarto_actual_no = 0
    cuarto_actual = cuartos[cuarto_actual_no]
     
    reloj = pygame.time.Clock()
      
    puntuacion = 0
     
    hecho = False
      
    while not hecho:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("SALISTEs")
                #game_over = True
                hecho = True
                sys.exit()
                #pygame.quit()

        protagonista.teclado(event)         

                     
        # --- Lógica del Juego ---
         
        protagonista.mover(cuarto_actual.pared_lista)
         
        if protagonista.rect.x < -15:
            if cuarto_actual_no == 0:
                cuarto_actual_no = 2
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 1141
            elif cuarto_actual_no == 2:
                cuarto_actual_no = 1
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 1141
            else:
                cuarto_actual_no = 0
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 1141
                 
        if protagonista.rect.x > 1152:
            if cuarto_actual_no == 0:
                cuarto_actual_no = 1
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 0
            elif cuarto_actual_no == 1:
                cuarto_actual_no = 2
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 0
            else:
                cuarto_actual_no = 0
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 0
     
        # --- Dibujamos ---
##        pantalla.fill(NEGRO)
        imagen_defondo = pygame.image.load("Factory.png").convert()

        pantalla.blit(imagen_defondo, [0, 0])
         
        desplazarsprites.draw(pantalla)
        cuarto_actual.pared_lista.draw(pantalla)
         
        pygame.display.flip()
      
        reloj.tick(300)                  
    pygame.quit()
 
#main()
    
