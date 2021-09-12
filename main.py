"""
PROYECTO PYTHON Y MYSQL

. Abrir asistente
. Login o registro
    . Si elegimos registro, crear usuario en base de datos
    . Si elegimos login, identificar al usuario

. Opciones al usuario:
    . Crear nota
    . Mostrar notas
    . Borrar nota
"""
from os import system
from usuarios import acciones


system("cls")

print("""
Acciones disponibles:
    -Registro
    -Login
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")

system("cls")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()

#system("cls")