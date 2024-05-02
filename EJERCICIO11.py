'''
Generar la matriz M de tamaño NxN.
'''
def mostrar_matriz(M):
    for i in M:
        for j in i:
            print (j,end="\t")
        print("\n")

def generar(matriz, n):
    matriz = [  [ 0 for _ in range(n) ] for _ in range(n) ]
    return matriz

def generarMatriz(M,n):
    num=1
    n2=n
    cc=n-1
    for k in range(int(n/2)):
        c=k
        for i in range(n2):
            M[i][c]=num
            num+=1
            c+=1
        for j in range(n2-2,-1,-1):
            M[j][cc]=num
            num+=1
        n2-=2
        cc-=1
    return M

n = int(input("Ingrese n: "))
matriz=[]
matriz=generar(matriz,n)
matriz=generarMatriz(matriz,n)
mostrar_matriz(matriz)