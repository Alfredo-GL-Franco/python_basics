print("======================================\n")
print("Clasificador de numero impar o par\n")
print("======================================\n")

num= int(input("Escriba el numero que quiera clasificar: "))
mod=num%2
if mod==0:
    print("El numero '",num,"' es par")              
else:
    print("El numero '",num, "' es impar")    