'''Generar el vector V de tamaño N de la siguiente forma:
    N = 10 [1 3 4 2 5 7 8 6 9 11]
'''
def generarVector (V,n):
    c=0
    num=1
    for i in range (n):
        V[i]=num
        if c==0:
            num+=2
            c+=1
        elif c==1:
            num+=1
            c+=1
        elif c==2:
            num-=2
            c+=1
        elif c==3:
            num+=3
            c=0
        
def mostrarVector (V,n):
    for i in range (n):
        print("[",V[i],"]", end=" ")
    print("")
        

n=int(input("Ingrese el valor de N: "))
V=[0]*n
generarVector(V,n)
mostrarVector(V,n)
