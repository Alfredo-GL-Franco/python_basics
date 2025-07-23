print("Operadores logicos")
print("===================\n")

num_uno= int(input("Escriba un numero entre 3 y 7: "))
if num_uno >= 3 and num_uno<= 7:
    print("La condicion se cumple\n")
else:
    print("La condion no se cumplio\n")

num_dos =int(input("Esciba un numero o menor de 10 o mayo que 100:  "))    
if num_dos <=10 or num_dos>=100:
    print("La condicon se cumple \n")

else:
    print("La condicion no se cumple")    
    
numr_tres= int(input("Escribe un numero que no sea par: "))
numr_tres=numr_tres % 2 
if not numr_tres==0:
    print("La condicion se cumple\n")

else:
    print("La condicion no se cumple\n")    

print("FIN.")    