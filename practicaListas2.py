miLista=['María', 'Pepe', 'Marta', 'Antonio']

miLista.extend(['Sandra', 'Ana', 'Lucía'])

print(miLista[:])

print(miLista[:3])

print(miLista[4:])

print(miLista[2])

print(miLista[2:3])

print(miLista[3:2])

#Recuerda
recuerda="""Todas estas ejecuciones se realizan por nombre
y no por letra como en la 1ªpráctica
ya que no es creada la lista dentro de una función 
y es creada en conjunto como una variable global
y al salir de la función y dividirlos se dividen por letra 
en cambio no es lo mismp si es una variable local.

"""
print(recuerda)

miLista.insert(2, 'Sandra')

print(miLista[:])

miLista.extend(['Fabian', 'Sergio', 'Rubio'])
print(miLista[:])

nom=str(miLista.index('Antonio'))
print('El nombre Antonio se encuentra en el índice ' + nom + ' de la lista.')

#La función index(''), te devuelve el índice del nombre o parámetro de cuya lista en el que se contiene.

miLista.remove('Ana')

#Si quiero eliminar un párametro de la lista, solo tengo que utilizar la función remove antes de usar la función print
print('Pepe' in miLista)

print(miLista[:])

miLista.pop()

print(miLista[:])

miLista2= ['Sandra','Ana']*3

miLista3= miLista+miLista2

print(miLista3[:])




# Luego está el operador (in )que devuelve un boolean(true o false), si se encuentra ese nombre o párametro en la lista o variable
#También en python se puede almacenar un número o boolean o de más en una lista.
#Y para eliminar algo de UNA lista al final como pasa con (append), que lo añade, (pop), lo elimina


