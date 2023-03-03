primero=int(input('Ingrese un numero : '))
segundo=int(input('Ingrese el segundo numero : '))
opcion=input('Ingre la operacion a realizar: ')
print("A)SUMA")
print("B)RESTA")
print("C)DIVISION")
print("D)MULTIPLICACION")
if simbolo=='A':
    print('suma: ',primero+segundo)
elif simbolo=='B':
    print('resta}: ',primero-segundo)
elif simbolo=='C':
    print('division: ',primero/segundo)
elif simbolo=='D':
    print('Multiplication: ',primero*segundo)
else:
    print("La operacion ingresada no es valida")
