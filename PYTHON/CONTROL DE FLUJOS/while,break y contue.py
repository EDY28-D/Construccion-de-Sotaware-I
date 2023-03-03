
op2=int

while op2 !=0:
    num1=int(input ("Ingrese un numero: "))
    num2=int(input ("Ingrese otro numero: "))
    print("Ingrese una de las opciones: ")
    print("A)suma")
    print("B)resta")
    opcion=input()
    if opcion=='A':
        print(num1+num2)
    elif opcion=='B':
        print(num1-num2)
    op2=int(input("Desea continuar? Ingrese 1 para si o 0 para no : "))
    
    





