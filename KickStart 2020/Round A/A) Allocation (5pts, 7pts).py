""" 
Problema
Hay N casas en venta. La i-ésima casa cuesta A[i] dólares para comprar. Tienes un presupuesto de B dólares para gastar.
¿Cuál es el número máximo de casas que puedes comprar?

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada caso de prueba comienza con una sola línea que contiene dos enteros N y B. La segunda línea contiene N enteros. El i-ésimo entero es A[i], es decir, el costo de la i-ésima casa.

Salida
Para cada caso de prueba, envíe una línea que contenga el Caso #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es el número máximo de casas que puede comprar.

Límites
Límite de tiempo: 15 segundos por conjunto de prueba.
Límite de memoria: 1 GB.

1 ≤ T ≤ 100.
1 ≤ B ≤ 105.
1 ≤ A[i] ≤ 1000.


Set de Prueba 1
1 ≤ N ≤ 100.

Set de Prueba 2
1 ≤ N ≤ 10^5.


Entrada
3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999

Salidas
Case #1: 2
Case #2: 3
Case #3: 0



En el Caso de ejemplo # 1, tiene un presupuesto de 100 dólares. Puedes comprar las casas primera y tercera por 20 + 40 = 60 dólares.
En el Caso de ejemplo # 2, tiene un presupuesto de 50 dólares. Puedes comprar la 1ra, 3ra y 4ta casa por 30 + 10 + 10 = 50 dólares.
En el Caso de ejemplo # 3, tiene un presupuesto de 300 dólares. No puedes comprar ninguna casa (entonces la respuesta es 0).
"""



#Se lee t (casos de prueba)
t=int(input())
for i in range(t):
    #se lee n y m
    n,m=map(int,input().split(" "))
    #lista de enteros con los precios de las casas
    a=list(map(int,input().split(" ")))
    #Se ordena el arreglo de menor a mayor
    a.sort()
    #inicio el contador y una variable para llevar el dinero
    din=cont=0
    #recorro la lista
    for j in a:
        #sumo el valor de la casa i a la variable de dinero
        din+=j
        #si el dinero es menor al m, es decir si es menor al dinero con el que se cuenta se agrega uno al contador de lo contrario se rompe el ciclo
        if din<=m: cont+=1
        elif din>m: break
    #Se imprime el resultado
    print("Case #%i: %i"%(i+1,cont))
