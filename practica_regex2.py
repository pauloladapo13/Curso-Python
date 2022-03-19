import re
import os 
import time




nombre1= "Sandra Lopez"

nombre2= "Sandra Lopez"

nombre3= "Maria Lopez"

nombre4= "sandra Lopez"

nombre5= "Jara Lopez"

nombre6= "Lara Lopez"

cadena1= "Jara Lopez"

cadena2="4793205-2937"

cadena3= "a4540804354"

codigo1="dsjlkedjodjsxzlfkzhj71fdhsfikvjlkdjfs;jgds;lskja"

codigo2="addkaldflajdljflkjdflkjslkajklladf"

codigo3="dkkald akdldl dklasdfdlfjl dskljflkaf sldk"


if re.search("71", codigo1):
    print("Hemos encontrado el nombre")

else: 

    print("No lo hemos encontrado")

if re.match(".ara", nombre5, re.IGNORECASE):
    
    print("Hemos encontrado el nombre")

else: 

    print("No lo hemos encontrado")



if re.match("\d", cadena2):

    
    print("Hemos encontrado el numero")

else: 

    print("No lo hemos encontrado")







def clear():
    time.sleep(5)
    if __name__ == '__main__':

        clear=lambda: os.system('clear')
        clear()


clear()