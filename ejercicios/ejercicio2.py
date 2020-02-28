#Escribir un programa que le diga al usuario que ingrese una cadena. 
# El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

def conytarMayus(cadena:str):
    mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    contaMyus = 1
    for i in mayusculas:
        if i in cadena:
            contaMyus += 1 

    return contaMyus
#mensaje = input('ingrese mensaje: ')
#print(conytarMayus(mensaje))

#Ejercicio 6 
# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

#respuesta:

# añoCurso = input('Ingrese el año de curso actual: ')
# fehActual = int(añoCurso)
# vuelta = 0
# datos = []
# estudiantes= []
# while vuelta < 3:
#     nombre = input('ingrese nombre de estudiante: ')
#     añoNacimiento = input('Ingrese el año de nacimiento: ')
#     fecha = int(añoNacimiento)
#     datos.append(nombre)
#     datos.append(fecha)
#     estudiantes.append(datos)
#     datos = []
#     vuelta += 1

def calcuEdad(añoActual, Participantes):
    
    for i in Participantes:
        edad = añoActual - i[1]
        print('La edad de '+i[0]+' es '+str(edad))
            

#calcuEdad(fehActual, estudiantes)

def contar_vocales(palabra):
    vocales = 'aeiou'
    contaVocal = 0
    for vocal in vocales:
        print(f'{vocal} : {palabra.count(vocal)}')
            
#palabra = input('Ingrese la palabra: ')
#contar_vocales(palabra)



#Definir una lista con un conjunto de nombres,
# imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar. 
# (Un poco mas emocionante)

usuarios = ['cercio', 'maria', 'simon', 'andres', 'delcy', 'karelba', 'mariela']

def usuarioPorLetra(usuarios, letra):
    contarUser = 0
    for user in usuarios:
        if user[0] == letra:
            contarUser += 1
    
    return contarUser

letra = input('introducir letra: ')
print(usuarioPorLetra(usuarios, letra))






