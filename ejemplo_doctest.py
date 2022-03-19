def cmail(mailuser):

    """
    la funcion cmail evalua un mail recibido 
    en busca de la @. Si tiene una @ es correcto, 
    si tiene mas de una @ es incorrecto si la @
    esta al final es incorrecto 
    
    
    >>> cmail('programador@enlinea.com')
    True

    >>> cmail('programadorenlinea.com@')
    False
    
    >>> cmail('programadorenlinea.com')
    False


    >>> cmail('programadorenlinea@.com')
    False


    """
    
    arr=mailuser.count('@')

    if (arr!=1 or mailuser.rfind('@')==(len(mailuser)-1) or mailuser.find('a')==0 or mailuser.rfind('@')==(len(mailuser)-5)):
        return False
    
    else:
        return True







import doctest
doctest.testmod()