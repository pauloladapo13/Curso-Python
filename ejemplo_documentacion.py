class Areas:
    def areaCuadrado(lado):

        ''' Calcula el area de un cuadrado elevando al cuadrado 
         el lado pasado por parametro '''
    
    
        return "El area del cuadrado es: " + str(lado*lado)


    def areaTriangulo(base, altura):

        return "El area del trianfulo es:" + str((base*altura)/2)


print(Areas.areaCuadrado.__doc__)

help(Areas.areaTriangulo)
help(Areas)