def validate_number(ingreso: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    contador_reintentos = 0
    while True:
        validacion = True
        if contador_reintentos == reintentos:
            numero = 0
            break
        numero = input(ingreso)
        for i in range(0, len(numero)):
            if numero[i] < "0" or numero[i] > "9":
                contador_reintentos += 1
                print("No es un numero")
                numero = input(numero)
                validacion = False
        if validacion:
            numero = int(numero)
            if numero > minimo and numero < maximo:
                print("Verificado correctamente")
                break
            else:
                contador_reintentos += 1
                print("Fuera de rango")
    
    return numero