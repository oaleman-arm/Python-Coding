tipo_cambio_usd = input("Ingrese el Tipo de Cambio del dia: C$")
tipo_cambio_usd = float(tipo_cambio_usd)
cordobas = input("Ingrese la cantidad total de cordobas: C$ ")
cordobas = float(cordobas)
total_dolares = cordobas/tipo_cambio_usd
total_dolares = str(total_dolares)
print("El total en dolares es:$ " +total_dolares +"dolares")