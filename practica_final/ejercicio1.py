class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int = 2020):
        self.marca = marca
        self.modelo = modelo
        self._anio = 2020
        self.actualizar_anio(anio)

    def actualizar_marca(self, nueva_marca: str):
        self.marca = nueva_marca

    def actualizar_anio(self, nuevo_anio: int):
        if nuevo_anio > 0:
            self._anio = nuevo_anio
        else:
            print(f"[Error] El año '{nuevo_anio}' debe ser mayor que cero.")

    def obtener_anio(self):
        return self._anio

    def mostrar_datos(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Año: {self._anio}")


class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca: str, modelo: str, anio: int, codigo: str, tarifa_diaria: float):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self._tarifa_diaria = 0.0
        self.actualizar_tarifa(tarifa_diaria)

    def actualizar_tarifa(self, nueva_tarifa: float):
        if nueva_tarifa > 0:
            self._tarifa_diaria = nueva_tarifa
        else:
            print(f"[Error] Tarifa inválida ({nueva_tarifa}). No se modificó, se mantiene en: {self._tarifa_diaria}")

    def obtener_tarifa(self):
        return self._tarifa_diaria

    def aumentar_tarifa(self, porcentaje: float = 10):
        if porcentaje > 0:
            incremento = self._tarifa_diaria * (porcentaje / 100)
            self._tarifa_diaria += incremento
        else:
            print("[Error] El porcentaje de incremento debe ser mayor a cero.")

    def calcular_descuento(self, dias_alquiler: int):
        if dias_alquiler < 2:
            porcentaje_desc = 5
        elif 2 <= dias_alquiler <= 5:
            porcentaje_desc = 10
        else:
            porcentaje_desc = 15

        importe_bruto = self._tarifa_diaria * dias_alquiler
        monto_descuento = importe_bruto * (porcentaje_desc / 100)
        total_final = importe_bruto - monto_descuento

        print("--------------------------------------------------")
        print(f"--- REPORTE DE ALQUILER (Días: {dias_alquiler}) ---")
        print("--------------------------------------------------")
        self.mostrar_datos()
        print(f"Código de alquiler: {self.codigo}")
        print(f"Tarifa diaria actual: ${self._tarifa_diaria:.2f}")
        print(f"Importe antes del descuento ({dias_alquiler} días): ${importe_bruto:.2f}")
        print(f"Descuento aplicado: {porcentaje_desc}% (${monto_descuento:.2f})")
        print(f"TOTAL FINAL A PAGAR: ${total_final:.2f}")
        print("--------------------------------------------------\n")



if __name__ == "__main__":
    print("=== 1. CREACIÓN DE VEHÍCULOS ===")
    auto1 = VehiculoAlquiler("Toyota", "Corolla", 2022, "V-001", 50.0)
    auto2 = VehiculoAlquiler("Hyundai", "Accent", 2021, "V-002", 40.0)

    auto1.mostrar_datos()
    auto2.mostrar_datos()
    print()

    print("=== 2. DOS INCREMENTOS CONSECUTIVOS A LA TARIFA ===")
    print(f"Tarifa inicial de {auto1.marca}: ${auto1.obtener_tarifa():.2f}")

    auto1.aumentar_tarifa()
    print(f"Tras 1er incremento (10%): ${auto1.obtener_tarifa():.2f}")

    auto1.aumentar_tarifa(porcentaje=20)
    print(f"Tras 2do incremento (20%): ${auto1.obtener_tarifa():.2f}")
    print()

    print("=== 3. CÁLCULO DE DESCUENTOS CON DISTINTAS CANTIDADES DE DÍAS ===")
    auto1.calcular_descuento(1)

    auto1.calcular_descuento(4)

    auto2.calcular_descuento(7)

    print("=== 4. PRUEBA DE TARIFA NEGATIVA ===")
    print(f"Tarifa actual de {auto2.marca}: ${auto2.obtener_tarifa():.2f}")
    print("Intentando asignar una tarifa negativa (-15.5)...")
    auto2.actualizar_tarifa(-15.5)
    print(f"Tarifa final tras el intento fallido: ${auto2.obtener_tarifa():.2f}")