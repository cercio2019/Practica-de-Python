class Gato:
    def __init__(self, nombre, edad, dueño, comidas):
        self.nombre = nombre
        self.edad = edad
        self.dueño = dueño
        self.comidas = comidas

    def imprimir_edad(self):
        if self.edad >= 10:
            print(self.nombre+' es un gato adulto')
        else:
            print(self.nombre+' es un gato cachorro')

    def buscar_comida(self, comida):
       busqueda = comida in self.comidas
       if busqueda == True:
           return comida+' si esta registrada en la lista de comida de '+self.nombre
       else:
           return comida+' no se encuentra registrado en en la lista de esta mascota'  


    def registrar_comida(self, comida):
        self.comidas.append(comida)
        print(comida+' fue registrada en la lista de comida de '+self.nombre)
        print(self.comidas)



comidas = ["arroz", "sardina", "pollo", "carne"]
gato = Gato('canela', 12, 'osveyri', comidas)
comida = input("introducir la comida que desea buscar: ")
print(gato.buscar_comida(comida))
new_comida = input("introducir la nueva comida que desea registrar: ")
gato.registrar_comida(new_comida)


