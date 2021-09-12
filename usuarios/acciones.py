#import usuarios.usuario as modelo
from usuarios import usuario as modelo
from os import system

import notas.acciones

class Acciones:

    def registro(self):
        print("Oka, vamos a registrarte en el sistema...")

        print("\nCompleta los siguientes datos:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")
        password = input("Pasword: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            system("cls")
            print(f"Bienvenido {registro[1].nombre}, te has registrado correctamente.")
        else:
            system("cls")
            print("No te has registrado correctamente.")


    def login(self):
        print("Okas, identificate en el sistema...")

        try:
            print("\nCompleta los siguientes datos:")
            email = input("Email: ")
            password = input("Password: ")

            usuario = modelo.Usuario('','', email, password)

            login = usuario.identificar()

            if email == login[3]:
                system("cls")
                print(f"Bienvenido {login[1]}")
                self.proximasAcciones(login)
        
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Error en el login")

    
    def proximasAcciones(self, usuario):
        
        print("""
        Acciones disponibles:
        -Crear nota (crear)
        -Mostrar tus notas (mostrar)
        -Eliminar nota (eliminar)
        -Salir (salir)
        """)

        accion = input("Elija una opción: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            system("cls")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            system("cls")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            #system("cls")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            system("cls")
            print("Saliendo....")
            exit()
        