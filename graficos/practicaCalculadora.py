from tkinter import *

raiz = Tk()

miFrame= Frame(raiz)
miFrame.pack()

pantalla= Entry(miFrame) 

# ----------------------------pantalla-------------------------------------

pantalla.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------------fila 1 -----------------------------------

boton7=Button(miFrame, text="7") 
boton7.grid(row=2, column=0)
boton8=Button(miFrame, text="8")
boton8.grid(row=2, column=1)
boton9=Button(miFrame, text="9")
boton9.grid(row=2, column=2)
botonMult=Button(miFrame, text="x")
botonMult.grid(row=2, column=3)

# --------------------fila2--------------------------------------

boton4= Button(miFrame, text="4")
boton4.grid(row=3, column=0)
boton5= Button(miFrame, text="5")
boton5.grid(row=3, column=1)
boton6= Button(miFrame, text="6")
boton6.grid(row=3, column=2)
botondiv= Button(miFrame, text="/")
botondiv.grid(row=3, column=3)

# ------------------fila3---------------------------------------------

boton1= Button(miFrame, text="1")
boton1.grid(row=4, column=0)
boton2=Button(miFrame, text="2")
boton2.grid(row=4, column=1)
boton3=Button(miFrame, text="3")
boton3.grid(row=4, column=2)
botonmin= Button(miFrame, text="-")
botonmin.grid(row=4, column=3)


# ------------------fila4-----------------------------------------------

boton0= Button(miFrame, text="0")
boton0.grid(row=5, column=0)
botoncoma= Button(miFrame, text= ",")
botoncoma.grid(row=5, column=1)
botonequal= Button(miFrame, text="=")
botonequal.grid(row=5, column=2)
botonsum= Button(miFrame, text="+")
botonsum.grid(row=5, column=3)

raiz.mainloop()