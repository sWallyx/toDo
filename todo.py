# Listado de imports
from todo_data import todo_data
import os
from functions import(
    exit_text,
    ayuda_text,
    comando_no_existe,
    longitud_minima_comando_correcta,
)
from constantes import (
    AYUDA_LISTADO,
    AGREGAR_LISTADO,
    COMPLETAR_LISTADO,
    SALIR_LISTADO
)

# Evitamos el error de devolucion de valor, que da alguna vez
# en python con '_' indicamos las variables que no se deberian
# de modificar
_ = os.system("clear")

todo = todo_data()
todo.print_data()

i = 0
cont = True

while cont:
    print("¿Que quieres hacer?")
    print("Si necesitas ayuda escribe ayuda.")
    comando_usuario = str(input("? "))

    # Para la decision usamos la primera palabra solamente
    decision = comando_usuario.split(' ')[0]

    # Dependiendo de la decision hacemos diferentes cosas
    if decision in AYUDA_LISTADO:
        ayuda_text()

    elif decision in SALIR_LISTADO:
        cont = False

    elif decision in AGREGAR_LISTADO:
        # ----------- FIX -----------
        # FIX si solo se agrega la palabra comando y nada mas el programa rompe
        if longitud_minima_comando_correcta(comando_usuario):
            todo.agregar_tarea(comando_usuario.split(' ', 1)[1])
            _ = os.system("clear")
            todo.print_data()
        else:
            print("Comando agregar mal escrito")
            ayuda_text()

    elif decision in COMPLETAR_LISTADO:
        # ----------- FIX -----------
        # De momento comprobamos que haya mas de una palabra,
        # pensar en algo mejor
        if longitud_minima_comando_correcta(comando_usuario):
            comando_sin_decision = comando_usuario.split(' ', 1)[1]

            # ----------- FIX -----------
            # Tiene que haber otra forma de hacerlo, controlar que solo se coge
            # un numero
            indice = int(comando_sin_decision.split(' ')[0])

            if isinstance(indice, int):
                todo.completar_tarea(indice - 1)

                _ = os.system("clear")
                todo.print_data()
                print("Tarea completada")

        else:
            print("Comando completar mal escrito")
            ayuda_text()

    else:
        comando_no_existe(decision)

todo.save_xml_file()
exit_text()
