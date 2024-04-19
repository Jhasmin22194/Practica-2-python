'''Llenar dos vectores A y B con N números enteros positivos. Hallar el número primo mayor
de cada vector y mostrar sus factoriales. En el caso de que alguno de los vectores o los
dos no tengan números primos mostrar el mensaje “Hasta luego!!!”'''
def llenarVector(v,n):
    print(f"Ingrese {n+1} valores")
    for i in range (n):
        v[i]=int(input(""))
    print(v)

def mayor(v,n):
    may=v[0]
    for i in range(1,n):
        if v[i]>may:
            may=v[i]
    return may
    
def hallarp(v,n):
    
    for i in range (n):
        for 
    print(v)
    may=mayor(v,n)

"""MAIN"""
n=int(input("Ingrese el valor de N: "))
va=[0]*n
vb=[0]*n
llenarVector(va,n)
llenarVector(vb,n)

