from tkinter import *

root=Tk()

root.title("Ejemplo")

playa= IntVar()
monte=IntVar()
turismoRural= IntVar()

def opcionesviaje():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" playa"
    
    if(monte.get()==1):
        opcionEscogida+=" monte"

    if(turismoRural.get()==1):
        opcionEscogida+=" turismoRural"

    textoFinal.config(text=opcionEscogida)


foto=PhotoImage(file="avion15.gif")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(frame, text="Monte", variable=monte, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(frame, text="Turismo rural",variable=turismoRural, onvalue=1, offvalue=0, command=opcionesviaje).pack()


textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()
