class Parada:
    def __init__(self, nombreP):
        self.__admins = [None] * 10
        self.__autos = [[None for k in range(3)] for j in range(10)]
        self.__nombreP = nombreP
        self.__nroAdmins = 0
        self.__nroAutos = 0
    def add(self, obj, conductor=None, placa=None):
        if conductor is None and placa is None:
            if self.__nroAdmins < 10:
                self.__admins[self.__nroAdmins] = obj
                self.__nroAdmins += 1
                print(f"Admin {obj} añadido.")
            else:
                print("No se pueden añadir más admins.")
        else:
            if self.__nroAutos < 10:
                self.__autos[self.__nroAutos][0] = obj     
                self.__autos[self.__nroAutos][1] = conductor
                self.__autos[self.__nroAutos][2] = placa
                self.__nroAutos += 1
                print(f"Auto {obj} - {conductor} - {placa} añadido.")
            else:
                print("No se pueden añadir más autos.")

    def mostrar(self):
        print(f"\nNombre de la Parada: {self.__nombreP}")
        print("Admins:")
        for admin in self.__admins:
            if admin:
                print(" -", admin)
        print("Autos:")
        for i in range(self.__nroAutos):
            print(f" - Modelo: {self.__autos[i][0]}, Conductor: {self.__autos[i][1]}, Placa: {self.__autos[i][2]}")

parada = Parada("Parada Principal")
parada.add("Admin1")              
parada.add("Toyota", "Tomas", "123ABC")           
parada.add("Nissan", "Jhonatan", "456XYZ")            

parada.mostrar()
