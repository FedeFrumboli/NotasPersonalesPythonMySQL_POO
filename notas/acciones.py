import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}, vamos a crear una nota.")

        titulo = input("Titulo: ")
        descripcion = input("Contenido de nota: ")

        # USUARIO[0] ES EL ID DEL USUARIO, PARA CONECTAR LAS TABLAS
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"La nota '{nota.titulo}' se guardó correctamente")
        else:
            print("La nota no se guardó corractamente")
        
    def mostrar(self, usuario):
        print(f"Ok {usuario[1]}, éstas son tus notas:")

        nota = modelo.Nota(usuario[0])
        print("Objeto creado")

        notas = nota.listar()
        print("Notas guardadas")

        for nota in notas:
            print("\n__________________________________________________")
            print(f"{nota[2]}\n")
            print(nota[3])
            print("\n__________________________________________________")


    def borrar(self, usuario):
        print(f"Ok {usuario[1]}, vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a eliminar: ")

        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"La nota '{nota.titulo}' se eliminó correctamente")
        else:
            print("La nota no se ha eliminado")
        

