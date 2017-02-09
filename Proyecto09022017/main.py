import pygame
import personaje
          
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("sonidos/leveltheme.wav")
pygame.mixer.music.play(3)

screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("BOMBERMAN")
clock = pygame.time.Clock()
jugador = personaje.Persona((50, 70))
 
game_over = False
 
while game_over == False:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    jugador.teclado(event)
    imagen_defondo = pygame.image.load("fondo1.png").convert()
    
    screen.blit(imagen_defondo, [0, 0])
    screen.blit(jugador.image, jugador.rect)
   
 
    pygame.display.flip()              
    clock.tick(10)
 
pygame.quit ()
