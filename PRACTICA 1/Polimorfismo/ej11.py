class Pasajero:
    def __init__(self, nombre, edad, genero, habitacion, costo):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        self.__habitacion = habitacion
        self.__costo = costo

    # getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def genero(self):
        return self.__genero

    @property
    def costo(self):
        return self.__costo

    def __str__(self):
        return f"{self.__nombre} - {self.__genero}, Edad: {self.__edad}, Habitación: {self.__habitacion}, Costo: {self.__costo}"


class Crucero:
    def __init__(self, nombre, origen, destino, pasajeros=None):
        self.__nombre = nombre
        self.__origen = origen
        self.__destino = destino
        self.__pasajeros = pasajeros if pasajeros else []
    @classmethod
    def crear_crucero(cls, nombre, origen, destino, pasajeros=None):
        return cls(nombre, origen, destino, pasajeros)

    def __str__(self):
        return f"{self.__nombre} | Origen: {self.__origen} | Destino: {self.__destino} | Pasajeros: {len(self.__pasajeros)}"

    def __add__(self, pasajero):
        self.__pasajeros.append(pasajero)
        return self

    def __sub__(self, pasajero):
        if pasajero in self.__pasajeros:
            self.__pasajeros.remove(pasajero)
        return self

    def __eq__(self, otro):
        total1 = sum(p.costo for p in self.__pasajeros)
        total2 = sum(p.costo for p in otro.__pasajeros)
        return total1 + total2

    def contar_generos(self):
        hombres = sum(1 for p in self.__pasajeros if p.genero == "Masculino")
        mujeres = sum(1 for p in self.__pasajeros if p.genero == "Femenino")
        return hombres, mujeres

p1 = Pasajero("Juana", 30, "Femenino", 502, 500)
p2 = Pasajero("Marta", 25, "Femenino", 603, 1000)
p3 = Pasajero("Pedro", 40, "Masculino", 401, 925)
c1 = Crucero.crear_crucero("Luz de la Luna", "Corea", "EEUU", [p1, p2])
c2 = Crucero.crear_crucero("Luna", "España", "Italia", [p3])
print(c1)
print(c2)
c1 = c1 + Pasajero("Ana", 28, "Femenino", 202, 700)
print("\nDespués de añadir pasajero a c1:")
print(c1)
c2 = c2 - p3
print("\nDespués de eliminar pasajero de c2:")
print(c2)
print("\nSuma de costos de ambos:", c1 == c2)
print("Cantidad de géneros en c1:", c1.contar_generos())
print("Cantidad de géneros en c2:", c2.contar_generos())
