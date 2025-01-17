try: 
    #intentar dividir dos numeros
    numero1 = 10
    numero2 = 0
    division = numero1 / numero2
    print("el resultado de la division es", division)
except ZeroDivisionError:
    #si ocurre un error de division mostramos este mensaje
    print("Error, no se puede dividir entre cero")