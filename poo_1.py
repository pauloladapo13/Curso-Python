class Coche():

    # constructor. metodo inicial que le da el estado inicial a los objetos.
    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120 
        self.__ruedas = 4
        self.__enMarcha = False
    # La clase tiene 4 propiedades

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if(self.__enMarcha):
            chequeo = self.__chequeo_intento()

        if (self.__enMarcha and chequeo):
            return 'El coche está en marcha'

        elif(self.__enMarcha and chequeo == False):
            return 'Algo ha salido mal en el chequeo, no podemos arrancar.'

        else:

            return 'El coche está parado'

    def estado(self):
        print('El coche tiene ', self.__ruedas, 'ruedas. Un ancho de ',
              self.__anchoChasis, 'y largo de ', self.__largoChasis)

    def __chequeo_intento(self):
        print('realizando chequeo interno')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):

            return True
        else:

            return False


# La clase tiene 2 comportamientos

miCoche = Coche()  # instanciar o ejemplerizar una clase


print(miCoche.arrancar(True))
miCoche.estado()

print('--------------------A continuación creamos el segundo objeto---------------------')

miCoche2 = Coche()

print(miCoche2.arrancar(False))

# miCoche2.ruedas=2 # Al encapsular tanto las propiedades como los estados con "__" en python.
# NO SE PODRÁ ACCEDER AL CAMBIO DE LA CLASE desde el exterior. Es decir, cualquiera que no tenga acceso a la clase no podrá camiar las propiedades principlaes del mismo(solo el que esta sometido a la encapsulación).

miCoche2.estado()
