print("===========================")
print("Ejemplo de break")
print("===========================")
stop=int(input("Ingrese un número para detener el bucle: "))

cont=0
while cont<100:
    cont+=1
    if cont ==stop:
        print("El numero es:", cont, "por lo que se detiene el bucle")
        break
    print("valor actual es: ",cont)
print("============================")
print("imprimir solo los numero pares")

cont_1=0
while cont_1<100:
    cont_1+=1
    if (cont_1 % 2) !=0:
        continue
    print(cont_1, end=" ")


