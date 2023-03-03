def mifuncion():
    print("Mi primera funcion ")
#mifuncion()
def imprimir(nombre,apellido):#llamamos a la funcion
    print("Mi nombre es: ",nombre,apellido)
# imprimir('junior','alexa') #se tiene que pasar todos los parametros si hay varios argumentos
def imprimir(*nombre):#el asterisco sirve para poner mas argumentos
    print("Mi nombre es: ",nombre)
#imprimir('junior','alexa','puta') 

def nombrecompleto(nombre,apellido):
    print(nombre,apellido)
#nombrecompleto(nombre='edy',apellido='alexa')

def nombrecompleto2(**kwargs):#agrupar la funcion como si fuera un diccionario 
    print(kwargs['nombre'],kwargs['apellido'])
#nombrecompleto2(nombre='edy',apellido='alexa')
def mifuncion2(argumento='edy'):
    print(argumento)
#mifuncion2('batman')  
#mifuncion2()
def mifuncionlista(lista):
    for el in lista:
        print(el)
#mifuncionlista(['edy','feliz']) #imprime en en vertical

def concatenanombres(lista):
    i=' '
    for el in lista:
        i=i +' ' + el
    return i
nombres= concatenanombres(['edy','alexa'])
print(nombres)
