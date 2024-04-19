#LLENAR UN VECTOR D CON N NUMEROS, HALLAR EL NUMERO MAYOR
#Y COLOCARLO AL INICIO DEL VECTOR
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
    
def colocar(v,n):
    may=mayor(v,n)
    for i in range (n):
        if v[i]==may:
            a=v[0]
            v[0]=may
            v[i]=a
    print(v)

"""MAIN"""
n=int(input("Ingrese el valor de N: "))
v=[0]*n
llenarVector(v,n)
colocar(v,n)


    
