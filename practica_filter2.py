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
Empleado("Alvaro", "teleoperadora", 12000)

]

salarios_altos=filter(lambda empleado:empleado.salario>10000, listaEmpleados)
ls= []
for empleadosS in salarios_altos:
    print(empleadosS)
