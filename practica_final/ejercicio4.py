inventario = {
    "P001": {"nombre": "Laptop Gamer", "precio": 3200.0, "cantidad": 5},
    "P002": {"nombre": "Mouse Inalámbrico", "precio": 65.0, "cantidad": 25},
    "P003": {"nombre": "Teclado Mecánico", "precio": 180.0, "cantidad": 12},
    "P004": {"nombre": "Monitor 24 pulgadas", "precio": 750.0, "cantidad": 8}
}


def mostrar_inventario():
    print("=" * 65)
    print(f"{'CÓDIGO':<8} | {'PRODUCTO':<22} | {'PRECIO (S/)':<12} | {'STOCK':<8}")
    print("-" * 65)
    for codigo, datos in inventario.items():
        print(f"{codigo:<8} | {datos['nombre']:<22} | S/ {datos['precio']:<9.2f} | {datos['cantidad']:<8}")
    print("=" * 65)


def realizar_compra(codigo_producto: str, cantidad_solicitada: int):

    print(f"\n[PROCESANDO COMPRA] Producto: {codigo_producto}, Cantidad: {cantidad_solicitada}")

    if codigo_producto not in inventario:
        print(f"[Error] El producto con código '{codigo_producto}' no existe en el inventario.")
        return None

    producto = inventario[codigo_producto]

    if cantidad_solicitada <= 0:
        print("[Error] La cantidad solicitada debe ser mayor a cero.")
        return None

    if cantidad_solicitada > producto["cantidad"]:
        print(
            f"[Error] Stock insuficiente. Stock disponible: {producto['cantidad']} unidades (Solicitado: {cantidad_solicitada}).")
        return None

    importe = cantidad_solicitada * producto["precio"]
    producto["cantidad"] -= cantidad_solicitada

    print(f"[¡COMPRA EXITOSA!]")
    print(f"   • Producto: {producto['nombre']}")
    print(f"   • Cantidad comprada: {cantidad_solicitada}")
    print(f"   • Importe total a pagar: S/ {importe:.2f}")
    print(f"   • Stock restante: {producto['cantidad']} unidades")
    return importe


def calcular_valor_inventario() -> float:
    valor_total = 0.0
    for datos in inventario.values():
        valor_total += datos["precio"] * datos["cantidad"]
    return valor_total



if __name__ == "__main__":
    print("=== 1. MOSTRAR INVENTARIO INICIAL ===")
    mostrar_inventario()
    print(f"Valor monetario inicial del inventario: S/ {calcular_valor_inventario():.2f}\n")

    print("=== 2. REALIZAR OPERACIONES DE COMPRA ===")

    realizar_compra("P002", 4)

    realizar_compra("P999", 2)

    realizar_compra("P001", 10)

    print("\n=== 3. MOSTRAR INVENTARIO ACTUALIZADO Y VALOR TOTAL ===")
    mostrar_inventario()
    print(f"Valor monetario final del inventario: S/ {calcular_valor_inventario():.2f}")