'''
Dado el vector V de tamaño N, con elementos enteros positivos. Ordenar 
descendentemente sus elementos aplicando el Método Shell
'''
def shell_sort_descendente(V,n):
    espacio = n // 2
    while espacio > 0:
        for i in range(espacio, n):
            temp = V[i]
            j = i
            while j >= espacio and V[j - espacio] < temp:
                V[j] = V[j - espacio]
                j -= espacio
            V[j] = temp
        espacio //= 2
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
V=shell_sort_descendente(V,n)
mostrarVector(V,n)