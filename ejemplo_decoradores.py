import os
import time


def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):

        # Acciones adicionales que decoran

        print("Vamos a realizar un calculo: ")

        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decdoran
        try:
            print("Hemos terminado el calculo")
            def clearr():
                time.sleep(5)
                if __name__== "__main__":
                    clear= lambda:os.system("clear")
                clear() 
            clearr()
        except:
            print('unable to perform request')

        finally:
            clearr()
        
    return funcion_interior



@funcion_decoradora
def suma(num, num2):

    print(num+ num2)

@funcion_decoradora
def resta(num, num2):

    print(num - num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(53, 32)
resta(83,32)


potencia(base=5, exponente=3)





