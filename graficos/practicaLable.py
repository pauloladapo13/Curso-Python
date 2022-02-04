from tkinter import *

root=Tk()

miFrame= Frame(root, width=500, height=400)

miFrame.pack()

miImage=PhotoImage(file='giphy.gif')

Label(miFrame, image=miImage).place(x=100, y=200)



# miLabel= Label(miFrame, text='Hola usuarios ', fg='red', font=('Comic Sans MS',18 ))
# miLabel.place(x=100, y=200)
# Si no vamos a usar ninguna variable de tipo label podemo abreviar la sintaxis 
# de la siguiente manera: Label(miFrame, text='Hola usuarios ').place(x=100, y=200)





root.mainloop()