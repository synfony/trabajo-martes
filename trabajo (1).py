cliente=str(input("Ingrese el nombre del cliente (Para terminar el program ingrese fin) "))


total_recaudado=0
cantidad_clientes=0
clientes_con_regalo = 0
while cliente != "fin":
    cantidad_produtos=int(input( "Ingrese la cantidad del productos "))
    suma_precios=0

    for i in range(1,cantidad_produtos+1):

        precio_unitario=int(input(f"Ingrese el valor del producto {i}: "))

        suma_precios+=precio_unitario

    if  cantidad_produtos  >= 5 and cantidad_produtos <10:
        descuento=suma_precios*0.10
        total=suma_precios-descuento
        print(f"El valor de la compra de { cliente } es de {total}")
    elif cantidad_produtos >=10:
        descuento=suma_precios*0.10
        clientes_con_regalo += 1
        total=suma_precios-descuento
        print("Felicidades te has ganado un regalo")
        print(f"El valor de la compra de { cliente } es de {total}")
    else:
        total=suma_precios
        print(f"El valor de la compra del { cliente } es de {total}")

    
    total_recaudado+=total
    cantidad_clientes+=1

    cliente=str(input("Ingrese el nombre del cliente (Para terminar el program ingrese fin) "))
    
print(f"\nResumen del día:")
print(f"Total recaudado: ${total_recaudado:.2f}")
print(f"Cantidad de clientes atendidos: {cantidad_clientes}")
print(f"Cantidad de clientes que recibieron un regalo: {clientes_con_regalo}")