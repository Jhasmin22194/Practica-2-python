'''
Dado el vector V de tamaño N, con elementos enteros positivos. Ordenar 
descendentemente sus elementos aplicando el Método Burbuja.
'''
def ordenar_burbuja(V,n):
    for i in range(n):
        for j in range(0, n-i-1):
            if V[j] < V[j+1]:
                V[j], V[j+1] = V[j+1], V[j]
    return V


def llenarVector (V,n):
    for i in range (n):
        V[i]=int(input())
        
def mostrarVector (V,n):
    for i in range (n):
        print("[",V[i],"]", end=" ")
    print("")
        

n=int(input("Ingrese el valor de N: "))
V=[0]*n
print(f"Ingrese {n} numeros")
llenarVector(V,n)
print("Entrada:")
mostrarVector(V,n)
print("Salida:")
V=ordenar_burbuja(V,n)
mostrarVector(V,n)