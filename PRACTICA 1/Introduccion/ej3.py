class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            total = cantidad * self.__precio
            print(f"Se vendieron {cantidad} unidades de {self.__nombre}.")
            print(f"Ingreso total: Bs. {total}")
        else:
            print(f"No hay suficiente stock. Solo quedan {self.__stock} unidades.")

    def reabastecer(self, cantidad):
        self.__stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades. Stock actual: {self.__stock}")

    def mostrar_stock(self):
        print(f"Stock actual de {self.__nombre}: {self.__stock}")
        return self.__stock

producto1 = Producto("Helado", 7.50, 50)

print("\n--- Simulación de Producto ---")
producto1.vender(9)     
producto1.mostrar_stock()  
producto1.vender(32)       
producto1.reabastecer(21)  
producto1.mostrar_stock()
