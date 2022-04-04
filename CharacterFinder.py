s= input("Introduce una palabra: ") 
p= input("Introduce una cadena a buscar: ")

def cad(palabra, cadena):
    count=0
    s= palabra
    t= len(palabra)
    ca= len(cadena) 

    for i in range(0,t, ca ):
        cad=i+ca
        c= s[i:cad+1]
        print(c)
        if cadena in c:
            count +=1
    print(count)

cad(s, p)# ui es un ejemplo que use con tequierotequierotequiero, puedes poner la cantidad de cad3nas que quieras a buscar.