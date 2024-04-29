'''
 Dado el vector V de tamaño N, con elementos enteros positivos. Ordenar 
descendentemente sus elementos aplicando el Método QuickSort.
'''
def quicksort_descendente(V):
    if len(V) <= 1:
        return V
    pivot = V[len(V) // 2]
    menores = [x for x in V if x < pivot]
    iguales = [x for x in V if x == pivot]
    mayores = [x for x in V if x > pivot]
    return quicksort_descendente(mayores) + iguales + quicksort_descendente(menores)


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
V=quicksort_descendente(V)
mostrarVector(V,n)