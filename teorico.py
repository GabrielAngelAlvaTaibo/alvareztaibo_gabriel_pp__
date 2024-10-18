def determinar_caracteres(cadena: str) -> str:
    """recibe una cadena de caracteres y realiza el conteo total de caracteres, 
    vocales en mayusculas y todas las palabras.

    Args:
        cadena (str): Es el parametro string que recibe.

    Returns:
        str: Es el retorno de los resultados del conteo.
    """
    cantidad_vocales = 0
    cantidad_caracteres = 0
    cantidad_palabras = 0
    for i in range(0, len(cadena)):
        if not(cadena[i] == "" or cadena[i] == " "):
            cantidad_palabras += 1
            cantidad_caracteres += 1
            match cadena[i]:
                case "A" | "E" | "I" | "O" | "U":
                    cantidad_vocales += 1
                case _:
                    pass
        else:
            cantidad_palabras += 1
    
    mensaje = f"Se econtraron {cantidad_vocales} vocales en mayusculas \n Se econtraron {cantidad_caracteres} caracteres \n Se econtraron {cantidad_palabras} palabras"
    return mensaje

print(determinar_caracteres(""))