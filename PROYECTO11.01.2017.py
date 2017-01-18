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


