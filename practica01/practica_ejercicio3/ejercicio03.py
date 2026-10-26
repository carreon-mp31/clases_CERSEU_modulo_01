"""VARIABLES"""
MontoTotal=1000.000
Porcentaje_De_Propina=0.15
NumPersonas=12

"""Proceso"""
montopropina=MontoTotal*Porcentaje_De_Propina
total_con_propina = MontoTotal + montopropina
Propina_persona=montopropina/NumPersonas
"""Salida"""
print("Monto total con propina: S/. {:.2f}".format(total_con_propina))
print("Cada persona debe pagar: S/. {:.2f}".format(Propina_persona))
if Propina_persona>100:
    print("¡Advertencia! El monto por persona supera los S/. 100")