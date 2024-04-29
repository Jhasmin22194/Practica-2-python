''' Llenar un vector NT con las notas de N estudiantes.
Hallar la nota menor que divida al vector en dos partes
y hallar el promedio de cada una de las partes.
(En caso de que la nota menor se repita,
tomar la primera que se encuentre en el vector) '''
def llenarVector (V,n):
    for i in range (n):
        V[i]=int(input())
        
def mostrarVector (V,n):
    for i in range (n):
        print("[",V[i],"]", end=" ")
    print("")
        
def Pmenor (V,n):
    menor=V[0]
    pos=0
    for i in range (n):
        if V[i] < menor:
            menor = V[i]
            pos=i
    return pos

def promVector(V,n):
    return sum(V)/n
    

def dividirVector (V,n):
    pos = Pmenor(V,n)
    A=V[0:pos]
    B=V[pos+1:n]
    print("Primera parte")
    print(A)
    print("Promedio: ",promVector(A,len(A)))
    print("Segunda parte")
    print(B)
    print("Promedio: ",promVector(B,len(B)))

n=int(input("Ingrese el valor de N: "))
V=[0]*n
print(f"Ingrese {n} notas")
llenarVector(V,n)
print("notas")
mostrarVector(V,n)
dividirVector(V,n)