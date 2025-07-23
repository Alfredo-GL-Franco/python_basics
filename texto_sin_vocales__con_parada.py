print("Practica texto sin vocales")
print("+++++++++++++++++++++++++++++++++")
print()
cadena=input("Escribe la cadena de texto: ")
caracter=input("Escribe el caracter de parada: ")

for i in cadena:

    if i.lower() == caracter.lower():
        print("\nSe interrumpio el pograma correctamente: ")
        break
    
    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
        print("*",end="")
        continue
    print(f"{i}",end="")
