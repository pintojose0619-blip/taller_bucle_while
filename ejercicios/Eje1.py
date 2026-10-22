"""
Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».

"""
a = int(input("Ingrese valor A "))
b = int(input("Ingrese valor B "))

while True:
    interiores = a
    if a == b or a+1 == b: 
        print("No hay enteros interiores ")
        break

    elif a < b: 
        for i in range(a+1, b):
        
            interiores += 1
            print (interiores)
        break
    else:
        print("ingrese un numero menor en a y uno mayor en b ")
        break