class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.__nroTel = nroTel
        self.__dueño = dueño
        self.__espacio = espacio
        self.__ram = ram          
        self.__nroApp = nroApp 
    def __add__(self, otro):
        if otro == "++": 
            self.__nroApp += 10
        return self
    def __sub__(self, otro):
        if otro == "--":
            self.__espacio -= 5
            if self.__espacio < 0:
                self.__espacio = 0
        return self
    def mostrar(self):
        print(f"Teléfono: {self.__nroTel}")
        print(f"Dueño: {self.__dueño}")
        print(f"Espacio: {self.__espacio} GB")
        print(f"RAM: {self.__ram} GB")
        print(f"Número de Apps: {self.__nroApp}")
        print("---------------------------")

cel1 = Celular("777-12345", "Lucas", 64, 4, 20)
print("Datos antes de operadores:")
cel1.mostrar()
cel1 + "++"  
cel1 - "--"   
print("Datos después de operadores:")
cel1.mostrar()
