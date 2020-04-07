/*
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
*/

#include <bits/stdc++.h>
using namespace std;

void resolver()
{
    //Se crea una variable para la respuesta
    string res="";
    //Se declara la N (la cantidad de actividades), S (la hora de inicio de una actividad) y E (la hora final de un actividad)
    int n,s,e;
    //Se crea un vector de vectores para alamacenar la lista de actividades
    vector<vector<int>> lista;
    //Se lee n
    cin>>n;
    //Se inicializa una bandera en verdadero
    //Esta se usara para saber si es posible cumplir con el itinerario de actividades o no
    bool ban=true;
    //Ciclo donde se leen todas las actividades
    for(int i=0;i<n;i++)
    {
        //Se crea un vector temporal
        vector<int> v;
        //Se lee S y E
        cin>>s>>e;
        //Se agregan S y E al vector temporal
        v.push_back(s);
        v.push_back(e);
        //Se agrega el vector con las horas a la lista de actividades
        lista.push_back(v);
    }
    //Se copia el vector lista
    vector<vector<int>> copia(lista);
    //Se ordena la copia de la lista de menor a mayor
    //La funcion sort viene incluida en la libreria <bits/stdc++.h>
    //Como parametros necesita el inicio y el fin de lo que se va a sortear
    sort(copia.begin(),copia.end());
    //Se crea un vector para Cameron y otro para Jamie
    vector<vector<int>> C;
    vector<vector<int>> J;
    //Por cada actividad
    for(int i=0;i<n;i++)
    {
        //Si la lista C esta vacia, se agrega la actividad
        if(C.size()==0) C.push_back(copia[i]);
        else
        {
            //Se inica una bandera bc en false, se usara para saber si Cameron puede realizar la actividad o no
            bool bc=false;
            //Por cada actividad de Cameron
            for(int j=0;j<C.size();j++)
            {
                //Si la actividad actual inicia y termina igual que alguna actividad de Cameron
                //Se cambia a True la bandera y se rompe el ciclo
                if(copia[i]==C[j])
                {
                    bc=true;
                    break;
                }
                //Si la actividad actual inicia despues de haber terminado la actividad de Cameron
                //o si la actividad actual termina antes de que la actividad de Cameron inicie
                //significa que se puede hacer y se pasa a la siguiente iteracion
                else if(copia[i][0]>=C[j][1] || copia[i][1]<=C[j][0]) continue;
                //Si no cumple ningun criterio se cambia la bandera a True y se rompe el ciclo
                //Por que Cameron no sera capaz de realizar la actividad
                else
                {
                    bc=true;
                    break;
                }
            }
            //Si la bandera es falsa, se agrega la actividad a la lista de Cameron
            //De lo contrario se realiza el mismo proceso para Jamie
            if(!bc) C.push_back(copia[i]);
            else
            {
                if(J.size()==0) J.push_back(copia[i]);
                else
                {
                    bool bj=false;
                    for(int j=0;j<J.size();j++)
                    {
                        if(copia[i]==J[j])
                        {
                            bj=true;
                            break;
                        }
                        else if(copia[i][0]>=J[j][1] || copia[i][1]<=J[j][0]) continue;
                        else
                        {
                            bj=true;
                            break;
                        }
                    }
                    if(!bj) J.push_back(copia[i]);
                    //Si Jamie tampoco puede hacer la actividad la bandera ban se pasa a falso
                    else ban=false;
                }
            }
        }
    }
    //Si la bandera se quedo en true, quiere decir que todas las actividades se pueden realizar bajo las condiciones del problema
    if(ban)
    {
        //El juez espera que el resultado este ordenado de acuerdo al orden que se ingresa las actividades
        //Por lo que hay que acomodar la respuesta en dicho orden
        //Por cada actividad
        for(int i=0;i<n;i++)
        {
            //Se crea una bandera para saber si el siguiente ciclo se rompera o no
            bool rompe=true;
            //Por cada actividad de Cameron
            for(int j=0;j<C.size();j++)
            {
                //Si la actividad de Cameron es igual a la de la lista de actividades sin ordenar
                if(lista[i]==C[j])
                {
                    //Se agrega C a la respuesta
                    res+="C";
                    //Se borra la actividad de la lista
                    C.erase(C.begin()+j);
                    //La bandera se pasa a false y se rompe el ciclo
                    rompe=false;
                    break;
                }
            }
            //Si el ciclo no se rompio quiere decir que Cameron no tenia la actividad
            //Se agrega J a la respuesta
            if(rompe) res+="J";
        }
        //Se muestra la respuesta y se sale de la funcion
        cout<<res<<endl;
        return;
    }
    //Si la bandera es falsa, se regresa IMPOSSIBLE
    else cout<<"IMPOSSIBLE"<<endl; return;
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