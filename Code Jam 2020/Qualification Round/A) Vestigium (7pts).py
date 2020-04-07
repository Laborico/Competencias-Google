"""
Problema
Vestigium significa "rastro" en latín. En este problema, trabajamos con cuadrados latinos y trazos matriciales.
El trazo de una matriz cuadrada es la suma de los valores en la diagonal principal (que se extiende desde la parte superior izquierda a la inferior derecha).
Una matriz cuadrada N por N es un cuadrado latino si cada celda contiene uno de N valores diferentes, y no se repite ningún valor dentro de una fila o columna. En este problema, trataremos solo con "cuadrados latinos naturales" en los que los valores de N son los enteros entre 1 y N.
Dada una matriz que contiene solo enteros entre 1 y N, queremos calcular su traza y verificar si es un cuadrado latino natural. Para dar información adicional, en lugar de simplemente decirnos si la matriz es un cuadrado latino natural o no, calcule el número de filas y el número de columnas que contienen valores repetidos.

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada uno comienza con una línea que contiene un solo número entero N: el tamaño de la matriz a explorar. Luego, siguen N líneas. El i-ésimo de estas líneas contiene N enteros Mi, 1, Mi, 2 ..., Mi, N. Mi, j es el número entero en la i-ésima fila y j-ésima columna de la matriz.

Salida
Para cada caso de prueba, envíe una línea que contenga el Case #x: k r c, donde x es el número de caso de prueba (comenzando desde 1), k es el rastro de la matriz, r es el número de filas de la matriz que contienen elementos repetidos, y c es el número de columnas de la matriz que contienen elementos repetidos.

Limites
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.

1 ≤ T ≤ 100.
2 ≤ N ≤ 100.
1 ≤ Mi,j ≤ N, for all i, j.

Entradas
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

Salidas
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2



En el caso de ejemplo # 1, la entrada es un cuadrado latino natural, lo que significa que ninguna fila o columna tiene elementos repetidos. Los cuatro valores en la diagonal principal son 1, por lo que la traza (su suma) es 4.
En el caso de ejemplo # 2, todas las filas y columnas tienen elementos repetidos. Observe que cada fila o columna con elementos repetidos se cuenta solo una vez, independientemente del número de elementos que se repiten o con qué frecuencia se repiten dentro de la fila o columna. Además, observe que algunos enteros en el rango de 1 a N pueden estar ausentes de la entrada.
En el caso de ejemplo # 3, las columnas más a la izquierda y a la derecha tienen elementos repetidos.
"""


#Se cargan las funciones en memoria para optimizar tiempo de ejecucion
#Entrada
inp=input
#Entrada entera
iinp= lambda: int(inp())
#Lista de enteros 
li=lambda: list(map(int,inp().split(" ")))
#Longuitud de un set
ls=lambda x: len(set(x))

def resolver():
    #Se declara res, variable para la respuesta
    res=''
    #Se lee N, el tamaño de la matriz
    n=iinp()
    #Se declara una variable para la matriz
    mat=[]
    #Se declara una lista para las columnas
    b=[]
    #Se inicializa K (la suma de la diagonal), R (la cantidad de filas que se repite) y C (la cantidad de columnas que se repite) en 0
    k=r=c=0
    #Se leen N filas
    for i in range(n):
        #Se guarda la fila como una lista de enteros
        a=li()
        #Se agrega la lista a la matriz
        mat.append(a)
        #Si la longuitud del set es diferente de N, quiere decir que hay elementos repetidos en la fila
        #Un set una collecion de datos que no se repite, si se convierte la lista de enteros en un Set se eliminan los valores repitodos
        if ls(a)!=n:
            r+=1
    #Se recorre la matriz
    for i in range(n):
        #Se hace la suma de cada elemento de la diagonal
        k+=mat[i][i]
        #Se recorre la matriz para agregar cada valor de la columna actual
        for j in range(n):
            b.append(mat[j][i])
        #Si la longuitud del set es diferente de N, quiere decir que hay elementos repetidos en la columna
        if ls(b)!=n:
            c+=1
        #Se reinicia la lista de los valores de la columna
        b=[]
    #en la variable de la respuesta se le asignan los valores de K,R y C en el formato deseado
    res+=str(k)+" "+str(r)+" "+str(c)
    #la funcion resolver regresa la variable respues con el formato deseado
    return res

#Se lee T (Numero de casos de prueba)
t=iinp()
for i in range(t):
    #Se asigna el resultado de la funcion resolver a la variable res
    res=resolver()
    #Se muestra el resultado en el formato pedido
    print("Case #%i: %s"%(i+1,res))