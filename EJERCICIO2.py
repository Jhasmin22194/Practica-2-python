'''Llenar dos vectores A y B con N números enteros positivos. Hallar el número primo mayor
de cada vector y mostrar sus factoriales. En el caso de que alguno de los vectores o los
dos no tengan números primos mostrar el mensaje “Hasta luego!!!”'''
def llenarVector(v,n):
    print(f"Ingrese {n} valores")
    for i in range (n):
        v[i]=int(input(""))
    print(v)

def esprimo(n):
    c = 0
    for j in range(1, n + 1):
        if n % j == 0:
            c += 1
    return c == 2
  
def factorial(n):
    f = 1
    for j in range(1, n + 1):
        f *= j
    return f
    
def mayor(v):
    may = v[0]
    sw = 0
    for i in v:
        if esprimo(i):
            sw = 1
            if i > may:
                may = i
    if sw == 0:
        print("Hasta luego!!!")
    else:
        print(f"Factorial de {may} = {factorial(may)}")

"""MAIN"""
n=int(input("Ingrese el valor de N: "))
va=[0]*n
vb=[0]*n
llenarVector(va,n)
llenarVector(vb,n)
mayor(va)
mayor(vb)
