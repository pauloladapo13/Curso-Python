from cProfile import label
from email import message
from tkinter import *
from tkinter import messagebox

root= Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Paul", "Procesador Actualizado en 2022")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    # valor=messagebox.askquestion("Salir", "Do you want to exit?")

    valor=messagebox.askokcancel("Exit", "Do you want to exit?")
    if valor==True:
        root.destroy()
    
def cerrarDocumento():
        valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
        if valor==False:
            root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu= Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="New File")
archivoMenu.add_command(label="New Folder")
archivoMenu.add_separator()
archivoMenu.add_command(label="Save")
archivoMenu.add_command(label="Save as..")
archivoMenu.add_separator()
archivoMenu.add_command(label="Close", command= cerrarDocumento)
archivoMenu.add_command(label="Exit", command=salirAplicacion)



archivoEdicion= Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copy")
archivoEdicion.add_command(label="Cut")
archivoEdicion.add_command(label="Paste")
archivoHerramientas= Menu(barraMenu)

archivoAyuda= Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia) 
archivoAyuda.add_command(label="About...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edit", menu=archivoEdicion)
barraMenu.add_cascade(label="Tools", menu=archivoHerramientas)
barraMenu.add_cascade(label="Help", menu=archivoAyuda)

root.mainloop()