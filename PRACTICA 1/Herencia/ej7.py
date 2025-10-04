class Persona:
    def __init__(self, nombre, paterno, materno, edad): 
        self._nombre = nombre  
        self._paterno = paterno  
        self._materno = materno  
        self._edad = edad 

    def get_nombre(self):
        return self._nombre

    def get_paterno(self):
        return self._paterno

    def get_materno(self):
        return self._materno

    def get_edad(self):
        return self._edad

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_paterno(self, paterno):
        self._paterno = paterno

    def set_materno(self, materno):
        self._materno = materno

    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser un valor positivo.")

    def mostrar(self):
        return f"Nombre: {self._nombre}, Apellido Paterno: {self._paterno}, Apellido Materno: {self._materno}, Edad: {self._edad}"


class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, reg_profesional): 
        super().__init__(nombre, paterno, materno, edad)
        self._sueldo = sueldo 
        self._reg_profesional = reg_profesional 

    def get_sueldo(self):
        return self._sueldo

    def get_reg_profesional(self):
        return self._reg_profesional

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def set_reg_profesional(self, reg_profesional):
        self._reg_profesional = reg_profesional

    def mostrar(self):
        return f"{super().mostrar()}, Sueldo: {self._sueldo}, Reg. Profesional: {self._reg_profesional}"


class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self._ru = ru 
        self._matricula = matricula 

    def get_ru(self):
        return self._ru

    def get_matricula(self):
        return self._matricula

    def set_ru(self, ru):
        self._ru = ru

    def set_matricula(self, matricula):
        self._matricula = matricula

    def mostrar(self):
        return f"{super().mostrar()}, RU: {self._ru}, Matrícula: {self._matricula}"

print("--- Instanciando objetos ---")
estudiante1 = Estudiante("Ana", "Perez", "Gonzales", 20, "1234567", "2023")
estudiante2 = Estudiante("Luis", "Mamani", "Quispe", 22, "7654321", "2022")
docente1 = Docente("Maria", "Rodriguez", "Vargas", 35, 5000, "12345")

print("\n--- Mostrando datos ---")
print(f"Datos del Estudiante 1: {estudiante1.mostrar()}")
print(f"Datos del Estudiante 2: {estudiante2.mostrar()}")
print(f"Datos del Docente: {docente1.mostrar()}")


def promedio_edad(estudiantes):
    total_edad = sum(estudiante.get_edad() for estudiante in estudiantes)
    return total_edad / len(estudiantes)


estudiantes = [estudiante1, estudiante2]
promedio = promedio_edad(estudiantes)
print(f"\n--- Promedio de edad de los estudiantes: {promedio} ---")

print("\n--- Modificando edad del Estudiante 1 ---")
estudiante1.set_edad(21)
print(f"Nueva edad del Estudiante 1: {estudiante1.get_edad()}")

print("\n--- Verificando si algún estudiante tiene la misma edad que el docente ---")
if estudiante1.get_edad() == docente1.get_edad() or estudiante2.get_edad() == docente1.get_edad():
    print("Al menos un estudiante tiene la misma edad que el docente.")
else:
    print("Ningún estudiante tiene la misma edad que el docente.")
