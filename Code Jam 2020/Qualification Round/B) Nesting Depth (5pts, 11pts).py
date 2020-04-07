"""
Problema
tl; dr: Dada una cadena de dígitos S, inserte un número mínimo de paréntesis de apertura y cierre de manera que la cadena resultante esté equilibrada y cada dígito d esté exactamente dentro de d pares de paréntesis coincidentes.
Deje que el anidamiento de dos paréntesis dentro de una cadena sea la subcadena que ocurre estrictamente entre ellos. Se dice que un paréntesis de apertura y un paréntesis de cierre que está más a la derecha coinciden si su anidamiento está vacío, o si cada paréntesis en su anidamiento coincide con otro paréntesis en su anidamiento. La profundidad de anidación de una posición p es el número de pares de paréntesis coincidentes m, de modo que p se incluye en el anidamiento de m.
306/5000
Por ejemplo, en las siguientes cadenas, todos los dígitos coinciden con su profundidad de anidación: 0 ((2) 1), (((3)) 1 (2)), ((((4)))), (((2)) ((2)) (1). Las primeras tres cadenas tienen una longitud mínima entre aquellas que tienen los mismos dígitos en el mismo orden, pero la última no tiene (dado que ((22) 1) también tiene los dígitos 221 y es más corta.
Dada una cadena de dígitos S, encuentre otra cadena S', compuesta de paréntesis y dígitos, de modo que:
     todos los paréntesis en S' coinciden con otros paréntesis,
     eliminar cualquiera y todos los paréntesis de los resultados de S en S,
     cada dígito en S' es igual a su profundidad de anidación, y
     S' es de longitud mínima.

Entrada
La primera línea de la entrada da el número de casos de prueba, las líneas T. T lineas siguen. Cada línea representa un caso de prueba y contiene solo la cadena S.

Salida
Para cada caso de prueba, envíe una línea que contenga el Case #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es la cadena S 'definida anteriormente.

Limite
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
1 ≤ T ≤ 100.
1 ≤ longuitud de S ≤ 100.

Set de prueba 1
Cada caracter de S es 0 o 1.

Set de prueba 2
Cada caracter de S es un numero decimal entre 0 y 9, inclusivo.

Entradas
4
0000
101
111000
1

Salidas
Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)

Las cadenas () 0000 (), (1) 0 (((())) 1) y (1) (11) 000 no son soluciones válidas para los Casos de muestra # 1, # 2 y # 3, respectivamente, solo porque No son de longitud mínima. Además, 1) (y) (1 no son soluciones válidas para el Caso de muestra # 4 porque contienen paréntesis sin igual y la profundidad de anidación es 0 en la posición donde hay un 1.
Puede crear entradas de muestra que sean válidas solo para el Conjunto de pruebas 2 eliminando los paréntesis de las cadenas de ejemplo mencionadas en la declaración del problema.
"""



#Se cargan las funciones en memoria para optimizar tiempo de ejecucion
#Entrada
inp=input
#Entrada entera
iinp= lambda: int(inp())
#Funcion Ord, dado un caracter regresa su valor ANSII
o=ord
def resolver():
    #Se lee S
    s=inp()
    #Variable res para la respuesta
    res=''
    #Se inicializa la profundidad en 0
    profundidad=0
    #Por cada caracter de S
    for i in s:
        #n es el valor ANSII del caracter actual menos 48 (valor ANSII de 0)
        n=o(i)-48
        #Para saber cuantos ( se necesitan, se resta al digito la profundidad 
        #Si el digito es mayor se necesitan mas (
        #en python multiplar un caracter o una cadena por un numero N, da como resultado el caracter o la cadena multipliacada N veces
        #Si es el numero N es menor o igual que 0, da como resultado una cadena vacia
        res+='('*(n-profundidad)
        #Para saber cuantos ) se necesitan, se resta a la profundidad el digito
        #Si la profundidad es mayor, se necesitan mas )
        res+=')'*(profundidad-n)
        #Se agrega el digito a la cadena
        res+=i
        #La profundidad se convierte en el digito actual
        profundidad=n
    #Si quedan ) pendientes, se agregan
    res+=')'*profundidad
    #la funcion regresa la respuesta
    return res
     
#Se lee T, la cantidad de casos de pruebas
t=iinp()
for i in range(t):
    #Se le asigna a la variable res el resultado de la funcion resolver
    res=resolver()
    #Se muestra en el formato deseado
    print("Case #%i: %s"%(i+1,res))