i=0
print("Ejercicio practico: Eliminar una palabra de una cadena")
print("=====================================")
print()
cadena= input("Escriba la cadena de texto: ")
palabra=input("Ingrese la palabra que desea eliminar:")

print()
print(f"Texto toriginal: {cadena} ")
print(f"Palabra a eliminar: {palabra}")
print()
print(f"Cuantas veces aparece la palabra en el texo: {cadena.count(palabra)}")
print()
veces= cadena.count(palabra)


while cadena.startswith(palabra,i)== False:
    print("Buscando la palabra en la posicion:",i)
    i+=1

print()  
cant= len(palabra)
inicio=cadena[:i]
fin=cadena[i+cant:]

print(f"La cadena sin la palabra es: {inicio}{fin}")

print("\n===========================")
print("Ejemplo con find")
print("===========================")
indice=cadena.find(palabra)
if indice != -1:
    inicio=cadena[:indice]
    fin=cadena[indice+len(palabra):]
    print(f"La cadena sin la palabra es: {inicio}{fin}")
 