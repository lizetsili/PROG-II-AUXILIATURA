class Persona:
    def __init__(self, nombre, apellido, ci):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ci = ci

    def mostrar_datos(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, CI: {self.__ci}"
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, ci, nrocompra, idcliente):
        super().__init__(nombre, apellido, ci) 
        self.__nrocompra = nrocompra
        self.__idcliente = idcliente

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Nro. Compra: {self.__nrocompra}, ID Cliente: {self.__idcliente}"

class Jefe(Persona):
    def __init__(self, nombre, apellido, ci, sucursal, tipo):
        super().__init__(nombre, apellido, ci)
        self.__sucursal = sucursal
        self.__tipo = tipo

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Sucursal: {self.__sucursal}, Tipo Jefe: {self.__tipo}"
persona1 = Persona("Juan", "Huallpa", "8347822")
cliente1 = Cliente("Maria", "Gonzales", "7654321", "C001", "CLI001")
jefe1 = Jefe("Carla", "Ramirez", "9876543", "Zona Sur", "Gerente")

print(f"Datos de Persona: {persona1.mostrar_datos()}")
print(f"Datos de Cliente: {cliente1.mostrar_datos()}")
print(f"Datos de Jefe: {jefe1.mostrar_datos()}")
