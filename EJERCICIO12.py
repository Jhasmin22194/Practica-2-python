'''
Dado el vector V de tamaño N, llenar con elementos enteros positivos. Ordenar sus 
elementos pares ascendentemente. En caso de no haber elementos pares, mostrar el 
mensaje “”Hasta luego!!!”.
'''
def par(V,n):
    A=[]
    for i in range(n):
        if V[i]%2==0:
            A.append(V[i])
    return A


def ordenBurbuja(V,n):
    for _ in range (1,n):
        for j in range (n-1):
            if V[j]>V[j+1]:
                aux=V[j]
                V[j]=V[j+1]
                V[j+1]=aux
    return V

def ordenPares (V,n):
    A=par(V,n)
    A=ordenBurbuja(A,len(A))
    c=0
    sw=0
    for i in range (n):
        if V[i]%2==0:
            sw=1
            V[i]=A[c]
            c+=1
    if sw==0:
        print("Hasta luego!!!")
    else:
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
ordenPares(V,n)