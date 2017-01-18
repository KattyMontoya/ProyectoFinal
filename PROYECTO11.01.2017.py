from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=730, height=700)
canvas.pack()

imagen=PhotoImage(file="esenario.png")
my_image=PhotoImage(file="p_1_down.png")


canvas.create_image(0,0,anchor=NW,image=imagen)
canvas.create_image(60,85,anchor=NW,image=my_image)

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

