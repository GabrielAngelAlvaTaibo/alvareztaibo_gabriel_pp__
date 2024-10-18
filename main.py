from Package_Calculos.Generales import *
from Package_Calculos.Especificas import *

clientes = 3
matriz_clientes = []
cantidad_cadenas = 2
matriz_clientes = inicializar_matriz(2, 4, 0)

for i in range(0, len(matriz_clientes)):
    cantidad_carga = 0
    contador_pequeno = 0
    contador_mediano = 0
    contador_grande = 0
    while cantidad_carga <= 5:
        carga = validate_number("""Ingrese un numero dependiendo del tipo de paquete: 
Pequeño: 1\nMediano: 2\nGrande: 3\nSalir: 4\n""",0,5,3)
        match carga:
            case 1:
                contador_pequeno += 1
                cantidad_carga += 1
            case 2:
                contador_mediano += 1
                cantidad_carga += 1
            case 3:
                contador_grande += 1
                cantidad_carga += 1
            case 4:
                break
            case _:
                print("Error de ingreso")
    for j in range(0, len(matriz_clientes[i])):
        contador_clientes = 0
        match j:
            case 0:
                matriz_clientes[i][j] = f"Cliente num{matriz_clientes[j][i] + 1}"
            case 1:
                matriz_clientes[i][j] = contador_pequeno
            case 2:
                matriz_clientes[i][j] = contador_mediano
            case 3:
                matriz_clientes[i][j] = contador_grande


while True:
    opciones = input("""1. Cantidad de paquetes que envía cada cliente.
2. Cantidad de clientes que no enviaron ni paquetes pequeños ni grandes.
3. Generar un informe de clientes ordenados por el total a pagar de sus envíos de forma
descendente.
4. Total de la recaudación en pesos por cada tipo de paquete. Además, necesitamos saber
cuál es el tamaño que más recaudó.
5. Informar cuál fue el/los clientes que enviaron más cantidad de paquetes medianos.
6. Salir""")
    opciones = int(opciones)
    match opciones:
        case 1:
            if matriz_clientes == None:
                print("Primero Obtener datos")
            else:
                resultado = contabilizar_por_cliente(matriz_clientes)
                print(resultado)
        case 2:
            if matriz_clientes == None:
                print("Primero Obtener datos")
            else:
                resultado = obtener_cantidad_clientes_no_pequenos_ni_grandes(matriz_clientes)
                print(resultado)
        case 3:
            if matriz_clientes == None:
                print("Primero Obtener datos")
            else:
                """resultado = informar_clientes_a_pagar(matriz_clientes)
                print(resultado)"""
        case 4:
            if matriz_clientes == None:
                print("Primero Obtener datos")
            else:
                resultado = informar_recaudacion(matriz_clientes)
                print(resultado)
        case 5:
            if matriz_clientes == None:
                print("Primero Obtener datos")
            else:
                resultado = informar_clientes_medianos(matriz_clientes)
                print(resultado)
        case 6:
            break
        case _:
            "Error de tipeo"

