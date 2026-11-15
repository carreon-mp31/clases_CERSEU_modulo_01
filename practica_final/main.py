import operaciones as op


def ejecutar_prueba(n_cantidad: int, posicion_prueba: int):
    print("=" * 60)
    print(f" EJECUCIÓN CON CANTIDAD n = {n_cantidad} ")
    print("=" * 60)

    print(f"1. Generando lista original de {n_cantidad} elementos...")
    lista_original = op.generar_aleatorios(n_cantidad)

    if not lista_original and n_cantidad <= 0:
        print("-> Prueba de cantidad inválida superada correctamente (retornó lista vacía).\n")
        return

    print(f"   Lista Original: {lista_original}")

    lista_sin_dup = op.eliminar_duplicados(lista_original)
    print(f"2. Lista sin duplicados: {lista_sin_dup}")

    asc, desc = op.ordenar_listas(lista_original)
    print(f"3. Orden Ascendente:  {asc}")
    print(f"   Orden Descendente: {desc}")

    mayor_par = op.mayor_numero_par(lista_original)
    print(f"4. Mayor número par: {mayor_par}")

    print(f"5. Buscando elemento en la posición [{posicion_prueba}]:")
    resultado_pos = op.obtener_elemento(lista_original, posicion_prueba)
    print(f"   Resultado: {resultado_pos}")
    print("\n")


if __name__ == "__main__":
    print("=== INICIO DE PRUEBAS OBLIGATORIAS ===\n")

    ejecutar_prueba(n_cantidad=10, posicion_prueba=3)

    ejecutar_prueba(n_cantidad=7, posicion_prueba=15)

    ejecutar_prueba(n_cantidad=-5, posicion_prueba=0)