def inicializar_matriz(cantidad_filas, columnas, valor_inicial):
    """Crea una matriz mediante parametros

    Args:
        cantidad_filas (_type_): obtiene como parametro la cantidad de filas
        columnas (_type_): obtiene como parametro la cantidad de columnas
        valor_inicial (_type_): obtiene como parametro el valor inicial de cada posicion

    Returns:
        _type_: retorna una matriz
    """
    matriz = []
    for _ in range(0, cantidad_filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    
    return matriz

def contabilizar_por_cliente(matriz):
    """Contabiliza la cantidad de paquetes que envía cada cliente.

    Args:
        matriz (_type_): obtiene la matriz a medir

    Returns:
        _type_: Retorna la cantidad de envios de cada cliente
    """
    cantidad = 0
    for i in range(0, len(matriz)):
        for j in range(1, len(matriz[i])):
            cantidad += matriz[i][j]

    return cantidad

def obtener_cantidad_clientes_no_pequenos_ni_grandes(matriz):
    """Obtiene la cantidad de clientes que no enviaron ni paquetes pequeños ni grandes.

    Args:
        matriz (_type_): obtiene la matriz a medir

    Returns:
        _type_: Retorna la cantidad de clientes que no enviaron ni paquetes pequeños ni grandes
    """
    cantidad = 0
    for i in range(0, len(matriz)):
        sin_envio_pequeno = False
        sin_envio_grande = False
        for j in range(1, len(matriz[i])):
            match j:
                case 1:
                    if matriz[i][j] == 0:
                        sin_envio_pequeno = True
                case 2:
                    continue
                case 3:
                    if matriz[i][j] == 0:
                        sin_envio_grande = True
        if sin_envio_grande == True and sin_envio_pequeno == True:
            cantidad += 1
    
    return cantidad
"""
def informar_clientes_a_pagar(matriz):
    bandera_pagos = True
    listado_pagos = []
    listado_pagos = inicializar_matriz(2, 2, 0)
    for i in range(0, len(matriz)):
        cantidad_a_pagar = 0
        cliente = 1
        for j in range(1, len(matriz[i])):
            match j:
                case 1:
                    if matriz[i][j] > 0:
                        cantidad_a_pagar += matriz[i][j] * 1000
                case 2:
                    if matriz[i][j] > 0:
                        cantidad_a_pagar += matriz[i][j] * 1500
                case 3:
                    if matriz[i][j] > 0:
                        cantidad_a_pagar += matriz[i][j] * 2000
        for ix in range(0, listado_pagos):
            for jx in range(0, listado_pagos[ix]):
                if jx == 0:
                    listado_pagos[ix][jx] += f"Cliente num {cliente}°"
                else:
                    listado_pagos[ix][jx] += cantidad_a_pagar
        cliente += 1

    for i in range(0, listado_pagos):
        for j in range(1, listado_pagos[i]):
            if bandera_pagos:
                pago_mayor = listado_pagos[i][j]
                listado_pagos[i][j - 1] = f"Cliente num: {listado_pagos[ix][0]}°"
                bandera_pagos = False
            else:
                if listado_pagos[i][j] >= pago_mayor:
                    pago_mayor = listado_pagos[i][j]
"""

def informar_recaudacion(matriz):
    """Informa cuál fue el/los clientes que enviaron más cantidad de paquetes medianos.

    Args:
        matriz (_type_): obtiene la matriz a medir

    Returns:
        _type_: Retorna el cliente que envio más cantidad de paquetes medianos
    """
    mayor_reacudacion = 0
    cantidad_pequenos = 0
    cantidad_medianos = 0
    cantidad_grandes = 0
    for i in range(0, len(matriz)):
        for j in range(1, len(matriz[i])):
            match j:
                case 1:
                    if matriz[i][j] > 0:
                        cantidad_pequenos += matriz[i][j] * 1000
                case 2:
                    if matriz[i][j] > 0:
                        cantidad_medianos += matriz[i][j] * 1500
                case 3:
                    if matriz[i][j] > 0:
                        cantidad_grandes += matriz[i][j] * 2000
    
    if cantidad_pequenos > cantidad_medianos and cantidad_pequenos > cantidad_grandes:
        mayor_reacudacion = cantidad_pequenos
    else:
        if cantidad_medianos > cantidad_grandes:
            mayor_reacudacion = cantidad_medianos
        else:
            mayor_reacudacion = cantidad_grandes

    mensaje = f"""Reacaudacion: \nPequenos: {cantidad_pequenos}
Medianos: {cantidad_medianos}\nGrandes: {cantidad_grandes}
El tamaño que más recaudó fue {mayor_reacudacion}"""

    return mensaje

def informar_clientes_medianos(matriz):
    bandera_mayor = True
    envio_mayor = 0
    mayor_cliente = ""
    for i in range(0, len(matriz)):
        for j in range(1, len(matriz[i])):
            match j:
                case 1:
                    continue
                case 2:
                        if bandera_mayor:
                            bandera_mayor = False
                            envio_mayor = matriz[i][j]
                            mayor_cliente = f"Cliente {matriz[i][0]}"
                        else:
                            if matriz[i][j] > envio_mayor:
                                envio_mayor = matriz[i][j]
                                mayor_cliente = f"Cliente {matriz[i][0]}"
                case 3:
                    continue
    mensaje = f"Quien envio mas paquetes medianos fue {mayor_cliente} con una cantidad de {envio_mayor}"

    return mensaje