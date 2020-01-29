def exit_text():
    """ Impresiones de salida """
    print("")
    print("Adios :(")
    print("")


def ayuda_text():
    """
    Textos con los posibles comandos
    Realmente se aceptan mas comandos, pero indicamos los
    mas simples
    """
    print("Agregar [tarea] -> Añadira una nueva tarea")
    print("Eliminar [numero tarea] -> Elimina una tarea")
    print("Completar [numero tarea] -> Marca una tarea como completada")
    print("Salir -> Para abandonar el programa")
    print("")


def comando_no_existe(comando):
    print("No existe el comando: " + comando)
    ayuda_text()

def longitud_minima_comando_correcta(comando):
    # Para minimizar codigo, un if logico en una linea
    return True if len(comando.split(' ', 1)) > 1 else False