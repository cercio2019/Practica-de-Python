class Empleado:
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.legajo = legajo
        self.sueldo = sueldo

    def calcular_sueldo(self, descuento, bonos):
        return self.sueldo-descuento+bonos



class AgentesVentas(Empleado):
    def __init__(self, nombre, edad, legajo, sueldo, mostrador):
        self.numeroMostrador = mostrador
        super().__init__(nombre, edad, legajo, sueldo)


class Tripulante(Empleado):
    def mostrar_Renovacion(self):
        if self.edad >= 58:
            return "La licencia tiene que ser renovada cada un año"
        else:
            return "La licencia tiene que ser renovada cada 6 meses"



cercio = AgentesVentas("cercio", 24, "m618", 6000, 4)
print(cercio.nombre)
print(cercio.edad)
print(cercio.calcular_sueldo(300, 3000))

t = Tripulante("viloria", 45, "m789", 4000)
print(t.mostrar_Renovacion())

