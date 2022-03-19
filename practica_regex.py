import re
import os
import time
from turtle import clearscreen

# cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje sencillo de aprender"

# textoBuscar="Python"

# textoEncontrado=re.search(textoBuscar, cadena)

# print(textoEncontrado.start())

# print(textoEncontrado.end())

# print(textoEncontrado.span())

# print(re.findall(textoBuscar, cadena))

# print(len(re.findall(textoBuscar, cadena)))

# lista_nombres=['Ana Gomez', 
#  'Maria Martin', 
#  'Sandra Lopez', 
#  'Santiago Marten',
#  'Sandra Fernandez']


# for elemento in lista_nombres:
#     if re.findall('Martin$', elemento):
#         print(elemento)

# for elemento in lista_nombres:
#     if re.findall('[z]', elemento):

#         print(elemento)

lista_nombres=['Ana', 'Pedro', 'Maria', 'Rosa', 'Sandra', 'Celia', 'Cecilia', 'Ceci', 'Roxana', 'Rosalia', 'Roman']

for elemento in lista_nombres:
       if re.findall('Mart[ie]n', elemento):
        print(elemento)


for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):

        print(elemento)

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

for elemento in lista_nombres:
    if re.findall('Ro[^o-t]', elemento):

        print(elemento)

def clearr():
    time.sleep(7)
    if __name__=='__main__':
        clear = lambda: os.system('clear')
        print('done')
        clear()

clearr()

