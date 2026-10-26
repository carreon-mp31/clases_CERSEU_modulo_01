"""Variables"""
Nombre="Paulo Carreon"
Salario=1500
Edad="20"
Compania="Telefonica"

if int(Edad)>30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono = 0.10
else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    bono = 0.05

Bonofinal=(Salario**2)+(Salario*bono)
print("-------------------  RESULTADO FINAL  -------------------")
print("Nombre: {}".format(Nombre))
print("Salario: {}".format(Salario))
print("Edad: {}".format(Edad))
print("Compania: {}".format(Compania))
print("Bono: {}".format(bono))
print("Bono Final: {}".format(Bonofinal))