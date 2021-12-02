mi_diccionario = {'Alemania':'Berlín', 'Francia':'París', 'Reino Unido': 'Londres', 'España':'Madrid'}
#Un diccionario almacena una clave y una valor.
#Puede ser un dato de cualquier tipo en ambos casos
print(mi_diccionario['Francia'])
#Puedes accecer a un valor del diccionario con la clave 
# para acceder a todo el diccionario
mi_diccionario['Italia'] = 'Lisboa' # Para añadir elementos
print(mi_diccionario)

#Para modificar un elemento de un diccionario
mi_diccionario['Italia'] = 'Roma'
print(mi_diccionario)
#para eliminar una elemento de un diccionario se utiliza el metodo "del"
del mi_diccionario['Reino Unido']
print(mi_diccionario)
mi_tupla = ('España', 'Francia', 'Reino Unido', 'Alemania')
mi_diccionario ={mi_tupla[0]:'Madrid', mi_tupla[1]:'París', mi_tupla[2]:'Londres', mi_tupla[3]:'Madrid'}
# Para asignar un valor desde una clave almacenado en una tupla.
print(mi_diccionario['Francia'])
mi_diccionario = {23:'jordan', 'Nombre': 'Michael', 'Equipo':'Chicago', 'anillo':[1991,1992,1993,1996,1997,1998]}
print(mi_diccionario)
print(mi_diccionario['anillo'])
mi_diccionario = {23:'jordan', 'Nombre': 'Michael', 'Equipo':'Chicago', 'anillo':{'temporadas':[1991,1992,1993,1996,1997,1998]}}
print(mi_diccionario)
print(mi_diccionario.keys()) # La función "key()" te devuelve todas las claves de tu diccionario o la que quieras elegir.
print(mi_diccionario.values()) # La función "values()" devuelve los valores del diccionario.
print(len(mi_diccionario)) # Devuelve la cantidad de elementos en el diccionario.
