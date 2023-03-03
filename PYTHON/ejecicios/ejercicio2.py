#primero=int(input("Ingrese el primer numero :")) #por default sin el int es un tipo string y no va leer 
#segundo=int(input("Ingrese el segundo numero :"))
#print(primero+segundo)

primero=input("Ingrese el primer numero :")
try: primero=int(primero)
except: 
    primero='hola'
segundo=input("Ingrese el segundo numero :")
try: 
    segundo=int(segundo)
except: segundo='que tal'
if primero=='hola' or segundo=='que tal' :
    print("Ingresaste mal, prueba con numeros")
else :
    print(primero+segundo)
 