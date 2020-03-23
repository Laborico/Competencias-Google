"""
Problema
Tambourine ha preparado un programa de ejercicios para que pueda estar más en forma! El programa está compuesto de N sesiones. Durante la i-ésima sesión, Tambourine hará ejercicio durante M[i] minutos. La cantidad de minutos que ella ejercita en cada sesión aumenta estrictamente.
La dificultad de su programa de acondicionamiento físico es igual a la diferencia máxima en la cantidad de minutos entre dos sesiones de entrenamiento consecutivas.
Para hacer que su programa sea menos difícil, Tambourine ha decidido agregar hasta K sesiones de entrenamiento adicionales a su programa de acondicionamiento físico. Puede agregar estas sesiones en cualquier parte de su programa de acondicionamiento físico y ejercer cualquier número entero positivo de minutos en cada una de ellas. Después de agregar la sesión de entrenamiento adicional, la cantidad de minutos que ella ejercita en cada sesión debe seguir aumentando estrictamente. ¿Cuál es la dificultad mínima posible?

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada caso de prueba comienza con una línea que contiene dos enteros N y K. La segunda línea contiene N enteros, el i-ésimo de ellos es M[i], la cantidad de minutos que ejercerá en la i-ésima sesión.

Salida
Para cada caso de prueba, envíe una línea que contenga el Caso #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es la dificultad mínima posible después de agregar hasta K sesiones de entrenamiento adicionales.

Límites
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
1 ≤ T ≤ 100.
Para un máximo de 10 casos de prueba, 2 ≤ N ≤ 105.
Para todos los demás casos de prueba, 2 ≤ N ≤ 300.
1 ≤ M[i] ≤ 109.
M[i] < M[i] + 1 para todo i.

Set de Prueba 1
K = 1.

Set de Prueba 2
1 ≤ K ≤ 10^5.

Entradas
1
3 1
100 200 230

3
5 2
10 13 15 16 17
5 6
9 10 20 26 30
8 3
1 2 3 4 5 6 7 10

Salidas
Case #1: 50

Case #1: 2
Case #2: 3
Case #3: 1


Caso # 1: 2
Caso # 2: 3
Caso # 3: 1
  

Muestra n. ° 1
En el caso n. ° 1: Tambourine puede agregar hasta una sesión: 100 150 200 230. La dificultad es ahora 50.

Muestra # 2

En el caso n. ° 1: Tambourine puede agregar hasta seis sesiones: 9 10 12 14 16 18 20 23 26 29 30. La dificultad es ahora 3.

En el caso n. ° 2: Tambourine puede agregar hasta tres sesiones: 1 2 3 4 5 6 7 8 9 10. La dificultad es ahora 1. Tenga en cuenta que Tambourine solo agregó dos sesiones.
"""

#EL problema se resuelve usando busqueda binaria, solo que buscamos el minimo valor posible en lugar de un elemento en una lista


#Se lee t, el numero de casos de prueba
t=int(input())
#por cada caso de prueba
for z in range(t):
    #se lee n (el numero de sesiones) y k (la cantidad maxima de sesiones a agregar)
    n,k=map(int,input().split(" "))
    #guardamos en una lista las sesiones
    a=list(map(int,input().split(" ")))
    #definimos el minimo como 1
    mini=1
    #definimos el maximo como 10^5 ya que el problema asi lo indica
    maxi=1000000000
    #mientras que el minimo sea menor que el maximo
    while mini<maxi:
        #el punto medio es el minimo + el maximo entre 2, redondeado haca abajo
        medio=int((mini+maxi)/2)
        #se establece las sesiones a agregar en 0
        sesiones=0
        #por cada sesiones hasta n-1
        for i in range(n-1):
            #se calcula la diferencia entre la siguiente sesion y la actual
            diferencia=a[i+1]-a[i]
            #si la diferencia es mayor a el punto medio
            if diferencia>medio:
                #si la diferencia es mayor al punto medio, es decir si la difucultad del la sesion es mayor al punto medio
                #se calcula la cantidad de sesiones necesarias a agregar para disminuir la diferencia y que esta se acerca al punto medio
                #esto se hace sumando la diferencia y el medio, restando 1, despues se divide entre el punto medio (redondeando hacia abajo) y se resta 1
                #por ejemplo si la diferencia es 100 y el punto medio es 50
                #100+50-1=149
                #149/50=2.98=2
                #2-1=1
                #Tendriamos que agregar una sesion de que la difucultad baje, esto es correcto como podemos observar en la explicacion del primer caso de prueba
                sesiones+=int((diferencia+medio-1)/medio)-1
        #si las sesiones a agregar es mayor a la cantidad maxima permitida, el punto minimo se vuelve el punto medio mas uno
        if sesiones>k: mini=medio+1
        #de lo contrario el punto maximo se vuelve el medio
        else: maxi=medio
    #Se muestra la respuesta
    print("Case #%i: %i"%(z+1,mini))
