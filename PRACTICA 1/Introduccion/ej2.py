class Bus:
    def __init__(self, capacidad):
        self.__capacidad = capacidad     
        self.__pasajeros = 0              
        self.__costo_pasaje = 1.50        

    def subir_pasajeros(self, cantidad):
        if self.__pasajeros + cantidad <= self.__capacidad:
            self.__pasajeros += cantidad
            print(f"Subieron {cantidad} pasajeros. Total a bordo: {self.__pasajeros}")
        else:
            disponibles = self.__capacidad - self.__pasajeros
            print(f"No pueden subir {cantidad}. Solo hay {disponibles} asientos disponibles.")

    def cobrar_pasaje(self):
        total = self.__pasajeros * self.__costo_pasaje
        print(f"Se cobraron Bs. {total:.2f} por {self.__pasajeros} pasajeros.")
        return total
    
    def asientos_disponibles(self):
        disponibles = self.__capacidad - self.__pasajeros
        print(f"Asientos disponibles: {disponibles}")
        return disponibles

miBus = Bus(40) 

print("\n--- Simulación del Bus ---")
miBus.subir_pasajeros(25) 
miBus.subir_pasajeros(10)   
miBus.subir_pasajeros(8)    

miBus.cobrar_pasaje()       
miBus.asientos_disponibles()
