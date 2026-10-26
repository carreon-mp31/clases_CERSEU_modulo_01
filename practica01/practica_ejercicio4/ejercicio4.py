"""Lista de participantes"""
participantes=[]
"""Lista de participanntes creada"""
participantes.append("Paulo Carreon")
participantes.append("Richard Yancce")
participantes.append("Marlon Alvarez")

"""Inserta un nuevo participante en la segunda posición."""

participantes.insert(1, "Jose Castillo")

"""Actualiza el nombre del primer participante."""
participantes[0] = "Jesus Espejo"

"""Eliminamos a un participante"""

participantes.remove("Marlon Alvarez")
print("Lista de participantes")
print(participantes)
