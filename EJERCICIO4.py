''' Llenar un vector GD de tamaño N con los gastos diarios de los estudiantes de 2do. 
Semestre de Ingeniería de Sistemas. Rotar los elementos del vector dos posiciones hacia 
la izquierda
'''
def llenarVector (V,n):
    for i in range (n):
        V[i]=int(input())
        
def mostrarVector (V,n):
    for i in range (n):
        print("[",V[i],"]", end=" ")
    print("")
        
def rotarIzq(V,n):
    a=V[2:n]
    b=V[0:2]
    return (a+b)

n=int(input("Ingrese el valor de N: "))
GD=[0]*n
print(f"Ingrese {n} gastos")
llenarVector(GD,n)
print("Entrada:")
mostrarVector(GD,n)
print("Salida:")
mostrarVector(rotarIzq(GD,n),n)