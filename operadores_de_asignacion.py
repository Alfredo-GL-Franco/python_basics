print("**************************************\n")
print("Operadores de asigancion \n")
print("**************************************\n")

name= input("Escriba su nombre por favor: ")
num=int(input("Escriba el numero inicial: "))
operacion=int(input("Escoga la operacion \n 1) suma \n 2) resta \n 3)division \n 4) multiplicacion\n operacion: "))
modificacion= int(input("Escriba con un numero como desea modificar el numero anterior: "))

mensaje ="Hola "
mensaje+=name

if operacion ==1:
    print("Se escogio la operacion suma: \n")
    num+=modificacion
    print(mensaje," el resultado es de la suma es: ",num)

elif operacion ==2:
    print("Se escogio la operacion resta: \n")
    num-=modificacion
    print(mensaje," el resultado es de la resta es: ",num)

elif operacion ==3:
    print("Se escogio la operacion division: \n")
    num/=modificacion
    print(mensaje," el resultado es de la division es: ",num)

elif operacion ==4:
    print("Se escogio la operacion multiplicacion: \n")
    num*=modificacion
    print(mensaje," el resultado es de la multiplicacion es: ",num)

else:
    print("Operacion no encontrada\n")    