"""
Problema:
¡El hijo de Cameron y Jamie tiene casi 3 años! Sin embargo, a pesar de que el niño es más independiente ahora, programar las actividades de los niños y las necesidades domésticas sigue siendo un desafío para la pareja.
Cameron y Jamie tienen una lista de N actividades para cuidar durante el día. Cada actividad ocurre durante un intervalo específico durante el día. Deben asignar cada actividad a una de ellas, de modo que ninguno de ellos sea responsable de dos actividades que se superpongan. No se considera que una actividad que termina en el tiempo t se solape con otra actividad que comienza en el tiempo t.
Por ejemplo, supongamos que Jamie y Cameron necesitan cubrir 3 actividades: una de 18:00 a 20:00, otra de 19:00 a 21:00 y otra de 22:00 a 23:00. Una posibilidad sería que Jamie cubriera la actividad de 19:00 a 21:00, con Cameron cubriendo las otras dos. Otro horario válido sería que Cameron cubra la actividad de 18:00 a 20:00 y Jamie cubra las otras dos. Observe que las dos primeras actividades se superponen en el tiempo entre las 19:00 y las 20:00, por lo que es imposible asignar ambas actividades al mismo socio.
Dadas las horas de inicio y finalización de cada actividad, encuentre cualquier horario que no requiera que la misma persona cubra actividades superpuestas, o diga que es imposible.

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada caso de prueba comienza con una línea que contiene un solo número entero N, el número de actividades a asignar. Luego, siguen más N líneas. El i-ésimo de estas líneas (contando a partir de 1) contiene dos enteros Si y Ei. La i-ésima actividad comienza exactamente Si minutos después de la medianoche y termina exactamente Ei minutos después de la medianoche.

Salida
Para cada caso de prueba, envíe una línea que contenga el Case #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es IMPOSSIBLE si no hay un programa válido de acuerdo con las reglas anteriores, o una cadena de exactamente N caracteres de otra manera. El i-ésimo carácter en y debe ser C si la i-ésima actividad está asignada a Cameron en su horario propuesto, y J si está asignada a Jamie.
Si hay varias soluciones, puede generar cualquiera de ellas.

Limites
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
1 ≤ T ≤ 100.
0 ≤ Si <Ei ≤ 24 × 60.

Set de prueba 1
2 ≤ N ≤ 10

Set de prueba 2
2 ≤ N ≤ 1000

Entradas
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

Salidas
Case #1: CJC
Case #2: IMPOSSIBLE
Case #3: JCCJJ
Case #4: CC

El caso de ejemplo n.º 1 es el que se describe en la declaración del problema. Como se mencionó anteriormente, hay otras soluciones válidas, como JCJ y JCC.
En el Caso de ejemplo # 2, las tres actividades se superponen entre sí. Asignarlos a todos significaría que alguien terminaría con al menos dos actividades superpuestas, por lo que no hay un horario válido.
En el caso de ejemplo # 3, observe que Cameron finaliza una actividad y comienza otra en el minuto 100.
En el caso de muestra # 4, cualquier horario sería válido. Específicamente, está bien que un socio realice todas las actividades.
"""

#Se cargan las funciones en memoria para optimizar tiempo de ejecucion
#Entrada
inp=input
#Entrada entera
iinp=lambda : int(inp())
#Lista de enteros 
li=lambda: list(map(int,inp().split(" ")))

#funcion resolver
def resolver():
    #se crea la variable res para guardar el resultado
    res=''
    #se inicializa una bandera en True
    ban=True
    #Se lee la cantidad de actividades
    n=iinp()
    #Se crea una lista vacia para Camareon
    C=[]
    #Se crea una lista vacia para Jamie
    J=[]
    #Se crea una lista para las actividades
    s=[]
    #por cada actividad
    for i in range(n):
        #se guarda un lista de las actividades en la lista s
        #creando una lista de listas
        s.append(li())
    #Se crea una copia de la ordenada de lista S
    #Python al hacer sort de una lista de listas, toma el primer valor de cada lista para hacer el sort
    ss=sorted(s)
    #Por cada actividad
    for i in range(n):
        #Si la lista de Cameron esta vacia, se agrega la lista con las 2 horas a la lista de Cameron
        if len(C)==0:
            C.append(ss[i])
        else:
            #si no esta vacia
            #Se inicializa una bandera BC en falso
            bc=False
            #por cada lista en lista de cameron
            for j in range(len(C)):
                #si la lista actual es igual alguna lista en la lista de Cameron 
                #significa que tiene una actividad en ese mismo horario y no puede realizarla
                if ss[i]==C[j]:
                    #Se cambia a True la bandera JC y se rompe el ciclo
                    bc=True
                    break 
                #Si la hora de inicio de la actividad actual es mayor o igual a la hora de finalizacion de la actividad actual de Cameron
                #o si la hora de finalizacion acutal es menor o igual a la hora de inicio de la actividad de Cameron
                #significa que puede realizar la actividad actual 
                elif ss[i][0]>=C[j][1] or ss[i][1]<=C[j][0]: pass
                else:
                    #Si no se cumple ninguno de los criterios se cambia la bandera BC a True y se rompe el ciclo
                    #Por que Cameron no sera capaz de realizar la actividad
                    bc=True
                    break
            #Si la bandera BC  es Falsa, se agrega la actividad a la lista de actividades de Cameron
            #de lo contrario se realiza el mismo proceso para Jamie
            if not bc:
                C.append(ss[i])
            else:
                #Si la lista de Jamie esta vacia, se agrega la lista con las 2 horas a la lista de Jamie
                if len(J)==0:
                    J.append(ss[i])
                else:
                    #si no esta vacia
                    #Se inicializa una bandera BJ en falso
                    bj=False
                    #por cada lista en la lista de Jamie
                    for j in range(len(J)):
                        #si la lista actual es igual alguna lista en la lista de Jamie 
                        #significa que tiene una actividad en ese mismo horario y no puede realizarla
                        if ss[i]==J[j]:
                            bj=True
                            break
                        #Si la hora de inicio de la actividad actual es mayor o igual a la hora de finalizacion de la actividad actual de Jamie
                        #o si la hora de finalizacion acutal es menor o igual a la hora de inicio de la actividad de Jamie
                        #significa que puede realizar la actividad actual 
                        elif ss[i][0]>=J[j][1] or ss[i][1]<=J[j][0]: pass
                        else:
                            #Si no se cumple ninguno de los criterios se cambia la bandera BJ a True y se rompe el ciclo
                            bj=True
                            break
                    #Si la bandera BJ no es Falsa, se agrega la actividad a la lista de actividades de Cameron 
                    if not bj:
                        J.append(ss[i])
                    else:
                        #Si la bandera ban se hace False, significa que es imposible realizar todas las actividades bajo el criterio del problema
                        ban=False
    #Si la bandera ban es True quiere decir que todas las actividades se pueden realizar
    if ban:
        #El juez espera que el resultado este ordenado de acuerdo al orden que se ingresa las actividades
        #Por lo que hay que acomodar la respuesta en dicho orden
        #por cada actividad
        for i in range(n):
            #Se guarda la longuitud de la lista de Cameron 
            lon=len(C)
            #por cada actividad en la lista de Cameron
            for j in range(lon):
                #Si la actividad actual de lista sin ordernar es igual a la actividad actual de Cameron
                if s[i]==C[j]:
                    #Se agrega C a la respuesta
                    res+='C'
                    #Se le quita la actividad a la lista de Cameron
                    C.pop(j)
                    #se le resta 1 a la longuitud
                    lon-=1
                    #se rompe el ciclo
                    break
            #en Python se puede usar un else con un ciclo for
            #se usa para cuando un ciclo no se rompe
            #si no se rompe el ciclo quiere decir que Cameron no tenia la actividad
            else:
                #Se agrega J a la respuesta
                res+='J'
        #la funcion retorna la respuesta
        return res
    else:
        #Si la bandera es falsa, se retorna IMPOSSIBLE
        return "IMPOSSIBLE"

#Se lee T (Cantidad de casos de prueba)
t=iinp()
for i in range(t):
    #Se guarda el resultado de la funcion resolver
    res=resolver()
    #Se muesta la respuesta en la forma deseada
    print("Case #%i: %s"%(i+1,res))