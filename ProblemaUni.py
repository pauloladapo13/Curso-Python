char= input('introduce una cadena: ')
v='True'
def isANumber():

	global char
	global v
	alfabet= ['q','w','e','r','t','y','u','i','o','p','a','s','d','f',	'g','h','j','k','l','z','x','c','v','b','n','m']
	for x in alfabet:
		for y in char:
			if (y != '1' and x  in char) :
				v='False'
			elif (y != '2' and x  in char) :
				v='False'
			elif (y != '3' and x  in char) :
				v='False'
			elif (y != '4' and x  in char) :
				v='False'
			elif (y != '5' and x  in char) :
				v='False'
			elif (y != '6' and x  in char) :
				v='False'
			elif (y != '7' and x  in char) :
				v='False'
			elif (y != '8' and x  in char) :
				v='False'
			elif (y != '9' and x  in char) :
				v='False'
			elif (y != '0' and x  in char) :
				v='False'
		
		
			else:
				v=v
	print(v)
	
isANumber()