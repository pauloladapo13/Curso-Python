class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    # La clase tiene 4 propiedades
    def arrancar(self):
        self.enMarcha = True
        
    def estado(self):
        if(self.enMarcha):
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'
# La clase tiene 2 comportamientos

miCoche = Coche() #instanciar o ejemplerizar una clase

print('El largo del cohe es:',miCoche.largoChasis)
print('El coche tiene ', miCoche.ruedas, 'ruedas')
miCoche.arrancar()
print(miCoche.estado())