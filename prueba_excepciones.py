def suma(num1, num2):
    
    return num1+num2

def resta(num1, num2):
    
    return num1-num2

def multiplica(num1, num2):
    
    return num1*num2

def divide(num1, num2):
    
    try:
        return num1/ num2
    except ZeroDivisionError:
        print('no se puede dividir entre 0')
        return 'Operación errónea'

while True:
    try:
        op1 = int(input('Introcuce el 1ª número a calcular: '))
        op2 = int(input('Introcuce el 2ª número a calcular: '))
        break
    except ValueError:
        print('Los valores introducidos no son correctos. Intentelo de nuevo')
    
cal = input('introduce tipo de cálculo a realizar:(suma, resta, multiplica, divide): ')

if cal == 'suma':
    print(suma(op1, op2))
    
elif cal== 'resta':
    print(resta(op1, op2))
    
elif cal == 'multiplica':
    print(multiplica(op1, op2))
    
elif cal == 'divide':
    print(divide(op1, op2))
    
else: 
    print('operación no contemplada')
print('Operación ejecutada. Esperando a mas opciones y continuar')