def solicitar_dos_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Entrada no numérica detectada. Intente nuevamente.")


def dividir(a, b):
    resultado = None
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except TypeError:
        print("Error: Tipos de datos incompatibles para la división.")
    else:
        print("-> División ejecutada exitosamente sin excepciones.")
    finally:
        print("-> [Finalizando operación de división]")
    return resultado


def sumar(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: No se pueden sumar tipos incompatibles.")
        return None


def registrar_elementos_lista():
    while True:
        try:
            n = int(input("\n¿Cuántos elementos desea registrar en la lista (N)?: "))
            if n <= 0:
                print("Error: N debe ser mayor a cero. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    elementos = []
    for i in range(n):
        val = input(f"Ingrese el elemento {i + 1}: ")
        try:
            if "." in val:
                val = float(val)
            else:
                val = int(val)
        except ValueError:
            pass
        elementos.append(val)
    return elementos


def consultar_indice_lista(lista):
    while True:
        try:
            indice = int(input("\nIngrese el índice que desea consultar: "))
            elemento = lista[indice]
            print(f"Elemento encontrado en el índice [{indice}]: {elemento}")
            return elemento
        except ValueError:
            print("Error: El índice debe ser un número entero.")
        except IndexError:
            print(f"Error: Índice fuera de rango. La lista tiene índices válidos del 0 al {len(lista) - 1}.")


if __name__ == "__main__":
    print("=== EJERCICIO 3: Funciones y Manejo de Excepciones ===")

    print("\n--- Pruebas de Operaciones Matemáticas ---")
    n1, n2 = solicitar_dos_numeros()

    print(f"Resultado de la suma: {sumar(n1, n2)}")

    print("Resultado de la división:")
    res_div = dividir(n1, n2)
    if res_div is not None:
        print(f"Cociente: {res_div}")

    print("\n--- Pruebas de Gestión de Listas y Consultas ---")
    mi_lista = registrar_elementos_lista()
    print("Lista creada exitosamente:", mi_lista)

    consultar_indice_lista(mi_lista)