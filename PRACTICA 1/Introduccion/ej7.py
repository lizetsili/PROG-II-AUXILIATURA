class Mascota:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__energia = 25

    def alimentar(self):
        self.__energia += 20
        if self.__energia > 100:
            self.__energia = 100
        print(f"{self.__nombre} fue alimentado. Energía: {self.__energia}")

    def jugar(self):
        self.__energia -= 15
        if self.__energia < 0:
            self.__energia = 0
        print(f"{self.__nombre} jugó. Energía: {self.__energia}")

    def mostrarEnergia(self):
        print(f"Energía de {self.__nombre}: {self.__energia}")
        return self.__energia

mascota1 = Mascota("Coquito", "Perro")
mascota2 = Mascota("Jinu", "Gato")

print("\n--- Simulación de mascotas ---")
mascota1.mostrarEnergia()
mascota2.mostrarEnergia()

mascota1.alimentar()
mascota2.alimentar()

mascota1.jugar()
mascota2.jugar()

mascota1.alimentar()
mascota2.jugar()
