import json
def guardar_gastos(gastos):
    with open("gastos.txt", "w") as archivo:
        json.dump(gastos, archivo)
    print("\nGastos guardados correctamente.")
def cargar_gastos():
    try:
        with open("gastos.txt", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
print("Mis gastos")

# Pedir datos del usuario
nombre = input("Nombre del usuario: ")

# Dar la bienvenida
print()
print("¡Hola, Bienvenido", nombre, "!")
print("Te ayudaremos a controlar mejor tus gastos")
gastos = cargar_gastos()
# Menú de ingresos
while True:
    print("\n¿Cómo es tu ingreso?")
    print("1 - Mensual")
    print("2 - Quincenal")
    print("3 - Semanal")
    print("4 - Diario")

    opcion = input("Ingrese su opción: ")
    if opcion == "1":
        while True:
             ingreso = float(input("\n¿Cuánto es tu ingreso mensual? "))
             if ingreso >=0:
                print("\nIngreso mensual registrado:", ingreso)
                break
             print("\nEl ingreso no puede ser negativo. \nIntenta de nuevo")
        break
    elif opcion == "2":
        while True:
             ingreso = float(input("¿Cuánto es tu ingreso quincenal? "))
             if ingreso >=0:
                print("\nIngreso quincenal registrado:", ingreso)
                break
             print("\nEl ingreso no puede ser negativo.\nIntenta de nuevo")
        break
    elif opcion == "3":
        while True:
             ingreso = float(input("¿Cuánto es tu ingreso semanal? "))
             if ingreso >=0:
                print("\nIngreso semanal registrado:", ingreso)
                break
             print("\nEl ingreso no puede ser negativo.\nIntenta de nuevo")
        break
    elif opcion == "4":
        while True:
             ingreso = float(input("¿Cuánto es tu ingreso diario? "))
             if ingreso >=0:
                 print("\nIngreso diario registrado:", ingreso)
                 break
             print("\nEl ingreso no puede ser negativo.\nIntenta de nuevo") 
        break
    else:
        print("\nOpción no válida, inténtelo nuevamente.")
# Registro de gastos 
while True:
    print("\n¿Deseas agregar un gasto?")
    print("1 - Comida")
    print("2 - Ropa")
    print("3 - Combustible")
    print("4 - Vehiculo")
    print("5 - Hogar")
    print("6 - Internet")
    print("7 - TV")
    print("8 - Transporte")
    print("9 - Fiesta")
    print("10 - Salud")
    print("11- Otros gastos")
    print("R- Ver estado de cuenta")
    print("0- Regresar")
    opcion_gasto = input("Elige una opción:")
    if opcion_gasto == "0":
       break
    elif opcion_gasto.upper() == "R":
        total_gastos = sum (gastos.values())
        print("\nResumen de gastos")
        for categoria, monto in gastos.items():
           print(f"{categoria}: {monto}")
        print(f"Total gastado: {total_gastos}")
        print(f"Diferecia con ingreso: {ingreso - total_gastos}")
        continue
    categorias = {
        "1": "Comida",
        "2": "Ropa",
        "3": "Combustible",
        "4": "Vehiculo",
        "5": "Hogar",
        "6": "Internet",
        "7": "TV",
        "8": "Transporte",
        "9": "Fiesta",
        "10": "Salud",
        "11": "Otros gastos",
        "12": "Ver estao de cuenta",
    }
    if opcion_gasto in categorias:
       categoria = categorias[opcion_gasto]
       try:
          monto = float(input(f"\nCuanto gastaste en {categoria}?"))
       except ValueError:
              print("\nEse no es in nimero. Intenta de nuevo")
              continue
       if monto < 0:
          print("\nEl gasto no purde ser negativo")
          continue
       gastos[categoria] = gastos.get(categoria, 0) + monto
       print(f"Gasto agregado en {categoria}: {monto}")
       guardar_gastos(gastos)
    else:
          print("\nOpcion invalida, intenta otraves.")