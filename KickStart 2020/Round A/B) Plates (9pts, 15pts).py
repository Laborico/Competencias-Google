""" 
Problema
El Dr. Patel tiene N pilas de platos. Cada pila contiene K platos. Cada plato tiene un valor de belleza positivo, que describe cuán hermoso se ve.
El Dr. Patel quisiera tomar exactamente los platos P para cenar esta noche. Si a él le gustaría tomar un plato en una pila, también debe tomar todos los platos que están encima de él en esa pila.
Ayude al Dr. Patel a elegir las platos P que maximizarían la suma total de los valores de belleza.

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada caso de prueba comienza con una línea que contiene los tres enteros N, K y P. Luego, siguen N líneas. La línea i-ésima contiene K enteros, que describen los valores de belleza de cada pila de platos de arriba a abajo.

Salida
Para cada caso de prueba, envíe una línea que contenga el Caso #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es la suma total máxima de valores de belleza que el Dr. Patel podría elegir.

Límites
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
1 ≤ T ≤ 100.
1 ≤ K ≤ 30.
1 ≤ P ≤ N * K.
Los valores de belleza están entre 1 y 100, inclusive.

Set de Prueba 1
1 ≤ N ≤ 3.

Set de Prueba 2
1 ≤ N ≤ 50.


Entradas
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10

Salidas
Case #1: 250
Case #2: 180

En el caso de muestra n.º 1, el Dr. Patel necesita elegir P = 5 platos:
     Puede elegir los 3 mejores platos de la primera pila (10 + 10 + 100 = 120).
     Puede elegir las 2 mejores placas de la segunda pila (80 + 50 = 130).
En total, la suma de los valores de belleza es 250.

En el caso de muestra # 2, el Dr. Patel necesita elegir P = 3 platos:
     Puede elegir las 2 mejores placas de la primera pila (80 + 80 = 160).
     No puede recoger platos de la segunda pila.
     Puede elegir el plato superior de la tercera pila (20).
En total, la suma de los valores de belleza es 180.

Muy parecido al problema de Knapsack pero con algo de complejidad extra
https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem

Este problema probablemente es el mas confuso de explicar

"""
#Establezco el limite de llamadas recursivas 
from sys import setrecursionlimit as srl
srl(10**5)

#Una solucion optima es usar Programacion dinamica, es decir dividir el problema en subproblemas mas pequeños

#la funcion resolver necesita los valores n (la cantidad de pilas de platos), k (la cantidad de platos en cada pila), p (la cantidad de platos a tomar) y a (la lista de listas que contien todos los valores de los platos)
def resolver(n, k, p, a):
    #Nuestro primer subproblema es resolver la suma de cada plato hasta i, ya que si el Dr.Patel decide tomar el cuarto plato debe de tomar los primeros 3
    #es decir debemos de saber la suma de la belleza de cada plato hasta cada elemento i
    sumas = []
    #por cada fila de platos en la lista de listas de los platos
    for fila in a:
        #una lista temporal para guardar la suma
        s = [0]
        #por cada plato en la fila
        for x in fila:
            #se agrega la suma de cada plato hasta i, en la lista temporal
            s.append(s[-1] + x)
        #se agrega la lista temporal a la lista de sumas
        sumas.append(s)

    #un diccionario que se usara como memoria para optimimzar el calculo de la solucion
    #esta tecnica se en programacion dinamica se llama "memoization"
    #Si quieres aprender mas de programacion dinamica dejo aqui un link de una clase del MIT sobre lo mismo, esta en ingles
    #https://www.youtube.com/watch?v=OQ5jsbhAv_M&list=FLRa5-GQpedO58BNyXXy7CnQ&index=11&t=0s
    memo = {}
    #funcion dp, funcion es recursiva, toma los valores de i (el indice de la pila de platos) y tomado (la cantidad de platos a tomar)
    #el siguiente subproblema es calcular todas las sumas posibles de con las condiciones del problema
    #la recursion es la forma mas eficaz de hacerlo
    #la funcion lo que hace es calcular, por ejemplo, si tomo 2 platos de la primera fila y tomo 3 de la siguiente, cuanto es la suma
    def dp(i, tomado):
        #si la cantidad de platos a tomar es 0 o el indice de las pilas es igual a la cantidad de pilas, regresa 0
        if tomado == 0 or i == n:
            return 0
        #si la tupla de indice con la cantidad de platos tomados ya esta en memoria, regreso el valor en memoria
        if (i, tomado) in memo:
            return memo[i, tomado]

        #Si no se cumplen las condiciones, hay que calcular la respuesta
        res = 0
        #Cada plato en las filas puede ser una eleccion
        for eleccion in range(k+1):
            #una variable temporal, con la cual calculamos la cantidad de platos a tomar de la fila
            tomado2 = tomado - eleccion
            #si la cantidad es 0, se rompe el ciclo
            if tomado2 < 0: break
            #Calculamos el valor, se llama a la siguiente fila con los platos a sumar y se le suma el valor de la cantidad de platos actual
            #es decir si p es 5, y tomamos 3 platos de la primer fila (el valor ya esta guardado en sumas), necesitamos saber la el valor de la suma de los 2 platos restantes de la siguiente fila
            tmp = dp(i+1, tomado2) + sumas[i][eleccion]
            #si esta nueva suma es mayor a nuestra respuesta actual, la respuesta se convierte en la nueva suma
            if tmp>res: res=tmp
        #Guardamos la respuesta en memoria
        memo[i, tomado] = res
        #retornamos la respuesta
        return res
    #al llamar a la funcion resolver, regresamos el valor de dp(0, cantida de platos a tomar)
    #el 0 solo sirve de manera arbitraria, solo para saber la ultima respuesta posible, es por eso que al usar la variable temporal arriba, siempre llamamos dp(i+1)
    return dp(0, p)

#se lee t, la cantidad de casos de prueba
t=int(input())
#por cada caso de prueba
for i in range(t):
    #se lee n (la cantidad de pilas de platos), k (la cantidad de platos en cada pila), p (la cantidad de platos a tomar)
    n,k,p= map(int, input().split(" "))
    #se guarda cada valor de los platos en una lista de mapas, 
    a = [map(int, input().split(" ")) for _ in range(n)]
    #se llama a resolver y se guarda el valor el una variable
    res = resolver(n, k, p, a)
    #se muestra el resultado
    print("Case #%i: %i"%(i+1, res))
