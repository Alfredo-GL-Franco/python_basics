##############conversor
############

print("=============================")
print("Conversor de numero a palabras")
print("==============================")

print("Menu de oopciones:\n")
print("========================\n")
print("Presiona 1 para convertir un numero a palabra\n")
print("Presiona 1 para convertir una palabra a numero\n")
 
print("========================\n")
opcion= int(input("Cual es la opcion deseada?\n"))


if opcion == 1:
 
 print("\n Escogio convertir a palabras")
 opcion_1= int(input("Cual es el numero que quieres convertir?\n"))
 if opcion_1 ==1:
  print("\n El numero es: 'uno'")  
 elif opcion_1 == 2:
  print("\n El numero es: 'dos'") 
 elif opcion_1 == 3:
  print("\n El numero es: 'tres'") 
 elif opcion_1 == 4:
  print("\n El numero es: 'cuatro'") 
 elif opcion_1 == 5:
  print("\n El numero es: 'cinco'") 
 elif opcion_1 == 6:
  print("\n El numero es: 'seis'") 
 elif opcion_1 == 7:
  print("\n El numero es: 'siete'") 
 elif opcion_1 == 8:
  print("\n El numero es: 'ocho'") 
 elif opcion_1 == 9:
  print("\n El numero es: 'nueve'") 
 elif opcion_1 == 10:
  print("\n El numero es: 'diez'") 
 else:
  print("\n El numero no esta registrado")   



elif opcion == 2:
 opcion_1 = input("\n Cual es la palabra que quieres convertir\n")
 opcion_1=opcion_1.lower()
 if opcion_1 == "uno":
  print("\n El numero es: '1'")
 elif  opcion_1 == "dos":
  print("\n El numero es: '2'")
 elif  opcion_1 == "tres":
  print("\n El numero es: '3'")
 elif  opcion_1 == "cuatro":
  print("\n El numero es: '4'")
 elif  opcion_1 == "cinco":
  print("\n El numero es: '5'")
 elif  opcion_1 == "seis":
  print("\n El numero es: '6'")
 elif  opcion_1 == "siete":
  print("\n El numero es: '7'")
 elif  opcion_1 == "ocho":
  print("\n El numero es: '8'")
 elif  opcion_1 == "nueve":
  print("\n El numero es: '9'")
 elif  opcion_1 == "diez":
  print("\n El numero es: '10'")
 else:
  print("\n El numero no esta registrado")

 
else: 
 print("\n Opcion no disponible")
 


