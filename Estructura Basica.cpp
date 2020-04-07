/*
Estructura basica para las competencias de Google

La mayoria de los problemas de Google tienen la misma presentacion para las respuestas 

Case #x: y

Con esta estructura solo te enfocarias en resolver el problema

*/

#include <bits/stdc++.h>
using namespace std;

void resolver()
{
    //Aqui va todo tu codigo
    //Haces cout a tu variable con tu respuesta
    cout<<" "<<endl;
}


int main() 
{
    //Sincroniza las entradas con las salidas, como efecto secundario reduce el tiempo de ejecucion
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    //Se lee T (la cantidad de casos de prueba)
    int t,c=1;
    cin>>t;
    while(c<=t) 
    {
        cout<<"Case #"<<c<<": ";
        resolver();
        c++;
    }
    return 0;
}