from tkinter import *
raiz = Tk()

raiz.title('Ventana de pruebas')

raiz.resizable(1,1)

raiz.iconbitmap('Icono1.ico')
# raiz.geometry('650x350')

raiz.config(bg='blue')

miFrame= Frame()

miFrame.pack(fill='both')

miFrame.config(bg='red')
miFrame.config(width=640, height='350')
miFrame.config(bd='35')
miFrame.config(relief='sunken')
miFrame.config(cursor='pirate')
raiz.mainloop()

