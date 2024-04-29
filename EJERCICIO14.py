'''
Dado el vector V de tamaño N (par), llenar con elementos enteros positivos. Dividir 
imaginariamente el vector en dos partes iguales y ordenar ascendentemente los
elementos de la primera parte aplicando el Método Burbuja y ordenar 
descendentemente los elementos de la segunda parte aplicando Inserción Directa
'''
def ordenar_burbuja(V,n):
    for i in range(n):
        for j in range(0, n-i-1):
            if V[j] > V[j+1]:
                V[j], V[j+1] = V[j+1], V[j]
    return V

def ordenar_insercion(V,n):
    for i in range(1, n):
        key = V[i]
        j = i - 1
        while j >= 0 and key > V[j]:
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
print(f"Ingrese {n} elementos")
llenarVector(V,n)
print("Entrada:")
mostrarVector(V,n)
print("Salida:")
A=V[0:int(n/2)]
A=ordenar_burbuja(A,len(A))
B=V[int(n/2):n]
B=ordenar_insercion(B,len(B))
mostrarVector(A+B,n)