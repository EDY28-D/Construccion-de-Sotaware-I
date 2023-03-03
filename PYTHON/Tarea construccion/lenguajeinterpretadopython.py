#Mayor de N numero en python:
lista=[]
cant= int(input("¿Cuantos numeros desea ingresar? "))
i=1
while i<=cant :
    n=int(input(f"{i} Ingrese un numero: "))
    lista.append(n)
    i+=1
    lista.sort()

print("\nLos numeros ordenado de menor a mayor son: ")
print(lista)     
print("Numero mayor: ",max(lista))
print("Numero menor: ",min(lista))
    