# Clases base
class Nadador:
    def __init__(self, estilo_natacion):
        self.estilo_natacion = estilo_natacion

    def nadar(self):
        print(f"Nadando estilo {self.estilo_natacion}")


class Ciclista:
    def __init__(self, tipo_bicicleta):
        self.tipo_bicicleta = tipo_bicicleta

    def pedalear(self):
        print(f"Pedaleando en bicicleta tipo {self.tipo_bicicleta}")


class Corredor:
    def __init__(self, distancia_preferida):
        self.distancia_preferida = distancia_preferida

    def correr(self):
        print(f"Corriendo una distancia de {self.distancia_preferida} km")


# Clase Triatleta hereda de las tres
class Triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, estilo_natacion, tipo_bicicleta, distancia_preferida):
        # Inicializar las clases padre
        Nadador.__init__(self, estilo_natacion)
        Ciclista.__init__(self, tipo_bicicleta)
        Corredor.__init__(self, distancia_preferida)


# Crear un objeto Triatleta
t = Triatleta("Crol", "Montaña", 10.5)

# Usar los métodos heredados
t.nadar()
t.pedalear()
t.correr()
