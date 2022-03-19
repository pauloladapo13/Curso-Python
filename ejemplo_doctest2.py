import math

def rc(list):

    ''' 
    La funcion devuelve una lista con la 
    raiz cuadrada de los elementos numericos
    pasados por parametros en otra lista
    
    >>> lista=[]
    >>> for i  in [4, 9, 16]:
    ...     lista.append(i)

    >>> rc(lista)
    [2.0, 3.0, 4.0]



    >>> lista=[]
    >>> for i in [4, -9, 16]:
    ...     lista.append(i)
    >>> rc(list)
    Traceback(most recent call last):
        ...
    ValueError: math domain error    
    
    
     '''

    return [math.sqrt(n) for n in list]


# print(rc([9,-16,25,36]))

import doctest

doctest.testmod()