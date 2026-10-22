"""
Caso. Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.

"""

freno = -99
suma = 0
contador = 0

while True:
    
    numero = int(input("ingrese las notas "))
    if numero != freno:
        suma += numero
        contador += 1
    elif contador == 0:
        print("Cantidad ",contador, "Sin notas ") 
        break   
    else:
        promedio = suma / contador
        print("Cantidad ",contador, "Promedio ", promedio) 
        break  
