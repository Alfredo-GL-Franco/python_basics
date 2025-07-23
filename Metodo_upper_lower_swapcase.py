print("Metodo Upper Lower")
print("=================================")

firs_naem=input("Escriba su nombre: ")
last_name= input("Escriba sus apellidos:")
print()
res_est=input("Es usted estudiante? ")
print(f"La respuesta esta en el formato correcto: {res_est.islower()}")
print("Corrigiendo respuesta...")
print()
if res_est.lower()== "si":
    matricula= input("Escriba su matricula:")
    print(f"La respuesta esta en el formato correcto: {matricula.isupper()}")
    print("Corrigiendo respuesta...")
    print()

    if matricula.upper() == "A":
        ful_name=f"{firs_naem.title()} {last_name.title()}"
        print(f"Hola {ful_name}, es un gusto saludarte su matricula es: {matricula.upper()}")
        
    elif matricula.upper() == "B":
        ful_name=f"{firs_naem.upper()} {last_name.upper()}"
        print(f"Hola {ful_name}, es un gusto saludarte su matricula es: {matricula.upper()}")

    else :    
        print("Matricula no encontrada.")

elif res_est.lower()== "no":
    print("Lo sentimos, no podemos continuar con el proceso.")


print()   
texto= input("Escribe un texto con mayusculas y minusculas para invertirlo:")
print(f"El texto original es: {texto}")
print(f"El texto invertido es: {texto.swapcase()  } \n solo se muestra pero no se guarda el cambio")
print("====================================")


print()
print("=====================================")
t2="El vIAje A la PlAya es MUy GraTIFicanTe ParA mI"
print(t2)
print("Texto aplicanco capitalize: ")
print(t2.capitalize())
print("Texto aplicanco title: ")
print(t2.title())
print("Texto aplicanco swapcase: ")
print(t2.swapcase())
print("Texto aplicanco upper: ")
print(t2.upper())
print("Texto aplicanco lower: ")
print(t2.lower())
