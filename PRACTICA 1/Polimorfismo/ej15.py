class Ordenador:
    def __init__(self, serial, numero, ram, procesador, estado="activo"):
        self.__serial = serial
        self.__numero = numero
        self.__ram = ram
        self.__procesador = procesador
        self.__estado = estado 

    def __str__(self):
        return f"Serial: {self.__serial}, Nº: {self.__numero}, RAM: {self.__ram}GB, Procesador: {self.__procesador}, Estado: {self.__estado}"

    @property
    def estado(self):
        return self.__estado

    @property
    def ram(self):
        return self.__ram

    @property
    def serial(self):
        return self.__serial


class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__ordenadores = []

    def agregar_ordenador(self, ordenador):
        if len(self.__ordenadores) < self.__capacidad:
            self.__ordenadores.append(ordenador)
        else:
            print("No hay espacio para más ordenadores.")
    def informacion(self, estado=None, ram_min=None):
        print(f"\nOrdenadores en {self.__nombre}:")
        for o in self.__ordenadores:
            if estado and o.estado != estado:
                continue
            if ram_min and o.ram <= ram_min:
                continue
            print(o)
    def trasladar(self, otros_lab, cantidad):
        print(f"\nTraslado desde {self.__nombre} a {otros_lab.__nombre}:")
        print("Antes del traslado:")
        self.informacion()
        if cantidad > len(self.__ordenadores):
            cantidad = len(self.__ordenadores)
        for _ in range(cantidad):
            ordenador = self.__ordenadores.pop(0)
            otros_lab.agregar_ordenador(ordenador)
        print("Después del traslado:")
        self.informacion()
        otros_lab.informacion()
lab1 = Laboratorio("Lasin 1", 5)
lab2 = Laboratorio("Lasin 2", 5)

o1 = Ordenador("S001", 1, 16, "Intel i7")
o2 = Ordenador("S002", 2, 8, "Intel i5")
o3 = Ordenador("S003", 3, 12, "AMD Ryzen 5", "inactivo")
o4 = Ordenador("S004", 4, 4, "Intel i3")
o5 = Ordenador("S005", 5, 32, "AMD Ryzen 7")
o6 = Ordenador("S006", 6, 16, "Intel i9", "inactivo")

for o in [o1, o2, o3]:
    lab1.agregar_ordenador(o)
for o in [o4, o5, o6]:
    lab2.agregar_ordenador(o)
print("\n-- Ordenadores activos en Lasin 1 --")
lab1.informacion(estado="activo")
print("\n-- Ordenadores con más de 8GB de RAM en Lasin 2 --")
lab2.informacion(ram_min=8)
lab1.trasladar(lab2, 2)
