"""
Video explicativo de la solución: https://www.youtube.com/watch?v=VayKvCg4vvQ por Errichto, esta en Ingles

Problema:
Indicium significa "rastro" en latín. En este problema, trabajamos con cuadrados latinos y trazas matriciales.
Un cuadrado latino es una matriz cuadrada N por N en la que cada celda contiene uno de N valores diferentes, de modo que no se repite ningún valor dentro de una fila o columna. En este problema, trataremos solo con "cuadrados latinos naturales" en los que los valores de N son los enteros entre 1 y N.
La traza de una matriz cuadrada es la suma de los valores en la diagonal principal (que se extiende desde la parte superior izquierda a la inferior derecha).
Dados los valores N y K, produzca cualquier "cuadrado latino natural" N-por-N con traza K, o diga que es imposible. Por ejemplo, aquí hay dos respuestas posibles para N = 3, K = 6. En cada caso, los valores que contribuyen a la traza están subrayados.
2_ 1  3   3_ 1  2
3  2_ 1   1  2_ 3
1  3  2_  2  3  1_

Entrada
La primera línea de la entrada da el número de casos de prueba, los casos de prueba T. T lineas siguen. Cada uno consta de una línea que contiene dos enteros N y K: el tamaño deseado de la matriz y la traza deseada.

Salida
Para cada caso de prueba, envíe una línea que contenga el Case #x: y, donde x es el número de caso de prueba (comenzando desde 1) e y es IMPOSSIBLE si no hay respuesta para los parámetros dados o POSSIBLE de lo contrario. En el último caso, genera N más líneas de N enteros cada una, que representan un "cuadrado latino natural" válido con un rastro de K, como se describió anteriormente.

Limites
Límite de tiempo: 20 segundos por conjunto de prueba.
Límite de memoria: 1 GB.
N ≤ K ≤ N².

Set de prueba 1
T = 44.
2 ≤ N ≤ 5.

Set de prueba 2
1 ≤ T ≤ 100.
2 ≤ N ≤ 50.

Entradas
2
3 6
2 3

Salidas
Case #1: POSSIBLE
2 1 3
3 2 1
1 3 2
Case #2: IMPOSSIBLE

El caso de ejemplo n.º 1 es el que se describe en la declaración del problema.
El caso de ejemplo # 2 no tiene respuesta. Los únicos "cuadrados latinos naturales" 2 por 2 posibles son los siguientes:
1 2   2 1
2 1   1 2
Estos tienen trazas de 2 y 4, respectivamente. No hay forma de obtener un rastro de 3.
"""
#Para la solución de este problema es necesario conocer Bitpartite Marching y el teorema de Hall
#Sugiero altamente ver el vídeo de la explicación para entender por completo la solución, en ingles
#https://www.youtube.com/watch?v=VayKvCg4vvQ

#Se cargan las funciones en memoria para optimizar tiempo de ejecucion
#Entrada
inp=input
#Entrada entera
iinp= lambda: int(inp())
#Varias entradas enteras
ent=lambda : map(int,inp().split(" "))


#La forma sencilla de resolver el problema es encontrando la diagonal con la suma
#Y llenando el resto de la matriz como si fuera un sodoku
#De esta forma se obtiene un cuadradro latino


#Esta parte del codigo es algo dificil de explicar, te recomiendo ver el video de la solucion para que 
#entiendas mejor el tema de Bitpartite

#El Bitpartite se utiliza para resolver el resto de la matriz como sodoku

#Se crea la clase Bitpartite, que necesita 2 variables, N y M
#Estas para crear la matriz
class bitpartite:
    #en Python se puede sobreescribir las funciones de clase
    #en este se sobreescribe la funcion init, cuando se manda a llamar la clase
    #la funcion init se activa automaticamente, es parecido a los constructores en otros lenguajes de programacion
    def __init__(self,n,m):
        #Lo siguiente es parecido a la declaracion de variables en POO
        #Se declara la n de la clase como la n que se recibe
        self.n=n
        #se declara la m de la clase como la m que se recibe
        self.m=m
        #Se inicializa una matriz de tamaño n en -1, llamado pre 
        #En esta matriz se almacenan los valores de los indices antes de ser cambiados
        self.pre=[-1 for i in range(self.n)]
        #Se inicializa una matriz de tamaño n en -1, llamado raiz
        #En esta matriz se guardan los indices de posibles respuestas
        self.raiz=[-1 for i in range(self.n)]
        #Se inicializa una matriz de tamaño n en -1, llamado p
        #En esta matriz se almacena la posicion final del valor 
        self.p=[-1 for i in range(self.n)]
        #Se inicializa una matriz de tamaño en -1, llamado q
        #En esta matriz se agregan los indices relacionados a p
        self.q=[-1 for i in range(self.m)]
        #Se inicializa una matriz de matrices vacias de tamaño n en, llamado hacia
        #En esta se guardan los indices disponibles para llenar la matriz
        self.hacia=[[] for i in range(self.n)]

    #Funcion agregar, en ella se agregan los indices disponibles de la matriz respuesta
    #necesita dos valores enteros a y b
    def agregar(self,a,b):
        #A la matriz a se le agrega el valor b
        #Hacia es un matriz de matrices
        self.hacia[a].append(b)
    #Funcion solucion, obtiene las posiciones en la matriz de un valor
    def solucion(self):
        #se crea una bandera para saber si hay una actualizacion a los valores de las posiciones
        act=True
        #un ciclo activado siempre que exista una actualizacion
        while act:
            #se cambia la bandera a falso
            act=False
            #se crea una lista llamada S, almacena las posiciones posibles de un valor
            #lo mejor seria, por ejemplo en C++, usar una queue
            s=[]
            #Un ciclo hasta n
            for i in range(self.n):
                #El operador ~ invierte los bits de un valor
                #Esto lo que haces es que convierte el -1 en 0
                #y despues niega el 0, conviertiendo en True
                #es una forma eficiente de saber si un valor funciona o no
                if not ~self.p[i]:
                    #Si pasa la condicion se guarda el valor en la matriz de raiz
                    self.raiz[i]=i
                    #se agrega el indice a la lista S
                    s.append(i)
            #Un ciclo que se repetira siempre y cuando la lista S no este vacia
            while len(s):
                #Se guarda el primer elemento de la lista S en una variable V
                v=s[0]
                #Se remueve el primer elemento de la lista
                s.remove(s[0])
                #Si en la matriz p existe un valor que este en el indice de la matriz raiz cuyo indice es V
                #Hay que recordar que la matriz raiz guarda los indices de las posibles soluciones
                if ~self.p[self.raiz[v]]:
                    #Si existe un valor se continuea con la siguiente iteraccion del ciclo while
                    continue
                #Si no, se recore la matriz hacia, que contiene todas las posibles posiciones
                for i in range(len(self.hacia[v])):
                    #Se guarda en una variable u el valor de una posible posicion
                    u=self.hacia[v][i]
                    #si en la matriz q existe un valor que este en el indice de la matriz raiz cuyo indice es U
                    if not ~self.q[u]:
                        #Un ciclo que se repetira siempre que el valor invertido de u no se negativo
                        while ~u:
                            #Se guarda el valor V en el indice U de la matriz q
                            self.q[u]=v
                            #Se guarda en una variable temporal el valor de u
                            tmp=u
                            #A la variable U se le asigna el valor que esta en el indice V de la matriz p
                            u=self.p[v]
                            #Se le asigna al indice V de la matriz p el valor de la variable temporal 
                            self.p[v]=tmp
                            #Se le asigna el valor del indice V de la matriz pre a la variable V
                            v=self.pre[v]
                        #Como hubo actualizaciones en las matrices se enciende la bandera
                        act=True
                        #Se rompe el ciclo for
                        break
                    #Se guarda el valor del indice U de la matriz q en la variable u
                    u=self.q[u]
                    #Si el indice U de la matriz pre no es -1, se continua con la siguiente iteraccion del ciclo for
                    if ~self.pre[u]:
                        continue
                    #de lo contrario se le asigna el valor de V
                    self.pre[u]=v
                    #el valor del indice u se cambia por el del indice v de la matriz raiz
                    self.raiz[u]=self.raiz[v]
                    #se agrega el valor de U a la lista S
                    s.append(u)
            #Si la bandera esta en True hay que reiniciar las matrices pre y raiz
            if act:
                self.pre=[-1 for i in range(self.n)]
                self.raiz=[-1 for i in range(self.n)]
        return 0

#La funcion resolver necesita los parametros N (Tamaño de la matriz) y K (El resultado deseado del trazo)
def resolver(n,k):
    #Si el trazo deseado es menor que el tamaño de la matriz o mayor que el tamaño al cuadrado de la matriz 
    #es imposible resolver la matriz, por ejemplo si el tamaño de la matriz es 4 y el numero del trazo deseado es 3
    #es imposible de resolver, por que no hay 4 numeros positivos cuya suma de 3
    #y si el tamaño de la matriz es 4 el numero del trazo deseado es 17, es imposible de resolver
    #si hay 4 numeros positivos cuya suma es 17, pero no son iguales o consecutivos, requisitos para crear el cuadrado latino
    if k<n or k>n*n: 
        #retorna IMPOSSIBLE y sale de la funcion
        return print("IMPOSSIBLE")
    #Se crea una matriz de N*N, en la cual se almacenara el resultado
    respuesta=[[0 for i in range(n)]for i in range(n)]
    #Si el residuo de K entre N es 0, quiere decir que la diagonal de la matriz puede ser llenada inmediatamente
    #por ejemplo si el tamaño de la matriz es 3 y el tamaño del trazo deseado es 6, la diagonal de la matriz
    #puede ser llenada con 2
    if k%n==0:
        #Se llena la diagonal con el resultado de la division de k entre n
        #es Python se usa // para truncar el resultado de una division a entero
        for i in range(n):
            respuesta[i][i]=k//n
    else:
        #Si el trazo deseado es mayor que el tamaño de la matriz por uno o igual al tamaño al cuadrado menos 1
        #Es imposible realizar un cuadrado latino, por que no hay N numeros iguales o consecutivos que den como resultado N+1
        #Al igual que no hay N numeros consecutivos o iguales que sumados den como resultado N²-1
        if k==n+1 or k==n*n-1: 
            return print("IMPOSSIBLE")
        #Si el tamaño de la matriz es menor o igual que 3, es imposible realizar el cuadadrado latino
        #Solo es posible si el residuo de K entre N es 0, pero ese caso ya esta cubierto arriba
        if n<=3: 
            return print("IMPOSSIBLE")
        #Si se llega hasta aqui, quiere decir que es posible resolver el cuadrado latino
        #Pero como el residuo de K entre N no es 0, quiere decir que la diagonal sera formada por numeros diferentes
        #Se crea una lista para calcular los numeros de la digonal
        a=[0 for i in range(n)]
        #Se hace un ciclo de 0 hasta K
        for i in range(k):
            #Para calcular los numeros de la digonal se suma 1 al indice i%n
            #ya que K tiene que ser mayor que N, se tiene que obtener N numeros que den como suma K
            #al sumar 1 al indice i%n, se asegura que no se saldra del tamaño de la lista
            #por ejemplo si N es 4 y K es 6, la diagonal es 2 2 1 1
            a[i%n]+=1
        #En la diagonal solo puede ir como maximo 2 valores distintos, de lo contrario se complicaria el cuadrado latino
        #Si hay 3 valores, hay que reajustar la diagonal, para verificar eso, se calcula el residuo de K entre N
        r=k%n
        #Se establece una bandera llamada Tres en verdadero
        tres=True
        #En las 2 primeras condiciones, como resultado de las operaciones se genera un 3 o no se puede generar uno
        #Por eso la bandera Tres no se pasa a Falso
        #Si el residuo es 1
        if r==1:
            #Al segundo elemento de la diagonal se le suma uno y al ultimo se le resta uno
            #Estos cambios son necesarios para revolver el resto del cuadrado latino
            a[1]+=1
            a[n-1]-=1
        #Si el residuo es igual a N-1
        elif r==n-1:
            #Al primer elemento de la diagonal se le suma uno, al penultimo se le resta uno y se invierte la diagonal
            #Estos cambios son necesarios para revolver el resto del cuadrado latino
            #Este cambio se puede observar mejor si se compara N=8 k=14 con N=8 k=15
            a[0]+=1
            a[n-2]-=1
            a.reverse()
        else:
            #Si no, se toma el metodo X Y, que se menciona en el video
            #Donde toda la diagonal se llena con elementos X a excepcion de los ultimos que son elementos Y
            #X es el primer elemento de la diagonal y Y el ultimo
            x=a[0]
            y=a[-1]
            for i in range(r):
                respuesta[i][(i+1)%r]=y
            for i in range(n-r):
                respuesta[r+i][r+(i+1)%(n-r)]=x
            #Como no se sumo uno a ninguno elemento, la bandera Tres se cambia a falso
            tres=False
        #Si la bandera Tres es verdadera
        if tres:
            #Como es verdadera, se toma el metodo X Y Z, que se menciona en el video
            #X es el primer elemento de la diagonal
            x=a[0]
            #Y es el tercer elemento de la diagonal
            y=a[2]
            #Z es el ultimo
            z=a[-1]
            #Se acomoda Y en la matriz de forma correcta, se acomoda de forma que no se repita en las filas
            respuesta[0][1]=respuesta[1][-1]=respuesta[-1][0]=y
            #Se llenan los ultimos elementos de la diagonal con Z
            for i in range(n-1):
                respuesta[(i+1)%(n-1)][i]=z
            #Se llenan los elementos restantes con X
            for i in range(n-2):
                respuesta[2+i][2+(i+1)%(n-2)]=x
        #Se agrega la diagonal a la matriz respuesta
        for i in range(n):
            respuesta[i][i]=a[i]
    #Con la diagonal resulta solo queda resolver el resto del cuadrado latino
    #La forma mas facil de resolverlo es como si se resolviera un sodoku
    #Como hay que resolver en forma de soduko, es necesario iniciar en 1
    #X se usara para saber que numero agregar 
    #Si X es 1, se agrega todos los 1 restantes a la matriz
    #Si X es 2, se agrega todos los 2 restantes a la matriz
    #Asi sucesivamente
    for x in range(1,n+1):
        #Se incializa un contador en 0
        cont=0
        #Se recorre la matriz de la respuesta
        for i in range(n):
            for j in range(n):
                #Si la matriz contiene un elemento igual a X se le suma 1 al contador
                if respuesta[i][j]==x:
                    cont+=1
        #Si el contador es mayor que 0
        if cont:
            #Si contador es igual a N, se pasa a la siguiente iteraccion de X
            #Por ejemplo N=5, X=1
            #Si hay cinco unos en la matriz quiere decir que todos los 1 posibles estan en posicion
            #por lo que no se tiene que hacer nada
            if cont==n:
                continue
        #Se inicia un grado de bitmartite de tamaño N*N
        g=bitpartite(n,n)
        #se recorre la matriz de respuesta
        for i in range(n):
            for j in range(n):
                #Si aun hay 0 en la matriz, se agregan los indices en el grafo como posibles 
                #posiciones para los valores
                if respuesta[i][j]==0:
                    g.agregar(i,j)
        #Se llama el metodo solucion del grafo
        g.solucion()
        #La solucion contiene los indices correctos para la posicion del valor actual de X
        #Para entender mejor como se obtiene las posiciones, recomiendo ver el video de la solucion
        #https://www.youtube.com/watch?v=VayKvCg4vvQ
        for i in range(n):
            #Se agrega el valor de X en la posicion correcta
            #la matriz p del grafo contiene los indices donde debe de ir x
            respuesta[i][g.p[i]]=x
    #Se muestra POSSIBLE
    print("POSSIBLE")
    #Se muestra fila por fila la respuesta
    for i in range(n):
        #en Python usar * en una lista la "descomprime", en otras palabras, muestra sus elementos separados por un espacio
        print(*respuesta[i])
    return 0

#Se lee T (Cantidad de casos de prueba)
t=iinp()
for i in range(t):
    #Se lee N (Tamaño de la matriz) y K (El resultado deseado del trazo)
    n,k=ent()
    #Se imprime en el formato deseado
    print("Case #%i:"%(i+1),end=" ")
    #Se llama a la funcion resolver con los parametros N y K
    resolver(n,k)