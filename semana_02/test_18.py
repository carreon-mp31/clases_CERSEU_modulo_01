"""
## Ejercicio de Participación para Práctica 01
Tema: Listas en Python: creación, manipulación y métodos

### Objetivo
Aplicar los métodos de listas estudiados en clase para agregar, insertar, eliminar, modificar y organizar elementos en Python.

### Requisitos

**1. Creación de listas**

Crear dos listas vacías llamadas `usuario_1` y `usuario_2`.

Agregar a cada lista los siguientes datos, utilizando `append()` e `insert()`:

- Nombre (`str`)
- Apellido paterno (`str`)
- Edad (`int`)
- Profesión (`str`)

**2. Operaciones a realizar**

1. Suma de edades: Obtener y mostrar la suma de las edades de ambos usuarios mediante sus índices.
2. Concatenación: Unir ambas listas utilizando el operador `+` y guardar el resultado en una nueva lista llamada `usuarios`.
3. Invertir elementos: Utilizar `reverse()` para invertir el orden de la lista `usuarios` y mostrar el resultado.
4. Eliminar elementos: Utilizar `pop()`, `remove()` o `del` para eliminar la edad del primer usuario y el apellido del segundo usuario de la lista concatenada.
5. Actualizar información: Modificar la profesión del segundo usuario mediante su índice.
6. Contar elementos: Utilizar `count()` para verificar cuántas veces aparece un valor de su elección.
7. Copiar la lista: Utilizar `copy()` para generar una copia de la lista actualizada.
8. Mostrar resultados: Imprimir la lista original concatenada y la lista final después de las modificaciones.

**3. Consideraciones**

- Utilizar los métodos `append()`, `insert()`, `pop()`, `remove()`, `reverse()`, `count()` y `copy()` según corresponda.
- Incluir comentarios que expliquen las operaciones realizadas.
- Mostrar los resultados utilizando `print()`.
- Tener en cuenta que los índices cambian al eliminar o invertir elementos.
- El programa debe ejecutarse correctamente y sin errores.

### Indicaciones para la entrega

- Fecha: Hoy, domingo 18 de octubre
- Hora máxima: 7:00 p.m.
- Correo: docente.cerseu.unmsm@gmail.com
- Asunto: Participación a Práctica 02

Adjuntar: Archivo.py con la solución desarrollada
Importante: Colocar su nombre y apellido completo como comentario al inicio del archivo

"""

# ==========================================
# Nombre y Apellido: [TU NOMBRE Y APELLIDO AQUÍ]
# Participación para Práctica 01
# Tema: Listas en Python
# ==========================================

usuario_1 = []
usuario_2 = []

usuario_1.append("Juan")
usuario_1.append("Pérez")
usuario_1.append(25)
usuario_1.insert(3, "Ingeniero")

usuario_2.append("Maria")
usuario_2.insert(1, "Gómez")
usuario_2.append(30)
usuario_2.append("Diseñadora")

# 1. Suma de edades mediante sus índices
suma_edades = usuario_1[2] + usuario_2[2]
print("1. Suma de las edades:", suma_edades)

# 2. Concatenación con operador +
usuarios = usuario_1 + usuario_2
print("2. Lista concatenada:", usuarios)

# 3. Invertir elementos con reverse()
usuarios.reverse()
print("3. Lista invertida:", usuarios)

# 4. Eliminar elementos usando del y remove()
del usuarios[5]
usuarios.remove("Gómez")
print("4. Lista tras eliminar elementos:", usuarios)

# 5. Actualizar información mediante su índice
usuarios[0] = "Arquitecta"
print("5. Lista tras actualizar profesión:", usuarios)

# 6. Contar elementos con count()
cantidad = usuarios.count("Juan")
print("6. Cantidad de veces que aparece 'Juan':", cantidad)

# 7. Copiar la lista con copy()
copia_usuarios = usuarios.copy()

# 8. Mostrar resultados
print("\n--- RESULTADOS FINALES ---")
print("Lista final:", usuarios)
print("Copia de la lista:", copia_usuarios)