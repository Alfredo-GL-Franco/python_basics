print("Ejercicio practico")
print("=====================================")
print()
cadena= input("Escriba la cadena texto que desea invertir:")
print()

print(f"El texto original es: {cadena}")
i=0
print("El texto invertido es: ", end="")
for character in cadena:
    largo=len(cadena)
    print(cadena[-1-i:largo-i], end="")
    i+=1

print()
print("\n=====================================")
print("Otra forma de resolverlo")
print("=====================================")
print()
print("El texto invertido es: ", end="")
string_reversed = ""
for character in cadena:
    string_reversed = character + string_reversed
print(string_reversed)

print("\nFin del programa")