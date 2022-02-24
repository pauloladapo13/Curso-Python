from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre= StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg='blue', justify='center')

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(fg='blue', justify='center', show='$')


cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg='blue', justify='center')

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion.config(fg='blue', justify='center')

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky='nsew')

textoComentario.config(yscrollcommand=scrollVert.set )

nombreLabel= Label(miFrame, text='Nombre: ')
nombreLabel.grid(row=0, column=0, sticky='w', padx=10, pady=10)


apellidoLabel= Label(miFrame, text='Apellido: ')
apellidoLabel.grid(row=2, column=0, sticky='w', padx=10, pady=10)


direccionLabel= Label(miFrame, text='Dirreccion: ')
direccionLabel.grid(row=3, column=0, sticky='w', padx=10, pady=10)

PassLabel= Label(miFrame, text='Password: ')
PassLabel.grid(row=1, column=0, sticky='w', padx=10, pady=10)


ComentariosLabel= Label(miFrame, text='Comentario: ')
ComentariosLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

def codigoboton():
    minombre.set("Juan") 


botonEnvio= Button(raiz, text="Enviar", command= codigoboton)

botonEnvio.pack()


raiz.mainloop()