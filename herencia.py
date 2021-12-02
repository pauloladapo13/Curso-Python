class Vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca ', self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return 'La furgoneta está cargado'
        else:
            return 'La furgoneta no está cargada'


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'

    def estado(self):
        print('Marca ', self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, '\n', self.hcaballito)


class Velectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):

        self.cargando = True


miMoto = Moto('Honda', 'CBR')
miMoto.caballito()
miMoto.estado()
miFurgoneta = furgoneta('Seat', 'Kangoo')
miFurgoneta.estado()
print(miFurgoneta.carga(True))


class BicicletaElectica(Velectricos, Vehiculos):

    pass


miBici = BicicletaElectica('Audi', 'RK8') 

print(isinstance(miFurgoneta, Velectricos))
print(isinstance(miBici, Velectricos))
