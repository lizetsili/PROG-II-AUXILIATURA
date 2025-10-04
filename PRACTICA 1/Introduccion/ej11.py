class Cliente:
    def __init__(self, nombre, pedido):
        self.__nombre = nombre
        self.__pedido = pedido
        print(f"Cliente {self.__nombre} creado.")

    def getNombre(self):
        return self.__nombre

    def getPedido(self):
        return self.__pedido

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setPedido(self, pedido):
        self.__pedido = pedido

    def __del__(self):
        print(f"Cliente {self.__nombre} eliminado.")


class Pedido:
    def __init__(self, estado, total):
        self.__estado = estado
        self.__total = total
        print("Pedido creado.")

    def getEstado(self):
        return self.__estado

    def getTotal(self):
        return self.__total
    
    def setEstado(self, estado):
        self.__estado = estado

    def setTotal(self, total):
        self.__total = total

    def __del__(self):
        print("Pedido eliminado.")

pedido1 = Pedido("Registrado", 35.50)
cliente1 = Cliente("julian", pedido1)

print("\n--- Datos del cliente ---")
print("Nombre:", cliente1.getNombre())
print("Pedido:", cliente1.getPedido().getEstado(), "/ Total Bs.", cliente1.getPedido().getTotal())
