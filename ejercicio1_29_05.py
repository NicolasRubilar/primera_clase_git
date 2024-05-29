import os
import time
usuarios=[]
while True:
    print("Menu")
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Eliminar usuario")
    print("4) Salir")

    opc=int(input("Ingrese Opcion: "))
    if opc==1:
        pass
    elif opc==2:
        print("REGISTRAR USUARIO")
        correo=input("Ingrese correo: ")
        contrasenia=input("Ingrese contraseña: ")

        usuario={
            "correo": correo,
              "contrasenia": contrasenia,}
        usuarios.append(usuario)
        print("Felicidades su usuario fue agregado!")
    elif opc==3:
        print("ELIMINAR USUARIO")
        existe=True
    elif opc==4:
        print("Hasta Luego!")
        break
    else:
        print("intente de nuevo")
        time.sleep(1)

