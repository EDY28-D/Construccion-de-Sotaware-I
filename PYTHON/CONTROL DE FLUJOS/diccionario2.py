#agregar valores dentro del diccionario
diccionario={
"Base de datos": "SQL",
"Herrameinta":"ORACLE",
"NOTA": 20
}
print(diccionario)
print(diccionario.get("Base de datos"))  #acceder a un solo valor 
diccionario["Base de datos"]='Curso'#cambiar un diccionario por otro
print((diccionario))#imprimir
diccionario["MySQL"]='si'
print(diccionario)
diccionario.pop('MySQL')#eliminar el diccionario en este caso MySQL
print(diccionario)
diccionario["INTELIGENTE"]='EDY'
print(diccionario)
diccionario.popitem() #eliminar el ultimo elemento agreegado al diccionario
print(diccionario)
diccionario["Materia"]='Pensamiento'
print(diccionario)
xd=diccionario.copy() #copiando todo el diccionario original a xd
del diccionario['Materia'] #eliminando solo Materia
print (diccionario,xd)#imprimiendo el diccionario original mas la copia xd