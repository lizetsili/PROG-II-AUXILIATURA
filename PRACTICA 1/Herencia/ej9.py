# Clase base Político
class Politico:
    def __init__(self, profesion, anios_exp):
        self._profesion = profesion
        self._anios_exp = anios_exp

    def get_profesion(self):
        return self._profesion

    def get_anios_exp(self):
        return self._anios_exp
class Partido:
    def __init__(self, nombreP, rol):
        self._nombreP = nombreP
        self._rol = rol

    def get_nombreP(self):
        return self._nombreP

    def get_rol(self):
        return self._rol
class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, anios_exp, nombreP, rol):
        Politico.__init__(self, profesion, anios_exp)
        Partido.__init__(self, nombreP, rol)
        self._nombre = nombre
        self._apellido = apellido

    @classmethod
    def crear_presidente(cls, nombre, apellido, profesion, anios_exp, nombreP, rol):
        return cls(nombre, apellido, profesion, anios_exp, nombreP, rol)

    def mostrar(self):
        return (f"Presidente: {self._nombre} {self._apellido}, Profesión: {self._profesion}, "
                f"Años Exp: {self._anios_exp}, Partido: {self._nombreP}, Rol: {self._rol}")

p1 = Presidente("Juan", "Perez", "Abogado", 15, "Partido Azul", "Líder")
p2 = Presidente.crear_presidente("Maria", "Gomez", "Economista", 20, "Partido Verde", "Coordinador")
p3 = Presidente("Carlos", "Lopez", "Ingeniero", 10, "Partido Rojo", "Representante")
presidentes = [p1, p2, p3]
nombre_buscar = "Maria"
for pres in presidentes:
    if pres._nombre == nombre_buscar:
        print("\n--- Presidente encontrado ---")
        print(f"Nombre: {pres._nombre} {pres._apellido}")
        print(f"Profesión: {pres.get_profesion()}")
        print(f"Partido: {pres.get_nombreP()}")
