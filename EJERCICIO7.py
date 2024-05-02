'''
Generar la Matriz M de tamaño NxN
'''
def mostrar_matriz(matriz):
    for f in matriz:
        print(f)

def generar( n, m):
    matriz = [  [ 0 for _ in range(n) ] for _ in range(m) ]
    return matriz


def generar_fila(izq, der, m):
    fila = []
    c = 1
    for i in range(m):
        if i >= izq and i <=der:
            fila = fila + [c]
            c = c + 1
        else:
            fila = fila + [0]
    return fila

n = int(input("Ingrese n: "))

izq = 0
der = n-1
matriz = []
for i in range(1, n+1):
    matriz = matriz + [generar_fila(izq, der, n)]  
    if(i < ((n//2)+1)):
        izq = izq + 1
        der = der - 1
    else:
        izq = izq - 1
        der = der + 1

mostrar_matriz(matriz=matriz)