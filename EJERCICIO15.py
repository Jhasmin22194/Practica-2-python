'''
 Dado un vector NOM que contiene los nombres de N estudiantes, ordenarlos 
alfabéticamente y buscar un nombre dado en el vector. Si lo encuentra debe dar como 
resultado la posición en la que lo encontró, en caso contrario mostrar el mensaje “No 
existe el nombre”. (Aplicar búsqueda binaria).
'''
def ordenar_burbuja(V,n):
    for i in range(n):
        for j in range(0, n-i-1):
            if V[j] > V[j+1]:
                V[j], V[j+1] = V[j+1], V[j]
    return V

def busqueda_binaria(V, e, n):
    iz = 0
    de = n - 1

    while iz <= de:
        me = (iz + de) // 2
        if V[me] == e:
            return me
        elif V[me] < e:
            iz = me + 1
        else:
            de = me - 1

    return -1  

def llenarVector (V,n):
    for i in range (n):
        V[i]=input()
        
def mostrarVector (V,n):
    for i in range (n):
        print("[",V[i],"]", end=" ")
    print("")
        

n=int(input("N = "))
V=[0]*n
print(f"Ingrese {n} nombres")
llenarVector(V,n)
print("Entrada:")
mostrarVector(V,n)
print("Salida:")
V=ordenar_burbuja(V,n)
ele=input("EST = ")
print(V)
if busqueda_binaria(V,ele,n) != -1:
    print(f" {ele} se encuentra en la posicion {busqueda_binaria(V,ele,n)}")
else:
    print("No existe el nombre")