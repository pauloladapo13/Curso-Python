class Empleado:
    
    def __init__(self, nombre, cargo, salario):

        self.nombre= nombre

        self.cargo= cargo

        self.salario= salario

    def __str__(self):

        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[

Empleado("Juan", "Director", 75000), 
Empleado("Ana", "Presidenta", 110000),
Empleado("Maria", "Botones", 10000),
Empleado("Pedro", "limpiadora", 1000),
Empleado("Alvaro", "teleoperadora", 12000),

]

def calculo_comision(empleado):
    if empleado.salario<20000:
        empleado.salaio=empleado.salario*1.03

    return empleado

l=map(calculo_comision, listaEmpleados)

for empleado in l:

    print(empleado)
