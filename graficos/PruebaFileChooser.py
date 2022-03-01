from tkinter import *
from tkinter import filedialog


root= Tk()

def abreFichero():
    fichero= filedialog.askopenfilename(title="Abrir", initialdir="Users", filetypes=(("Ficheros zip", "*zip"),("Ficheros de texto", "*.txt"), ("Todos los Ficheros", "*.*")))

    print(fichero)

Button(root, text="Abrir fichero", command= abreFichero).pack()









root.mainloop()