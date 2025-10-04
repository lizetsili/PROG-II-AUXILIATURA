# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def desplazarse(self):
        print(f"{self.__nombre} se desplaza de alguna manera.")
class Leon(Animal):
    def desplazarse(self):
        print(f"{self.get_nombre()} camina majestuosamente.")

class Pinguino(Animal):
    def desplazarse(self):
        print(f"{self.get_nombre()} nada ágilmente.")

class Canguro(Animal):
    def desplazarse(self):
        print(f"{self.get_nombre()} salta con fuerza.")

animales = [
    Leon("Leon", 5),
    Pinguino("Pinguino", 3),
    Canguro("Canguro", 4)
]
for animal in animales:
    animal.desplazarse()
