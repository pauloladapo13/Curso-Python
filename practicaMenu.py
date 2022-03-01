from cProfile import label
from tkinter import *


root= Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu= Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="New File")
archivoMenu.add_command(label="New Folder")
archivoMenu.add_separator()
archivoMenu.add_command(label="Save")
archivoMenu.add_command(label="Save as..")
archivoMenu.add_separator()
archivoMenu.add_command(label="Close")
archivoMenu.add_command(label="Exit")



archivoEdicion= Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copy")
archivoEdicion.add_command(label="Cut")
archivoEdicion.add_command(label="Paste")
archivoHerramientas= Menu(barraMenu)

archivoAyuda= Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia") 
archivoAyuda.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edit", menu=archivoEdicion)
barraMenu.add_cascade(label="Tools", menu=archivoHerramientas)
barraMenu.add_cascade(label="Help", menu=archivoAyuda)

root.mainloop()