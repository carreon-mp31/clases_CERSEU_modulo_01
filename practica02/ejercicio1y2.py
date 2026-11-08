from datetime import datetime


class Persona:
    def __init__(self, nombre="", edad=0, saldo=0.0, nacionalidad="Peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M")

    def registrar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")

        while True:
            try:
                edad_ingresada = int(input("Ingrese la edad: "))
                if edad_ingresada < 0:
                    print("Error: La edad no puede ser negativa. Intente nuevamente.")
                    continue
                self.edad = edad_ingresada
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido para la edad.")

        while True:
            try:
                saldo_ingresado = float(input("Ingrese el saldo inicial en S/ : "))
                if saldo_ingresado < 0:
                    print("Error: El saldo inicial no puede ser negativo.")
                    continue
                self.saldo = saldo_ingresado
                break
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido para el saldo.")

    def cumpleaños(self):
        self.edad += 1

    def consultar_saldo(self):
        return f"Saldo actual de {self.nombre}: S/ {self.saldo:.2f}"

    def transferir(self, destinatario, monto):
        print(f"\n[Operación] Intentando transferir S/ {monto:.2f} de {self.nombre} a {destinatario.nombre}...")

        try:
            monto = float(monto)
        except (ValueError, TypeError):
            print("Error: El monto de la transferencia debe ser un valor numérico.")
            return False

        if monto <= 0:
            print("Error: El monto a transferir debe ser mayor a cero.")
            return False

        if monto > self.saldo:
            print(
                f"Error: Saldo insuficiente. {self.nombre} tiene S/ {self.saldo:.2f} y se intentó transferir S/ {monto:.2f}.")
            return False

        self.saldo -= monto
        destinatario.saldo += monto
        print("¡Transferencia realizada con éxito!")
        return True


def mostrar_fecha_registro(persona):
    print(f"Persona: {persona.nombre} | Registrada el: {persona.fecha_registro}")


if __name__ == "__main__":
    print("=== EJERCICIO 1: Registro y Datos ===")
    p1 = Persona()
    print("\n-- Registro de la Persona 1 --")
    p1.registrar_datos()

    p2 = Persona()
    print("\n-- Registro de la Persona 2 --")
    p2.registrar_datos()

    print("\n--- Momento de Creación ---")
    mostrar_fecha_registro(p1)
    mostrar_fecha_registro(p2)

    print("\n--- Aplicando Cumpleaños ---")
    p1.cumpleaños()
    p2.cumpleaños()
    print(f"Edad actualizada de {p1.nombre}: {p1.edad} años")
    print(f"Edad actualizada de {p2.nombre}: {p2.edad} años")

    print("\n=== EJERCICIO 2: Transferencias ===")
    print("Saldos iniciales registrados:")
    print(p1.consultar_saldo())
    print(p2.consultar_saldo())

    p1.transferir(p2, 99999.00)

    p1.transferir(p2, -10.00)

    monto_a_enviar = 50.00
    p1.transferir(p2, monto_a_enviar)

    print("\n--- Saldos Finales (Reflejando cambios) ---")
    print(p1.consultar_saldo())
    print(p2.consultar_saldo())