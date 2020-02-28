color = "blue"

if color == "red":
    print(f"el color es {color}")
elif color == "blue":
    print(f"el color es {color}")
else:
    print(f"el color puede ser cualquiera")    




personas = ["marce", "freitez", "cercio", "carolina", "lucy"]

nombre = input("Intoducir el nombre que desea buscar: ")

if nombre in personas:
    print(f"{nombre} se encuentra registrada en la base de datos ")
else:
        print("Esta persona no se encuentra registrada en la base de datos")