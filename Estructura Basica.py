""" 
Estructura basica para las competencias de Google

La mayoria de los problemas de Google tienen la misma presentacion para las respuestas 

Case #x: y

Con esta estructura solo te enfocarias en resolver el problema

"""

#Carga las funciones en memoria para acceder mas rapido a ellas
inp=input
iinp= lambda: int(inp())

def resolver():
    res=''
    #Aqui va todo tu codigo
    return res


#Se lee T (la cantidad de casos)
t=iinp()
for i in range(t):
    res=resolver()
    print("Case #%i: %s"%(i+1,res))