"""
Caso. Una actividad recibe números uno a uno hasta que aparezca -50. Muestre la suma de todas las
lecturas anteriores; -50 no forma parte de los datos y nunca se suma. Los demás valores, incluidos
negativos distintos de -50 y el cero, sí participan. Si el primer dato es -50, la suma es cero. El flujo siempre
contiene el centinela.

"""



freno = -50
suma = 0

while True:
    
    numero = int(input("ingrese los numeros"))
    if numero != freno:
        suma += numero
    else:
        print("suma ",suma) 
        break   


