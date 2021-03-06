#Programa de lista de compras de supermercado

listado_de_compras = list()

parar = False

print("Bienvenido al supermercado!")

while  not parar:
    #Obtengo los valores de la compra
    nombre = (input("\nEscriba su compra: ").lower().capitalize())
    cantidad = (input("Escriba su cantida: "))
    precio = (input("Escriba su precio: "))

    #Los almaceno en un dicc. y luego los agrego a una lista
    compra = {"nombre" : nombre, "cantidad":int(cantidad), "precio": float(precio)}
    listado_de_compras.append(compra)

    print("Producto agregado.")

    if input("\nQuiere agregar otro item?(s/n) ").upper() == "N":
        parar = True

#Mostrando la cantidad de elementos agregados a la lista de compras    
print(f"\nHubieron {len(listado_de_compras)} elementos agregados ")

#Creando un conjuto de los elementos unicos agregados a la lista de compras
conjunto = set(compras["nombre"] for compras in listado_de_compras)
print(f"Hubieron {len(conjunto)} elementos unicos")

print("\nSu compra fue:")

print("Nombre","Cantidad","Precio","monto a pagar", sep="\t")

total = 0
# Debiste agregar el monto a pagar a los datos guardados, luego sumar esos datos.
for compra in listado_de_compras:
    total += float(compra["cantidad"]*compra["precio"])
    print ('{:<12s}{:<8d}\t{:<.2f}\t{:<.2f}'.format(compra["nombre"], compra["cantidad"] ,compra["precio"],float(compra["cantidad"]*compra["precio"])))

print(f"\tEl total a pagar es: {total:.2f}")