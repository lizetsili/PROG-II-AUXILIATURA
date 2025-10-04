class Persona:
    def __init__(self,nombre,paterno,materno,edad,ci):
        self.__nombre=nombre
        self.__paterno=paterno
        self.__materno=materno
        self.__edad=edad
        self.__ci=ci

    def mostrarDatos(self):
        print(f"Nombre:{self.__nombre} {self.__paterno} {self.__materno}")
        print(f"Edad: {self.__edad}")
        print(f"Ci:{self.__ci}")

    def mayorDeEdad(self):
        if self.__edad>=18:
            print(f"{self.__nombre}:Es mayor de edad")
            return True
        else:
            print(f"{self.__nombre}:Es menor de edad")
            return False
        
    def modificarEdad(self,nEdad):
        self.__edad=nEdad
        print(f"La Edad de {self.__nombre} se cambio ahora es {self.__edad}")
        
    def getPaterno(self):
        return self.__paterno
    
persona1 = Persona("Juana","Balboa","Sanchez",18,"983542")
persona2= Persona("Luz","Hilari","Mendoza",15,"748393")

print("----------DATOS DE LAS PERSONAS------------------")
persona1.mostrarDatos()
persona2.mostrarDatos()

print("------------Sus Edades-----------------")
persona1.mayorDeEdad()
persona2.mayorDeEdad()

print("--------------Modificar edad----------------")
persona1.modificarEdad(34)
persona1.mostrarDatos()

print("-------Comparacion de Apellidos------------")
if persona1.getPaterno() == persona2.getPaterno():
    print("Tienen el mismo apellido")
else:
    print("No tienen el mismo apellido")