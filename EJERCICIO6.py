'''
Introducir datos de N equipos de fútbol de la liga universitaria en la matriz LIGA, que son
los siguientes: “Equipo”, “Ciudad”, “Puntos”, “Partidos Jugados”, “Partidos Ganados”,
“Partidos Empatados”, “Partidos Perdidos”, “Goles a Favor”, “Goles en Contra”, y
“Número de Asistentes a sus partidos”. Mostrar la tabla resultante y el equipo más
taquillero, su ciudad y el número de asistentes.
'''
def MatrizNula(n):
    M=[[0 for _ in range (11)] for _ in range (n+1)]
    return M
def mostrarMatriz(M):
    for i in M:
        for j in i:
            print (j,end="\t")
        print("\n")
def encabezado(M):
    M[0][0]="NRO"
    M[0][1]="EQUIPO"
    M[0][2]="CIUDAD"
    M[0][3]="PUNTOS"
    M[0][4]="PJ"
    M[0][5]="PG"
    M[0][6]="PE"
    M[0][7]="PP"
    M[0][8]="GF"
    M[0][9]="GC"
    M[0][10]="ASIS"
    return M
def llenarMatriz(M,n):
    num=1
    for i in range (1,n+1):
        M[i][0]=num
        M[i][1]=input("Ingrese equipo ")
        M[i][2]=input("Ingrese ciudad ")
        M[i][3]=int(input("Ingrese puntos "))
        M[i][4]=int(input("Ingrese PJ "))
        M[i][5]=int(input("Ingrese PG "))
        M[i][6]=int(input("Ingrese PE "))
        M[i][7]=int(input("Ingrese PP "))
        M[i][8]=int(input("Ingrese GF "))
        M[i][9]=int(input("Ingrese GC "))
        M[i][10]=int(input("Ingrese ASIS "))
        num+=1
    return M
def masTaquillero(M,n):
    may=0
    for i in range (1,n+1):
        if may < M[i][10]:
            may = M[1][10]
            pos=i
    eq=M[pos][1]
    ci=M[pos][2]
    asis=M[pos][10]
    print(f"El equipo mas taquillero es {eq}, de la ciudad de {ci}")
    print(f"con {asis} asistentes")
            
        
#MAIN
n=int(input("Ingrese N: "))
M=MatrizNula(n)
M=encabezado(M)
M=llenarMatriz(M,n)
print("\t TABLA DE POSICIONES - LIGA DE FUTBOL UNIVERSITARIO - 2024")
mostrarMatriz(M)
masTaquillero(M,n)
