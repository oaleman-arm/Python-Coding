
tipo_cambio_usd = input("Ingrese el Tipo de Cambio del dia: C$")
tipo_cambio_usd = float(tipo_cambio_usd)
cordobas = input("Ingrese la cantidad total de dinero:")
cordobas = float(cordobas)
opcion = input("Elija una operacion: \n 1- De cordobas a dolares \n 2- De Dolares a cordobas \n")
opcion = int(opcion)

if opcion == 1: print("El total en dolares es:$ " + str(cordobas/tipo_cambio_usd))

if opcion == 2: print("El total en dolares es:C$ " + str(cordobas*tipo_cambio_usd))

if opcion > 2 and opcion < 1 : print("Elija una opcion valida")

