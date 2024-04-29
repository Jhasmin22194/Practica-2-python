'''
 Dado el vector V de tamaño N, llenar con elementos enteros positivos. Ordenar sus 
elementos de las posiciones impares descendentemente
'''



def ordenBurbuja(V,n):
    for _ in range (1,n):
        for j in range (1,n-2,2):
            if V[j]>V[j+2]:
                aux=V[j]
                V[j]=V[j+2]
                V[j+2]=aux
    mostrarVector(V,n)

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
ordenBurbuja(V,n)