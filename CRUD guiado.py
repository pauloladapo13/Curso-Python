from select import KQ_FILTER_WRITE
from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()

barraMenu= Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")


crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Read")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")


ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="AYUDA", menu=ayudaMenu)

# --------------------------comienzo de campos-----------------------------------

miFrame=Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(fg="red", justify="right")

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=2, column=1, padx=10, pady=10)
cuadroNombre.config(show="£", )

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)







root.mainloop()