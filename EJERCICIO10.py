'''sumar filas de la matriz'''

def mostrarMatriz(M):
    for i in M:
        print (i)

def llenarMatriz(M,n):
    for i in range (n):
        for j in range (n):
            M[i][j]=int(input())
    return M
def sumaFila (M,n):
    for i in range(n):
        s=0
        for j in range (n):
            s=s+M[i][j]
        print(s)
        
#MAIN
n=int(input("Ingrese N: "))
M=[[0]*n for _ in range (n)]
M=llenarMatriz(M,n)
mostrarMatriz(M)
print("Suma ")
sumaFila(M,n)
