import sys, pygame
from pygame.locals import *
"""
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=640, height=360)
canvas.pack()

imagen=PhotoImage(file="Bomb_Factory.png")
my_image=PhotoImage(file="p_1_down.png")
bloque=PhotoImage(file="2.png")


canvas.create_image(0,0,anchor=NW,image=imagen)
canvas.create_image(60,85,anchor=NW,image=my_image)
x=100
for i in range(5):
    canvas.create_image(x,50,anchor=NW,image=bloque)
    x=x+100
x=90
for i in range(12):
    canvas.create_image(x,150,anchor=NW,image=bloque)
    x=x+40
x=100
for i in range(5):
    canvas.create_image(x,250,anchor=NW,image=bloque)
    x=x+100

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(2, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(2, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(2, -3, 0)
    else:
        canvas.move(2, 3, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()
"""
 
# Constantes
WIDTH = 480
HEIGHT = 480
MposX =0
MposY =0 
 
cont=5
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}


#=================IMAGEN====================================
 
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error as message:
                raise SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


def load_sound(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        sonido = pygame.mixer.Sound(ruta)
    except (pygame.error) as message:
        print("No se pudo cargar el sonido:" + ruta)
        sonido = None
    return sonido
 
#======================TECLADO===================================

def teclado():
    teclado = pygame.key.get_pressed()
    global MposX
    global cont, direc
   
    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1
        direc=True
    if teclado[K_LEFT]:
        MposX-=2
        cont+=1
        direc=False

    if teclado[K_UP]:
        Mposy-=2
        cont+=1
        direc=True
    if teclado[K_DOWN]:
        MposY+=2
        cont+=1
        direc=False
        
    elif teclado[K_q]:
        #SALTO
        MposX-=2
    #else :
         #cont=6
       
    return
   
 
#===================SPRITE===============================
#========================================================
def sprite():
 
    global cont
 
    xixf[0]=(0,0,20,37)
    xixf[1]=(22,0,26,37)
    xixf[2]=(47,0,25,37)
    xixf[3]=(73,0,20,37)
    xixf[4]=(95,0,26,37)
    #xixf[5]=(120,0,27,37)

    #Rxixf[0]=(122,0,22,41)
    Rxixf[0]=(96,0,25,37)
    Rxixf[1]=(74,0,22,37)
    Rxixf[2]=(50,0,23,37)
    Rxixf[3]=(24,0,26,37)
    Rxixf[4]=(0,0,25,37)
   
    p=5
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if cont==p*5:
        i=4
        cont=0

   
    #if cont==p*6:
       #i=5
       #cont=0
   
    return
 
def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonidos/leveltheme.wav")
    pygame.mixer.music.play(3)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BOMBERMAN")
   
    fondo = imagen("imagenes/fondo1.png")
         
    bomberman = imagen("imagenes/SP1.png",True)  
    bomberman_inv=pygame.transform.flip(bomberman,True,False);
     
    clock = pygame.time.Clock()
   
 
    # el bucle principal del juego
    while True:
       
        time = clock.tick(60)
       
        sprite()
        teclado()
   
        fondo = pygame.transform.scale(fondo, (480, 480))
             
        screen.blit(fondo, (0, 0))
       
        if direc==True:
            screen.blit(bomberman, ( MposX, 318),(xixf[i]))
   
        if direc==False:
            screen.blit(bomberman_inv,( MposX, 318),(Rxixf[i]))
   
        pygame.display.flip()
       
       
       
       
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0

if __name__ == '__main__':
    main()

