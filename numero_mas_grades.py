print("=======================================\n")
print("Buscador del numero mas grande\n")
print("=======================================\n")

a= int(input("Escriba el primer numero: "))
b= int(input("Escriba el segundo numero: "))
c= int(input("Escriba el tercer numero: "))

if a!= b :
    if b != c:
        if c!=a:
            if a>b and a>c:
                print("El numero mas grande es: ",a)
            elif b>a and b>c:
                print("El numero mas grande es: ",b)

            elif c>a and c>b:
                print("El numero mas grande es: ",c)
                
        else:
         print("Hay al menos dos numero repetidos ",a," y ",c)
     
    else:
     print("Hay al menos dos numero repetidos ",b," y ",c)       

else:
    print("Hay al menos dos numero repetidos ",a," y ",b)