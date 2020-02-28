class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = {}

    def agregarMateria(self, materia, codigo):
        self.materias[codigo]= materia


class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre = nombre
        self.profesor = profesor
        self.fechaInicioDictado = fecha
    
    @property
    def fechaInicioDictado(self):
        return self._fechaInicioDictado

    @fechaInicioDictado.setter
    def fechaInicioDictado(self, fecha):
        if fecha < 2006:
            self._fechaInicioDictado = 2006
        else:
            self._fechaInicioDictado= fecha



ing = Carrera("Ingenieria de sistemas")
matematicas = Materia("Matematicas", "Aldana", 2005)
print(matematicas.fechaInicioDictado)