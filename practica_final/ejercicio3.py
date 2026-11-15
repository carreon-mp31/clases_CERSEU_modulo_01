from datetime import datetime


def registrar_pedido(func):

    def wrapper(*args, **kwargs):
        ahora = datetime.now()
        fecha_hora_str = ahora.strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n[LOG] Ejecutando operación - Fecha y Hora: {fecha_hora_str}")

        resultado = func(*args, **kwargs)

        if resultado is not None:
            print("[ÉXITO] La operación finalizó correctamente.")

        print("-" * 65)
        return resultado

    return wrapper


@registrar_pedido
def calcular_total(*args):
    total = 0.0
    for precio in args:
        if not isinstance(precio, (int, float)) or precio <= 0:
            print(f"[Error] Precio inválido detectado ({precio}). Debe ser un número mayor a cero.")
            return None
        total += float(precio)
    return total


@registrar_pedido
def procesar_pedido(nombre_cliente: str, **kwargs):
    print(f"Cliente: {nombre_cliente}")
    total = 0.0
    for producto, precio in kwargs.items():
        if not isinstance(precio, (int, float)) or precio <= 0:
            print(f"[Error] Precio inválido en el producto '{producto}' (${precio}). Debe ser mayor a cero.")
            return None
        print(f"   • {producto}: ${precio:.2f}")
        total += float(precio)
    return total



if __name__ == "__main__":
    print("=================================================================")
    print("         SISTEMA DE GESTIÓN Y PEDIDOS - RAPPI            ")
    print("=================================================================")

    print("\n--- PRUEBA 1: calcular_total con *args ---")

    print(">> Ejecutando con 3 precios (15.50, 40.0, 10.0):")
    res_3 = calcular_total(15.50, 40.0, 10.0)
    if res_3 is not None:
        print(f"Importe Total Sumado: ${res_3:.2f}")

    print("\n>> Ejecutando con 6 precios (12.0, 8.5, 45.0, 9.99, 15.0, 20.0):")
    res_6 = calcular_total(12.0, 8.5, 45.0, 9.99, 15.0, 20.0)
    if res_6 is not None:
        print(f"Importe Total Sumado: ${res_6:.2f}")

    print("\n--- PRUEBA 2: procesar_pedido con **kwargs ---")

    print(">> Pedido 1: 4 productos válidos (Cliente: Carlos Mendoza)")
    total_valido = procesar_pedido(
        "Carlos Mendoza",
        hamburguesa=28.50,
        papas_fritas=10.0,
        gaseosa=6.50,
        helado=12.0
    )
    if total_valido is not None:
        print(f"TOTAL FINAL A PAGAR: ${total_valido:.2f}")

    print("\n>> Pedido 2: Contiene un precio negativo (Cliente: Ana Lucía)")
    total_invalido = procesar_pedido(
        "Ana Lucía",
        pizza_familiar=55.0,
        agua_mineral=4.0,
        ensalada_cesar=-8.50,
        postre=14.0
    )
    if total_invalido is not None:
        print(f"TOTAL FINAL A PAGAR: ${total_invalido:.2f}")
    else:
        print("[Aviso] El pedido fue rechazado por contener precios no válidos.")