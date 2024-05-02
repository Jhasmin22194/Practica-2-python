'''
Generar la Matriz M de tamaño NxN con números primos en las diagonales y números
enteros en las casillas sobrantes
'''
def mostrar_matriz(M):
    for i in M:
        for j in i:
            print (j,end="\t")
        print("\n")

def generar(matriz, n):
    matriz = [  [ 0 for _ in range(n) ] for _ in range(n) ]
    return matriz

def vectorPrimo(V,n):
    V=[0]*n
    cp=0
    x=1
    while cp!=n:
        x+=1
        cm=0
        for i in range (1,x+1):
            if x%i==0:
                cm+=1
        if cm==2:
            V[cp]=x
            cp+=1
                
    return V

def generar_X(M,n):
    V=[]
    V=vectorPrimo(V,(n*2-1))
    c=n
    num=1
    for i in range(n):
        for j in range(n):
            if j==i:
                M[i][j]=V[i]
        for k in range(n-1,-1,-1):
            if i!=int(n/2) and k!=int(n/2) and i+k==n-1:
                M[i][k]=V[c]
                c+=1
        for l in range (n):
            if M[i][l]==0:
                M[i][l]=num
                num+=1
    return M

n = int(input("Ingrese n: "))
matriz=[]
matriz=generar(matriz,n)
matriz=generar_X(matriz,n)
mostrar_matriz(matriz)