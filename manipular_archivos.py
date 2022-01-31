from io import open
import time
import os
def clearr():
    time.sleep(7)
    if __name__=='__main__':
        clear = lambda: os.system('clear')
        print('done')
        clear()

archivo_texto = open('archivo.txt', 'r+')       

# frase = 'Estupendo dia para estudiar Python\nEl Lunes'
# archivo_texto.rite(frase)
# archivo_texto.close()
# # print('close')
# texto = archivo_texto.read()

# archivo_texto.close()
# print(texto)

# lineas_texto = archivo_texto.readlines()

# archivo_texto.close()
# print(lineas_texto[1])
# archivo_texto.write('\nSiempre es una buena ocasion para estudiar Python')
# # archivo_texto.close()
# print(archivo_texto.read(11))
# # archivo_texto.seek(11)
# print(archivo_texto.read())
# archivo_texto.seek(len(archivo_texto.readline()))
# print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines();

lista_texto[1] = 'Esta linea ha sido incluida desde el exterior\n'
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()

clearr()