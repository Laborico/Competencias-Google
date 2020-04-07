/*
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
*/
//Para la solución de este problema es necesario conocer Bitpartite Marching y el teorema de Hall
//Sugiero altamente ver el vídeo de la explicación para entender por completo la solución, en ingles
//https://www.youtube.com/watch?v=VayKvCg4vvQ


//La forma sencilla de resolver el problema es encontrando la diagonal con la suma
//Y llenando el resto de la matriz como si fuera un sodoku
//De esta forma se obtiene un cuadradro latino

#include <bits/stdc++.h>
#include <vector>
using namespace std;


//Esta parte del codigo es algo dificil de explicar, te recomiendo ver el video de la solucion para que 
//entiendas mejor el tema de Bitpartite

//El Bitpartite se utiliza para resolver el resto de la matriz como sodoku

//Se crea la estructura Bitpartite, que necesita 2 variables, N y M
//Estas para crear la matriz
struct bipartite {
    //Se crea el vector pre, donde se almacenan los valores de los indices antes de ser cambiados
    //Se crea el vector raiz, donde se guardan los indices de posibles respuestas
    vector<int> pre, raiz;
    //Se crea el vector de vectores hacia,en esta se guardan los indices disponibles para llenar la matriz respuesta
    vector<vector<int>> hacia;
    //Se crea el vector p, donde se almacena la posicion final del valor
    //Se crea el vector q, donde se agregan los indices relacionados a p
    vector<int> p, q;
    //Se crea N y M, el tamaño de la matriz respuesta
    int n, m;
    //Se inicializan todos los valores
    //Pre se inicializa como un vector de tamaño N lleno de -1
    //Raiz se inicializa como un vector de tamaño N lleno de -1
    //Hacia se inicializa como un vector de tamaño N lleno de vectores vacios
    //P se inicializa como un vector de tamaño N lleno de -1
    //Q se inicializa como un vector de tamaño N lleno de -1
    bipartite(int n, int m):pre(n,-1),raiz(n,-1),hacia(n),p(n,-1),q(m,-1),n(n),m(m){}
    //Funcion agregar, en ella se agregan los indices disponibles de la matriz respuesta
    //necesita dos valores enteros a y b
    void agregar(int a, int b) { hacia[a].push_back(b);}
    //Funcion solucion, obtiene las posiciones en la matriz de un valor
    int solucion() 
    {
        //se crea una bandera para saber si hay una actualizacion a los valores de las posiciones
        bool act = true;
        //un ciclo activado siempre que exista una actualizacion
        while (act) 
        {
            //se cambia la bandera a falso
            act = false;
            //se crea una queue(cola) llamada S, almacena las posiciones posibles de un valor
            queue<int> s;
            //Un ciclo hasta n
            for(int i=0;i<n;i++)
            {
                //El operador ~ invierte los bits de un valor
                //Esto lo que haces es que convierte el -1 en 0
                //y despues niega el 0, conviertiendo en True
                //es una forma eficiente de saber si un valor funciona o no
                if (!~p[i]) 
                {
                    //Si pasa la condicion se guarda el valor en el vector raiz
                    raiz[i] = i;
                    //se agrega el indice a la queue S
                    s.push(i);
                }
            }
            //Un ciclo que se repetira siempre y cuando la queue S no este vacia
            while (s.size()) 
            {
                //Se guarda el primer elemento de la queue S en una variable V
                int v = s.front(); 
                //Se remueve el primer elemento de la queue
                s.pop();
                //Si en el vector p existe un valor que este en el indice del vector raiz cuyo indice es V se continua con el siguiente valor del ciclo while
                //Hay que recordar que la matriz raiz guarda los indices de las posibles soluciones
                if (~p[raiz[v]]) continue;
                //Si no, se recore el vector hacia, que contiene todas las posibles posiciones
                for(int i=0;i<hacia[v].size();i++) 
                {
                    //Se guarda en una variable u el valor de una posible posicion
                    int u = hacia[v][i];
                    //si en el vector q existe un valor que este en el indice del vector raiz cuyo indice es U
                    if (!~q[u]) 
                    {
                        //Un ciclo que se repetira siempre que el valor invertido de u no se negativo
                        while (~u) 
                        {
                            //Se guarda el valor V en el indice U del vector q
                            q[u] = v;
                            //Se intercambian los valores de p[v] y u
                            swap(p[v],u);
                            //Se le asigna el valor del indice V del vector pre a la variable V
                            v = pre[v];
                        }
                        //Como hubo actualizaciones en las matrices se enciende la bandera
                        act = true;
                        //Se rompe el ciclo for
                        break;
                    }
                    //Se guarda el valor del indice U del vector q en la variable u
                    u = q[u];
                    //Si el indice U de la matriz pre no es -1, se continua con la siguiente iteraccion del ciclo for
                    if (~pre[u]) continue;
                    //de lo contrario se le asigna el valor de V
                    pre[u] = v; 
                    //el valor del indice u se cambia por el del indice v del vector raiz
                    raiz[u] = raiz[v];
                    //se agrega el valor de U a la lista S
                    s.push(u);
                }
            }
            //Si la bandera esta en True hay que reiniciar las matrices pre y raiz
            //la funcion fill llena una estructura de datos, o parte de ella, con el valor deseado
            if (act) fill(pre.begin(),pre.end(),-1), fill(raiz.begin(),raiz.end(),-1);
        }
        return 0;
    }
};


//Resolver, muestra el resultado del problema
void resolver()
{
    //Se declara N (el tamaño de la matriz) y K (el valor deseado de la suma del trazo)
    int n,k;
    cin>>n>>k;
    //Si el trazo deseado es menor que el tamaño de la matriz o mayor que el tamaño al cuadrado de la matriz 
    //es imposible resolver la matriz, por ejemplo si el tamaño de la matriz es 4 y el numero del trazo deseado es 3
    //es imposible de resolver, por que no hay 4 numeros positivos cuya suma de 3
    //y si el tamaño de la matriz es 4 el numero del trazo deseado es 17, es imposible de resolver
    //si hay 4 numeros positivos cuya suma es 17, pero no son iguales o consecutivos, requisitos para crear el cuadrado latino
    if (k < n || k > n*n)
    {
        cout<<"IMPOSSIBLE"<<endl; 
        return;
    }
    //Se crea una matriz de N*N, en la cual se almacenara el resultado
    vector<vector<int>> res(n,vector<int>(n));
    //Si el residuo de K entre N es 0, quiere decir que la diagonal de la matriz puede ser llenada inmediatamente
    //por ejemplo si el tamaño de la matriz es 3 y el tamaño del trazo deseado es 6, la diagonal de la matriz
    //puede ser llenada con 2
    if (k%n == 0) 
    {
        //Se llena la diagonal con el resultado de la division de k entre n
      for(int i=0;i<n;i++) res[i][i] = k/n;
    } 
    else 
    {
        //Si el trazo deseado es mayor que el tamaño de la matriz por uno o igual al tamaño al cuadrado menos 1
        //Es imposible realizar un cuadrado latino, por que no hay N numeros iguales o consecutivos que den como resultado N+1
        //Al igual que no hay N numeros consecutivos o iguales que sumados den como resultado N²-1
        if (k == n+1 || k == n*n-1) 
        {
            cout<<"IMPOSSIBLE"<<endl; 
            return;
        }
        //Si el tamaño de la matriz es menor o igual que 3, es imposible realizar el cuadadrado latino
        //Solo es posible si el residuo de K entre N es 0, pero ese caso ya esta cubierto arriba
        if (n <= 3) 
        {
            cout<<"IMPOSSIBLE"<<endl; 
            return;
        }
        //Si se llega hasta aqui, quiere decir que es posible resolver el cuadrado latino
        //Pero como el residuo de K entre N no es 0, quiere decir que la diagonal sera formada por numeros diferentes
        //Se crea un vector para calcular los numeros de la digonal
        vector<int> a(n);
        //Se hace un ciclo de 0 hasta K
        //Para calcular los numeros de la digonal se suma 1 al indice i%n
        //ya que K tiene que ser mayor que N, se tiene que obtener N numeros que den como suma K
        //al sumar 1 al indice i%n, se asegura que no se saldra del tamaño de la lista
        //por ejemplo si N es 4 y K es 6, la diagonal es 2 2 1 1
        for(int i=0;i<k;i++) a[i%n]++;
        //En la diagonal solo puede ir como maximo 2 valores distintos, de lo contrario se complicaria el cuadrado latino
        //Si hay 3 valores, hay que reajustar la diagonal, para verificar eso, se calcula el residuo de K entre N
        int r = k%n;
        //Se establece una bandera llamada Tres en verdadero
        bool tres = true;
        //En las 2 primeras condiciones, como resultado de las operaciones se genera un tercer valor o no se puede generar uno
        //Por eso la bandera Tres no se pasa a Falso
        //Si el residuo es 1
        if (r == 1) 
        {
            //Al segundo elemento de la diagonal se le suma uno y al ultimo se le resta uno
            a[1]++; 
            a[n-1]--;
        } 
        //Si el residuo es igual a N-1
        else if (r == n-1) 
        {
            //Al primer elemento de la diagonal se le suma uno, al penultimo se le resta uno y se invierte la diagonal
            //Estos cambios son necesarios para revolver el resto del cuadrado latino
            //Este cambio se puede observar mejor si se compara N=8 k=14 con N=8 k=15
            a[0]++; 
            a[n-2]--;
            reverse(a.begin(),a.end());
        } 
        else 
        {
            //Si no, se toma el metodo X Y, que se menciona en el video
            //Donde toda la diagonal se llena con elementos X a excepcion de los ultimos que son elementos Y
            //X es el primer elemento de la diagonal y Y el ultimo
            int x = a[0], y = a.back();
            for(int i=0;i<r;i++) res[i][(i+1)%r] = y;
            for(int i=0;i<(n-r);i++) res[r+i][r+(i+1)%(n-r)] = x;
            //Como no se sumo uno a ninguno elemento, la bandera Tres se cambia a falso
            tres = false;
        }
        //Si la bandera Tres es verdadera
        if (tres) 
        {
            //Como es verdadera, se toma el metodo X Y Z, que se menciona en el video
            //X es el primer elemento de la diagonal
            //Y es el tercer elemento de la diagonal
            //Z es el ultimo
            int x = a[0], y = a[2], z = a.back();
            //Se acomoda Y en la matriz de forma correcta, se acomoda de forma que no se repita en las filas
            res[0][1] = res[1].back() = res.back()[0] = y;
            //Se llenan los ultimos elementos de la diagonal con Z
            for(int i=0;i<(n-1);i++) res[(i+1)%(n-1)][i] = z;
            //Se llenan los elementos restantes con X
            for(int i=0;i<(n-2);i++) res[2+i][2+(i+1)%(n-2)] = x;
        }
        //Se agrega la diagonal a la matriz respuesta
        for(int i=0;i<n;i++) res[i][i] = a[i];
    }
    //#Con la diagonal resulta solo queda resolver el resto del cuadrado latino
    //La forma mas facil de resolverlo es como si se resolviera un sodoku
    //Como hay que resolver en forma de soduko, es necesario iniciar en 1
    //X se usara para saber que numero agregar 
    //Si X es 1, se agrega todos los 1 restantes a la matriz
    //Si X es 2, se agrega todos los 2 restantes a la matriz
    //Asi sucesivamente
    for(int x=1;x<=n;x++)
    {
        //Se incializa un contador en 0
        int cnt = 0;
        //Se recorre la matriz de la respuesta
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                //Si la matriz contiene un elemento igual a X se le suma 1 al contador
                if (res[i][j] == x) ++cnt;
            } 
        }
        //Si el contador es mayor que 0
        if (cnt) 
        {
            //Si contador es igual a N, se pasa a la siguiente iteraccion de X
            //Por ejemplo N=5, X=1
            //Si hay cinco unos en la matriz quiere decir que todos los 1 posibles estan en posicion
            //por lo que no se tiene que hacer nada
            //de lo contrario la funcion assert se encarga de romper el if
            assert(cnt == n);
            continue;
        }
        //Se inicia un grado de bitmartite de tamaño N*N
        bipartite g(n,n);
        //se recorre la matriz de respuesta
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                //Si aun hay 0 en la matriz, se agregan los indices en el grafo como posibles 
                //posiciones para los valores
                if (res[i][j] == 0) g.agregar(i,j);
            } 
        }
        //Se llama el metodo solucion del grafo
        g.solucion();
        //La solucion contiene los indices correctos para la posicion del valor actual de X
        //Para entender mejor como se obtiene las posiciones, recomiendo ver el video de la solucion
        //https://www.youtube.com/watch?v=VayKvCg4vvQ
        for(int i=0;i<n;i++)
        {

            //Se agrega el valor de X en la posicion correcta
            //el grafo p del grafo contiene los indices donde debe de ir x
            res[i][g.p[i]] = x;
        }
    }
    //Se muestra POSSIBLE
    cout<<"POSSIBLE"<<endl;
    //Se muestra la respuesta
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<res[i][j];
            if(j<n-1) cout<<" ";
        }
        cout<<endl;
    }
}


int main() 
{
    //Sincroniza las entradas con las salidas, como efecto secundario reduce el tiempo de ejecucion
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    //Se declara T (la cantidad de casos de prueba) y C (el contador de casos de prueba)
    int t,c=1;
    //Se lee T
    cin>>t;
    //Mientras que el contador sea menor o igual que T
    while(c<=t) 
    {
        //Se muestra Case# El contador : 
        cout<<"Case #"<<c<<": ";
        //Se llama a la funcion resolver
        resolver();
        //Se le suma 1 al contador
        c++;
    }
    return 0;
}