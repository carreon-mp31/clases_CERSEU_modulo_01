"""Variables"""
Nombre = "Leonardo"
Matematicas= 17
Ciencia= 14
Historia=15
"""Proceso"""
PromedioFinal=(Matematicas*0.4)+(Ciencia*0.3)+(Historia*0.3)
print("La nota final es: {:.1f}".format(PromedioFinal))
"""Evaluación y Resumen"""
aprobado = PromedioFinal >= 13.0
print("¿Aprobado?: {}".format(aprobado))
if aprobado:
    print("El estudiante obtuvo una nota final de {:.1f} y su estado final es: Aprobado".format(PromedioFinal))
else:
    print("El estudiante obtuvo una nota final de {:.1f} y su estado final es: Desaprobado".format(PromedioFinal))
