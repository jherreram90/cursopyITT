def funciones_cajero(funcion, *args):
    if funcion == "ingresar dinero":
        ingresar_dinero, dinero_existende, total_dinero = args
        return total_dinero 