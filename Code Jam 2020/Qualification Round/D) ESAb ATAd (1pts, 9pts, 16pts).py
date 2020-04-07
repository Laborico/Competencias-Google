"""
Solución de Errichto
Video explicativo: https://www.youtube.com/watch?v=AK45-rrnYhY , en ingles

Problema
El año pasado, un consorcio de investigación tuvo algunos problemas con un sistema de base de datos distribuido que a veces perdió partes de los datos. ¡No necesita leer ni comprender ese problema para resolver este!
El consorcio ha decidido que los sistemas distribuidos son demasiado complicados, por lo que almacenan B bits de información importante en una sola matriz en una máquina increíble. Como una capa adicional de seguridad, han dificultado la obtención de la información rápidamente; el usuario debe consultar una posición de bit entre 1 y B, y luego recibe ese bit de la matriz almacenada como respuesta.
Desafortunadamente, esta máquina ultramoderna está sujeta a fluctuaciones cuánticas aleatorias. Específicamente, después de cada 1, 11, 21, 31 ... etc. se envía una consulta, pero antes de dar la respuesta, la fluctuación cuántica causa exactamente uno de los siguientes cuatro efectos, con la misma probabilidad:
     El 25% del tiempo, la matriz se complementa: cada 0 se convierte en 1, y viceversa.
     El 25% del tiempo, la matriz se invierte: el primer bit se intercambia con el último bit, el segundo bit se intercambia con el penúltimo bit, y así sucesivamente.
     El 25% del tiempo, las dos cosas anteriores (complementación e inversión) le ocurren a la matriz. (Tenga en cuenta que el orden en que ocurren no importa).
     El 25% de las veces, nada le sucede a la matriz.

Además, no hay indicación de qué efecto ha tenido la fluctuación cuántica cada vez. El consorcio ahora está preocupado, ¡y lo ha contratado para recuperar sus valiosos datos, en cualquier forma en que se encuentre! ¿Puedes encontrar toda la matriz, de modo que tu respuesta sea precisa en el momento en que la des? La respuesta no cuenta como una consulta, por lo que si responde después de su 30ª consulta, por ejemplo, la matriz será la misma que después de sus consultas 21 a 30.

Entrada y Salida
Este es un problema interactivo.
Inicialmente, su programa debe leer una sola línea que contenga dos enteros T y B: el número de casos de prueba y el número de bits en la matriz, respectivamente. Tenga en cuenta que B es igual para todos los casos de prueba.
Luego, debe procesar los casos de prueba T. En cada caso, el juez comienza con una matriz B-bit predeterminada; tenga en cuenta que esta matriz puede variar de un caso de prueba a otro, y no necesariamente se elige al azar. Luego, puede realizar hasta 150 consultas de la siguiente forma:
     Su programa genera una línea que contiene un único número entero P entre 1 y B, inclusive, que indica qué posición en la matriz desea ver.
     Si el número de consultas que ha realizado hasta el momento termina con un 1, el juez elige una de las cuatro posibilidades descritas anteriormente (complementación, reversión, complementación + reversión, o nada), uniformemente al azar e independientemente de todas las demás opciones, y altera la matriz almacenada en consecuencia. (Tenga en cuenta que esto sucederá en la primera consulta que realice).
     El juez responde con una línea que contiene un solo carácter 0 o 1, el valor que ha almacenado actualmente en la posición de bit P o N si proporcionó una línea con formato incorrecto (por ejemplo, una posición no válida).

Luego, después de haber realizado tantas de las 150 consultas anteriores como desee, debe realizar un intercambio más del siguiente formulario:

    Su programa genera una línea que contiene una cadena de caracteres B, cada uno de los cuales es 0 o 1, que representa los bits almacenados actualmente en la matriz (que no necesariamente coincidirá con los bits que estaban inicialmente presentes).
    El juez responde con una línea que contiene una sola letra: Y mayúscula si su respuesta fue correcta, y N mayúscula si no fue así (o proporcionó una línea con formato incorrecto). Si recibe Y, debe comenzar el próximo caso de prueba, o dejar de enviar entradas si no hay más casos de prueba.

Después de que el juez envía N a su flujo de entrada, no enviará ninguna otra salida. Si su programa continúa esperando al juez después de recibir N, su programa expirará, dando como resultado un error de Límite de tiempo excedido. 
Tenga en cuenta que es su responsabilidad hacer que su programa salga a tiempo para recibir un fallo de respuesta incorrecta en lugar de un error de límite de tiempo excedido. Como de costumbre, si se excede el límite de memoria o si su programa recibe un error de tiempo de ejecución, recibirá el juicio correspondiente.

Limites
Límite de tiempo: 40 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
1 ≤ T ≤ 100.

Set de prueba 1
B=10

Set de prueba 2
B=20

Set de prueba 3
B=100
"""

#Para resolver el problema se necesitan encontrar 2 pares de bits, un par que es igual y uno que es diferente
#Para encontrar los pares y saber cuales son los cambios que se hicieron, hay que saber los primeros y los ultimos bits de la cadena
#Con estos bits, se es capaz de saber si hay cambios en la cadena o no

#Se cargan las funciones en memoria para optimizar tiempo de ejecucion
#Entrada
inp=input
#Entrada entera
iinp=lambda: int(inp())

#Como se tiene que preguntar constantemente por valores de la cadena, se crea esta pequeña funcion 
def preguntar(i):
    #Se muestra la posicion que se quiere saber
    print(i)
    #se regresa la entrada (la respuesta del juez)
    return iinp()


def resolver(b):
    #Se crea una lista de 0 de longuitud B+1 
    respuesta=[0 for i in range(b+1)]
    #Se inicializa un contador para la parte izquierda de la cadena
    izquierda=1
    #Se inicializa un contador para la parte derecha de la cadena
    derecha=b
    #Se inicializa un contador para las consultas
    consultas=1
    #Ciclo infinito, las operaciones se haran hasta que se muestre el resultado
    while True:
        #Si el residuo del contador de la consultas entre 10 es 1 y es diferente de 1
        #es decir, el contador es 11,21,31,etc. 
        #Quiere decir que en la siguiente consulta se realizara un cambio a la cadena
        if consultas%10==1 and consultas!=1:
            #se inicializan 2 variables, una para saber si hay un par de bits iguales (encontrado) y otro para el par de bits diferentes (diferentes)
            encontrado=-1
            diferente=-1
            #se recorre la lista hasta los valores que se saben, es decir, hasta el limite izquierdo
            for i in range(1,izquierda):
                #Si el valor de la lista con el indice i de la parte izquiera es el mismo que el de parte derecha
                #encontrado se le asigna el valor del indice i
                if respuesta[i]==respuesta[b+1-i]:
                    encontrado=i
                else:
                    #Si no son iguales, el indice i es asignado a diferente
                    diferente=i
            #Si no se pudo encontrar un par igual
            #(Al final del codigo hay una pequeña explicacion de este caso)
            if encontrado==-1:
                #se pregunta por el primer valor de la cadena
                #Al hacer esta consulta se hace un cambio a la cadena antes de que el juez regresa una respuesta
                valornuevo=preguntar(1)
                #esta llamada a preguntar solo sirve para mantener el valor de las llamadas en impar
                preguntar(1)
                #si el primer valor de la cadena es diferente, la respuesta se completa (se cambian los 0 por 1, y viceversa)
                if valornuevo!=respuesta[1]:
                    #se cambian los valores de la parte izquierda
                    for i in range(1,izquierda+1):
                        #el operador ^ significa XOR
                        #0^1=1
                        #1^1=0
                        #es una forma de invertir los valores 
                        respuesta[i]^=1
                    #se cambian los valores de la parte derecha
                    for i in range(derecha,b+1):
                        respuesta[i]^=1
            #Si se encontro un par de bits iguales
            #(Al final del codigo hay una pequeña explicacion de este caso)
            else:
                #se pregunta por el valor en el indice del par de bits encontrados
                #Al hacer esta consulta se hace un cambio a la cadena antes de que el juez regresa una respuesta
                uno=preguntar(encontrado)
                #si ese valor no es igual al que se tiene se completa la cadena
                if uno!=respuesta[encontrado]:
                    for i in range(1,izquierda+1):
                        respuesta[i]^=1
                    for i in range(derecha,b+1):
                        respuesta[i]^=1
                #Si no se encontro un par de bits diferentes solo se llama a preguntar para manterner
                #el numero de consultas en impar
                if diferente==-1:
                    preguntar(encontrado)
                else:
                    #si se encontro un par de bits diferentes
                    #se llama a preguntar, si lo que se tiene en respuesta es diferente
                    #quiere decir que tambien se volteo la cadena
                    #(Al final del codigo hay una pequeña explicacion de este caso)
                    if preguntar(diferente)!=respuesta[diferente]:
                        #volteo de cadena con slicing
                        respuesta=[0]+respuesta[-1:0:-1]
            #aumenta el contador de las consultas en 2
            consultas+=2

        #se llama a preguntar el valor en el indice de la parte izquiera y se guarda 
        respuesta[izquierda]=preguntar(izquierda)
        #se repite el proceso con la parte derecha
        respuesta[derecha]=preguntar(derecha)
        #se le agrega uno al indice izquierdo
        izquierda+=1
        #se le agrega uno al indice derecho
        derecha-=1
        #si el indice izquierdo es mayor que el derecho quiere decir que ya conocemos todos los valores de la cadena
        if izquierda>derecha:
            #se muestra la respuesta
            print(*respuesta[1::],sep='')
            #si el juez dice que es correcto se regresa 0 y se sale de la funcion resolver
            if inp()=='Y':
                return 0
            else:
                #de lo contrario se regresa 1 y se sale de la funcion resolver
                return  1
        #se suman 2 a la consultas
        #una por la consulta de la parte izquierda y otra de la parte derecha
        consultas+=2

#se lee T (la cantidad de numeros de casos) y B (la longuitud de la cadena)
t,b=map(int,inp().split(" "))
for i in range(t):
    #se guarda el retorno de la funcion
    res=resolver(b)
    #si el valor es 1 se rompe el ciclo
    if b==1:
        break

#Explicacion:
#Si no se puede encontrar un par igual de bits, por ejemplo 11111111110000000000
#si se hace un cambio en la cadena, no importa cual, el resultado seria 00000000001111111111
#por lo que solo es necesario preguntar por el primer bit y saber si es diferente al que se tiene guardado
#si es diferente solo se tiene que invertir los valores conocidos (es decir cambiar los 0 por el 1 y viceversa)


#Si se puede encontrar un par de bits iguales pero no un par de bits diferente, por ejemplo 00000000000000000000
#se pregunta por el valor de la cadena en el indice N/2, el ultimo par de bits iguales conocidos
#si se le hace un cambio a la cadena no importa cual, el resultado seria 11111111111111111111
#se pregunta por el valor en la cadena si es diferente solo se tiene que completar (es decir cambiar los 0 por el 1 y viceversa)


#Si se puede encontrar un par de bits iguales y un par de bits diferentes, por ejemplo 01010101010101010111, donde el segundo y el penultimo es un par de bits iguales
#se pregunta por el valor de la cadena en el indice 2
#si es diferente quiere decir que la cadena se completo (es decir cambiar los 0 por el 1 y viceversa)
#despues se pregunta por el valor de la cadena en el indice 10, el ultimo par de bits diferentes conocidos
#si es diferente quiere decir que la cadena tambien se invirtio, por lo que hay que invertir la cadena tambien