/*
Solucion en c++ por mi amigo Darkensses (https://github.com/Darkensses)


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
*/

#include <bits/stdc++.h>
using namespace std;

void resolver()
{
    //Se declara una variable pendientes en 0
    //Se usara para llevar el conteo de los parentesis pendientes de abrir o cerrar
    int pendientes=0;
    //Se declara la variable S (La cadena base) y la variable res donde se ira guardando la respuesta
    string s, res="";
    //Se lee S
    cin>>s;
    //Por cada digito de S
    for(int i=0;i<s.size();i++)
    {
        //Se le resta el caracter 0 al caracter actual de la cadena
        //Es una forma simple de obtener el valor numerico de un caracter sin la necesidad de castear a Int
        int n=s[i]-'0';
        //Mientras que los parentesis pendientes sean menores a N (la profundidad deseada)
        while(pendientes<n)
        {
            //A respuesta se le agrega un parentesis de apertura
            res+='(';
            //Se le suma 1 a pendientes, por que ahora hay un parentesis mas que cerrar
            pendientes++;
        }
        //Si pendientes es mayor a la profundidad N, se cierran parentesis
        while(pendientes>n)
        {
            //Se agrega un parentesis de cierre a la respuesta
            res+=')';
            //Se le resta uno a lso pendientes
            pendientes--;
        }
        //Se le agrega el caracter a la respuesta
        res+=s[i];
    }
    //Si aun quedan parentesis pendientes de cerrar se agregan
    for(int i=0;i<pendientes;i++)
    {
        res+=')';
    }
    //Se muestra la respuesta
    cout<<res<<endl;
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