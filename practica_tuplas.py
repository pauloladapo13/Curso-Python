mitupla=('Juan', 13, 1, 1995, 13)
#Una tupla tiene la misma función que una lista solo que con excepciones
#Por ejemplo no se podrá acceder a cualquier función que modifique la misma
milista = list(mitupla)
#UNa tupla puede ser convertido a lista con la función "list()" y viceversa con la función "tuple()""
print(mitupla[1])
print(milista)
mitupla = tuple(milista)
print(mitupla)
print('Juan' in mitupla) # la función "in" si se puede utilizar en ambos casos como otros de parecidos casos
print(mitupla.count(13))
#La función "count()", permite determinar el numero de veces que se repite un elemento, devuelve un entero
print(len(mitupla)) #La función "len()", devuelve en este caso el numero de elementos totales y NO EL INDIDE  que contiene la tupla.
mitupla = ('juan',) # También se pueden crear tuplas unitarias , que es una tupla con un único elemento.
print( len(mitupla))
mitupla=('Juan', 13, 1, 1995)
nombre, dia, mes, agno = mitupla
# El famoso desempaquetado de tupla lo qu permite es asignar un nombre a cada elemento de la tupla de una forma sencilla.
print(nombre)
print(dia)
print(agno)
print(mes)
#si queremos que se nos devuelva un boolean y comprobar si el usuario ha introducido un dígito o no solo tenemos que utilizar el método "isdigit()"
print(mes.isdigit())