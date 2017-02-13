import pygame
import personaje

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
GRIS = (125, 125, 125)
ROJO = (255, 0, 0)
VIOLETA = (255, 0, 255)

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
        paredes = [ [0,0,1151,30,GRIS],
                  [1121,0,30,497,GRIS],
                  [0,457,1151,30,GRIS],
                  [0,0,30,497,GRIS],
                  [20,0,760,20,GRIS],
                  [20,580,760,20,GRIS],
                  [390,150,30,150,ROJO],
                  [170,150,30,150,ROJO],
                  [280,150,30,150,ROJO],
                  [500,150,30,150,ROJO],
                  [610,150,30,150,ROJO],
                  [720,150,30,150,ROJO],
                  [830,150,30,150,ROJO],
                  [940,150,30,150,ROJO],
                  [1050,150,30,150,ROJO],
                  [150,380,900,20,AZUL],
                  [150,40,900,20,AZUL]
                ]
         
        # Iteramos a través de la lista. Creamos la pared y la añadimos a la lista.
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
        
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("sonidos/leveltheme.wav")
pygame.mixer.music.play(3)

screen = pygame.display.set_mode((1151, 537))
pygame.display.set_caption("BOMBERMAN")
clock = pygame.time.Clock()
jugador = personaje.Persona((50, 70))

desplazarsprites = pygame.sprite.Group()

cuartos=[]
cuarto=Cuarto1()
cuartos.append(cuarto)
cuarto_actual_no=0
cuarto_actual=cuartos[cuarto_actual_no]
 
game_over = False
 
while game_over == False:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    jugador.teclado(event)
    imagen_defondo = pygame.image.load("Factory.png").convert()
    
    screen.blit(imagen_defondo, [0, 0])
    screen.blit(jugador.image, jugador.rect)

    desplazarsprites.draw(screen)
    cuarto_actual.pared_lista.draw(screen)
   
 
    pygame.display.flip()              
    clock.tick(10)
 
pygame.quit ()
