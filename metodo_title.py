print("====================================")
print("Ejemplo metodo title")
print("====================================")

first=input("Escribe tu nombre: ")
las=input("Escribe tu apellido:")
print()
full= f"{first} {las}"
print(f"Se escribio correctamente: {full.istitle()}")
print()
if full.istitle()== False:
    print("Error, la primera letra de cada palabra debe ser mayuscula")
    print(full.title())
    print("Nombre corregido...")

