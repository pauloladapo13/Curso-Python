import time     

nombre=input('Introduce nombre, por favor:')

def lista_de_nombres(nombre):

    miLista=["María", "Pepe", "Marta", "María",]

    miLista.append(nombre)
    return miLista



MiLista= str(lista_de_nombres(nombre))

print('De momento tu lista es: ' + MiLista)
print()

print(MiLista[:13])
print()
time.sleep(2)

print(MiLista[:23])
print()
time.sleep(2)

print(MiLista[24:])
print()
time.sleep(2)

print(MiLista[30:])  
print()  
time.sleep(2)


#Se partirá el objeto por letra o singo ya que proviene la variable de una función.

