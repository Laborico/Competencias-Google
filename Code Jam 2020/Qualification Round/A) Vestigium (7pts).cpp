/*
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
*/

#include <bits/stdc++.h>
using namespace std;

void resolver()
{
    //Se declara la varibale para N (El tamaño de la matriz), K (La suma de la diagonal), R (el contador de las filas) y C (el contador de las columnas)
    int n,k=0,r=0,c=0;
    //Se lee N (El tamaño de la matriz)
    cin>>n;
    //Se crea una matriz de tamaño N * N
    int mat[n][n];
    //Al ser una matriz bidimensional es necesario tener 2 ciclos
    //El primero recorre las filas y el segundo el valor de cada fila
    for(int i=0;i<n;i++)
    {
        //Se crea un set con el nombre fila
        //Un set es una lista cuyos valores son unicos 
        set<int> fila;
        //Se recorre cada valor de la fila
        for(int j=0;j<n;j++)
        {
            //Se guarda el valor ingresado en su lugar correspondiente
            cin>>mat[i][j];
            //Se agrega ese valor al set de la fila
            //Si el valor ya existe en el set, no se agrega nada
            fila.insert(mat[i][j]);
            //Si i==j, quiere decir que es el valor de la diagonal
            //Se le suma el valor a la variable K
            if(i==j) k+=mat[i][j];
        }
        //Si el tamaño de la fila es menor que N, quiere decir que habia elementos repetidos y se le suma 1 a la variable R
        if(fila.size()<n) r++;
    }
    //Se recorre de una forma diferente la matriz
    //En lugar de usar I para las filas y J para el valor de cada elemento
    //Se utiliza J para las columnas e I para el valor de cada elemento
    for(int i=0;i<n;i++)
    {
        //Se crea un set llamado columna
        set<int>columna;
        //Se agrega cada valor de la columna a la variable
        for(int j=0;j<n;j++) columna.insert(mat[j][i]);
        //Si el tamaño de la columna es menor que N, significa que habia un elemento repetido en la columna y se le suma 1 a la variable c
        if(columna.size()<n) c++;
    }
    //Se muestra las variables K,R y C en el formato deseado
    cout<<k<<" "<<r<<" "<<c<<endl;
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