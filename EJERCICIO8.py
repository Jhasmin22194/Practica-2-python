import math

def digitos(num):
    nd=int(math.log10(num))+1
    V=[0]*nd
    c=0
    while num!=0:
        V[c]=int(num%10)
        num=int(num/10)
        c+=1
    return V
def calcularN(dig):
    c=1
    while (c**2 <= len(dig)-1):
        c+=1
    return c
def mostrarMatriz(M):
    for f in M:
        print(f)

def llenarMatriz(M,V,n):
    c=len(V)
    for i in range (n):
        for j in range (n):
            if 0<c :
                M[i][j]=V[c-1]
                c-=1
            
    mostrarMatriz(M)

num=int(input("NUM = "))
dig=digitos(num)
n=calcularN(dig)
M=[[0]*n for _ in range (n)]
llenarMatriz(M,dig,n)