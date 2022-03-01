from tkinter import *

raiz = Tk()

miFrame= Frame(raiz)
miFrame.pack()

op=""       
res=0
# ----------------------------pantalla-------------------------------------

numeroP=StringVar()

pantalla= Entry(miFrame, textvariable=numeroP) 
pantalla.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# ----------------------------pulsaciones teclado------------------------

def numeroPulsado(num): 
    global op 
     
    if op!="":

        numeroP.set(num)

        op=""
    else: 
    
        numeroP.set(numeroP.get() + num)


# --------------------------funcion suma---------------------
    
def suma(num):
    global op

    global res

    res+=int(num)

    op= "suma"

    numeroP.set(res)

#-------------------------- funcion resta---------------------------
def resta(num):
    global op
    global res

    res= int(num)-res

    op= "resta"

    numeroP.set(res)
# ----------------------------------funcion el_resultado---------------------

def el_res():

    global res

    numeroP.set(res+int(numeroP.get()))

    res=0

#--------------------fila 1 -----------------------------------

boton7=Button(miFrame, text="7", command=lambda:numeroPulsado( "7")) 
boton7.grid(row=2, column=0)
boton8=Button(miFrame, text="8", command=lambda:numeroPulsado( "8"))
boton8.grid(row=2, column=1)
boton9=Button(miFrame, text="9", command=lambda:numeroPulsado( "9"))
boton9.grid(row=2, column=2)
botonMult=Button(miFrame, text="x")
botonMult.grid(row=2, column=3)

# --------------------fila2--------------------------------------

boton4= Button(miFrame, text="4", command=lambda:numeroPulsado( "4"))
boton4.grid(row=3, column=0)
boton5= Button(miFrame, text="5", command=lambda:numeroPulsado( "5"))
boton5.grid(row=3, column=1) 
boton6= Button(miFrame, text="6", command=lambda:numeroPulsado( "6"))
boton6.grid(row=3, column=2)
botondiv= Button(miFrame, text="/")
botondiv.grid(row=3, column=3)

# ------------------fila3---------------------------------------------

boton1= Button(miFrame, text="1", command=lambda:numeroPulsado( "1"))
boton1.grid(row=4, column=0)
boton2=Button(miFrame, text="2", command=lambda:numeroPulsado( "2"))
boton2.grid(row=4, column=1)
boton3=Button(miFrame, text="3", command=lambda:numeroPulsado( "3"))
boton3.grid(row=4, column=2)
botonmin= Button(miFrame, text="-", command=lambda:resta(numeroP.get()))
botonmin.grid(row=4, column=3)


# ------------------fila4-----------------------------------------------

boton0= Button(miFrame, text="0", command=lambda:numeroPulsado( "0"))
boton0.grid(row=5, column=0)
botoncoma= Button(miFrame, text= ",", command=lambda:numeroPulsado( ","))
botoncoma.grid(row=5, column=1)
botonequal= Button(miFrame, text="=", command= lambda:el_res()) 
botonequal.grid(row=5, column=2)
botonsum= Button(miFrame, text="+", command= lambda:suma(numeroP.get()))
botonsum.grid(row=5, column=3)

raiz.mainloop()