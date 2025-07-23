print("=================================\n")
print("Consultor de vacaciones\n")
print("=================================\n")
print("Hola bienvenido\n")
nombre= input("Por favor escriba su nombre completo: ")
clave= int(input("Por favor escriba su clave: "))
time= int(input("Escriba su antiguedad en años: "))

if clave == 1:
    print("Cargando datos del sistema...\n")
    if time ==1:
        print(nombre," tu  clave es: ",clave," cuentas con 6 dias de vacaciones")
    elif time >=2 and time <=6 :
        print(nombre," Tu clave es: ",clave," cuentas con 14 dias de vacaciones")   
    elif time>7:
        print(nombre, " tu clave es: ",clave," cuentas con 20 dias de vacaciones")    
    else:
        print(nombre," tu clave es: ",clave, " lo sentimos actualmente no cuentas con vacaciones")    

elif clave == 2:
    print("Cargando datos del sistema...\n")
    if time ==1:
        print(nombre," tu  clave es: ",clave," cuentas con 7 dias de vacaciones")
    elif time >=2 and time <=6 :
        print(nombre," Tu clave es: ",clave," cuentas con 15 dias de vacaciones")   
    elif time>7:
        print(nombre, " tu clave es: ",clave," cuentas con 22 dias de vacaciones")    
    else:
        print(nombre," tu clave es: ",clave, " lo sentimos actualmente no cuentas con vacaciones")   

elif clave == 3:
    print("Cargando datos del sistema...\n")  
    if time ==1:
        print(nombre," tu  clave es: ",clave," cuentas con 10 dias de vacaciones")
    elif time >=2 and time <=6 :
        print(nombre," Tu clave es: ",clave," cuentas con 20 dias de vacaciones")   
    elif time>7:
        print(nombre, " tu clave es: ",clave," cuentas con 30 dias de vacaciones")    
    else:
        print(nombre," tu clave es: ",clave, " lo sentimos actualmente no cuentas con vacaciones")     

else:
    print("Clave no encontrada.")    
 