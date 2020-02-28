#ejercico 1
def generar_n_caracteres(n, caracter):
    
    print(caracter * n)
    
    
#generar_n_caracteres(5, "x")


#ejercicio 2

def procedimiento():
    lista_numeros = [4, 9, 7]
    for i in lista_numeros:
        print("*"*i)

#procedimiento()


#ejercicio 3

def superPosicion():
    lista1 = [1, 5, 6, 7]
    lista2 = [2, 4, 3, 7]

    for i  in lista1:
        print(i in lista2)

#superPosicion()

#ejercicio 3
def inversa(cadena):

    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida
    


#print(inversa("estoy probando"))

#ejercicio 4
def palindromo(cadena):
    
    invertida = ""
    count = len(cadena)
    indi = -1
    while count >= 1:
        invertida += cadena[indi]
        indi = indi + (-1)
        count -= 1
    
    if invertida == cadena:
        return True
    else:
        return False


#print(palindromo("huevo"))

#ejercico 5
def mas_larga():
    lista = ['ejercicios', 'php', 'java', 'python', 'funciones', 'C', 'programacion' ]
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

        
#print(mas_larga())


#ejercicio 6 

def filtrar_palabra(n):
    lista = ['ejercicios', 'php', 'java', 'python', 'funciones', 'C', 'programacion' ]
    palabra = ""
    palabras_largas = []
    for i in lista:
        if len(i) > n:
            palabra = i
            palabras_largas.append(palabra)

    for j in palabras_largas:
        print(j)

filtrar_palabra(5)



            
