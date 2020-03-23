"""
Problema
Pip tiene N cadenas. Cada cadena consta solo de letras de la A a la Z. Pip desea agrupar sus cadenas en grupos de tamaño K. Cada cadena debe pertenecer exactamente a un grupo.
La puntuación de un grupo es igual a la longitud del prefijo más largo compartido por todas las cadenas de ese grupo. Por ejemplo:
     El grupo {RAINBOW, RANK, RANDOM, RANK} tiene una puntuación de 2 (el prefijo más largo es 'RA').
     El grupo {FIRE, FIREBALL, FIREFIGHTER} tiene una puntuación de 4 (el prefijo más largo es 'FIRE').
     El grupo {ALLOCATION, PLATE, WORKOUT, BUNDLING} tiene una puntuación de 0 (el prefijo más largo es '').
Ayude a Pip a agrupar sus cadenas en grupos de tamaño K, de modo que se maximice la suma de las puntuaciones de los grupos.

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada caso de prueba comienza con una línea que contiene dos enteros N y K. Luego, siguen N líneas, cada una con una de las cadenas de Pip.

Salida
Para cada caso de prueba, envíe una línea que contenga el Caso #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es la suma máxima posible de puntajes.

Límites
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 105.
2 ≤ K ≤ N.
K divide a N.
Cada una de las cadenas de Pip contiene al menos un carácter.
Cada cadena consta solo de letras de la A a la Z.


Set de pruebas 1
Cada una de las cadenas de Pip contiene como máximo 5 caracteres.

Set de pruebas 2
El número total de caracteres en las cadenas de Pip en todos los casos de prueba es como máximo 2 × 10^6.

Entradas
2
2 2
KICK
START
8 2
G
G
GO
GO
GOO
GOO
GOOO
GOOO

1
6 3
RAINBOW
FIREBALL
RANK
RANDOM
FIREWALL
FIREFIGHTER

Salidas
Case #1: 0
Case #2: 10

Case #1: 6

Muestra n. ° 1
En el Caso # 1, Pip puede lograr un puntaje total de 0 haciendo que los grupos:
     {KICK, START}, con una puntuación de 0.

En el Caso # 2, Pip puede lograr un puntaje total de 10 haciendo que los grupos:
     {G, G}, con una puntuación de 1.
     {GO, GO}, con una puntuación de 2.
     {GOO, GOO}, con una puntuación de 3.
     {GOOO, GOOO}, con una puntuación de 4.

Muestra # 2
En el caso # 1, Pip puede lograr un puntaje total de 6 haciendo que los grupos:
     {RAINBOW, RANK, RANDOM}, con una puntuación de 2.
     {FIREBALL, FIREWALL, FIREFIGHTER}, con una puntuación de 4.
"""
#Para solucionar este problema hay que usar una estructura de datos llamadas Trie
#El cual es como un arbol binario, pero generalmente los indices son cadenas en vez de numeros
#Tambien se usa Deep First Search (dfs) para navegar el Trie y obtener el resultado

#Se establece el limite de llamadas recursivas
from sys import setrecursionlimit as srl
srl(2 * 10**6)

#clase para el Trie
class ctrie:
    __slots__ = 'hijo', 'cont'
    def __init__(self):
        #se crean 26 nodos hijos vacios, uno por cada letra del alfabeto
        self.hijo = [None] * 26
        self.cont = 0

#funcion resolver la cual necesita n(la cantidad de cadenas),k (el tamaño de los grupos) y a (la lista de las palabras)
def resolver(n, k, a):
    #inicio el Trie
    trie = ctrie()
    #por cada palabra en la lista
    for palabra in a:
        #asignamos el Trie a una variable
        act = trie
        #por cada letra en la palabra se agregara un Trie y se le asignara un hijo
        #por ejemplo si tenemos la palabra 'AGUA'
        #el trie original tendra un trie hijo 'A'
        #el cual tendra un trie hijo 'G'
        #el cual tendra un trie hijo 'U'
        #el cual tendra un trie hijo 'A'
        #asi se contara cuantas palabras inician con A y cuantas palabras inician con AG y asi sucesivemente
        for letra in palabra:
            #obtenemos el indice de la letra en el alfabeto, el indice inicia en 0
            #la funcion ord regresa el valor ASCII de un caracter
            #el 65 es el valor ASCII de la letra 'A'
            i = ord(letra) - 65
            #si el hijo esta vacio
            if act.hijo[i] is None:
                #el hijo pasa de ser un nodo vacio a ser un Trie
                act.hijo[i] = ctrie()
            #ahora la variable es el Trie del nodo hijo
            act = act.hijo[i]
        #Se le agrega uno al contador del Trie del nodo hijo
        act.cont += 1
    
    #se calcula la respuesta
    res=[0]
    #funcion recursiva para dfs
    #necesita el nodo y la profundidad del mismo
    def dfs(nodo, profundidad=0):
        #si el nodo contien algo
        if nodo:
            #un ciclo del 0 al 25, para recorrer el alfabeto
            for c in range(26):
                #se guarda el nodo hijo en una variable
                nh = nodo.hijo[c]
                #si el nodo no esta vacio
                if nh is not None:
                    #se llama la funcion, ahora con el nodo actual (el cual es un Trie) y se le suma 1 a la profundidad
                    dfs(nh, profundidad+1)
                    #al contador del nodo se le suma el contado del nodo hijo
                    nodo.cont += nh.cont
            #mientras que el contador del nodo sea mayor al numero maximo de palabras en el grupo
            while nodo.cont >= k:
                #se resta el numero maximos de palabras en el grupo al contador del nodo hijo
                nodo.cont -= k
                #a la respuesta se le suma la profundidad del nodo
                res[0] += profundidad
    #se llama la funcion dfs con el Trie original
    dfs(trie)
    #se regresa la respuesta
    return res[0]
                
#se lee t (numero de casos de prueba)
t = int(input())
#por cada caso de prueba
for z in range(t):
    #se lee n(la cantidad de cadenas)y k (el tamaño de los grupos)
    n,k = map(int, input().split(" "))
    #se crea una lista con todas las palabras
    a = [input() for _ in range(n)] 
    #se guarda el resultado de la funcion resolver
    res= resolver(n, k, a)
    #se muestra el resultado
    print("Case #%i: %i"%(z+1,res))
