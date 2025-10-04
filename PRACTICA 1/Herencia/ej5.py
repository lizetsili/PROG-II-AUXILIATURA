class Vehiculo:
    def __init__(self, conductor, placa, id):
        self._conductor = conductor
        self._placa = placa
        self._id = id

    def get_conductor(self):
        return self._conductor

    def get_placa(self):
        return self._placa

    def get_id(self):
        return self._id

    def set_conductor(self, nuevo_conductor):
        self._conductor = nuevo_conductor

    def mostrar_datos(self):
        return f"Conductor: {self._conductor}, Placa: {self._placa}, ID: {self._id}"


class Bus(Vehiculo):
    def __init__(self, conductor, placa, id, capacidad, sindicato):
        super().__init__(conductor, placa, id) 
        self._capacidad = capacidad
        self._sindicato = sindicato

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Capacidad: {self._capacidad}, Sindicato: {self._sindicato}"


class Auto(Vehiculo):
    def __init__(self, conductor, placa, id, caballos_fuerza, descapotable):
        super().__init__(conductor, placa, id)
        self._caballos_fuerza = caballos_fuerza
        self._descapotable = descapotable

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Caballos de fuerza: {self._caballos_fuerza}, Descapotable: {self._descapotable}"


class Moto(Vehiculo):
    def __init__(self, conductor, placa, id, cilindrada, casco):
        super().__init__(conductor, placa, id) 
        self._cilindrada = cilindrada
        self._casco = casco

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Cilindrada: {self._cilindrada}, Casco: {self._casco}"

bus1 = Bus("Juan Perez", "ABC-123", 1, 50, "Los Andes")
auto1 = Auto("Maria Rodriguez", "DEF-456", 2, 150, True)
moto1 = Moto("Carlos Gomez", "GHI-789", 3, 200, True)

print(bus1.mostrar_datos())
print(auto1.mostrar_datos())
print(moto1.mostrar_datos())

bus1.set_conductor("Lorein Fernandez")
print(f"Nuevo conductor del Bus: {bus1.get_conductor()}")
