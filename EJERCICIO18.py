'''
Dado el vector V de tamaño N, con elementos enteros positivos. Ordenar 
ascendentemente sus elementos aplicando el Método de Inserción Directa.
'''
def ordenar_insercion_ascendente(V,n):
    for i in range(1, n):
        key = V[i]
        j = i - 1
        while j >= 0 and key < V[j]:
            V[j + 1] = V[j]
            j -= 1
        V[j + 1] = key
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
V=ordenar_insercion_ascendente(V,n)
mostrarVector(V,n)