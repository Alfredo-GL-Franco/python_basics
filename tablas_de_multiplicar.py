print("Practica tablas de multiplicar")
print("***********************************")

num= int(input("Escriba el numero de la tabla de multiplicar: "))

print("\n La tabla del ",num, " es: \n")
for i in range(11):

    print(f"{num} x {i} = ", num * int(i))

print("\n Fin del programa")    