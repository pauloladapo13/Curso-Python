import pickle
import time
import os
def clearr():
    time.sleep(7)
    if __name__=='__main__':
        clear = lambda: os.system('clear')
        print('done')
        clear()

# lista_nombres = ['Pedro','Ana','Maria, Isabel']

# fichero_binario = open('lista_nombres', 'wb')

# pickle.dump(lista_nombres, fichero_binario)

# fichero_binario.close()
# del(fichero_binario)

fichero= open('lista_nombres', 'rb')
# rd significa read binary info
lista= pickle.load(fichero)
print(lista)







clearr()

