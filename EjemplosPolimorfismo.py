class Coche():

    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')


class Moto():

    def desplazamiento(self):
        print('Me deplazo utilizando dos ruedas')


class Camion():

    def desplazamiento(self):
        print('Desplazamiento utilizando seis ruedas')


def desplazamientoVehiculo(vehiculo):

    vehiculo.desplazamiento()


mivehiculo = Moto()

desplazamientoVehiculo(mivehiculo)
