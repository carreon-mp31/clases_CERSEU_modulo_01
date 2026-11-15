import random


def generar_aleatorios(n: int) -> list:
    try:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("La cantidad 'n' debe ser un número entero estrictamente positivo (> 0).")

        return [random.randint(1, 100) for _ in range(n)]
    except ValueError as e:
        print(f"[Error de validación] {e}")
        return []


def eliminar_duplicados(lista: list) -> list:
    return list(dict.fromkeys(lista))


def ordenar_listas(lista: list):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente


def mayor_numero_par(lista: list):
    pares = [num for num in lista if num % 2 == 0]
    if not pares:
        return "No existen números pares en la lista."
    return max(pares)


def obtener_elemento(lista: list, posicion: int):
    try:
        return lista[posicion]
    except IndexError:
        return f"[Error] La posición '{posicion}' está fuera del rango de la lista (Tamaño: {len(lista)})."
    except TypeError:
        return "[Error] La posición debe ser un número entero válido."