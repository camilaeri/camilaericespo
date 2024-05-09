#definir variables
valor=0
precio=0
precio1=0
precio2=0
precio3=0
precio4=0
codigo=False
precio_total=0
valor_final_condescuento=0
otro_pedido=1
agregar_otro=1
contador1=0
contador2=0
contador3=0
contador4=0
cantidad_total=0
precio_final=0
#Comenzar bucle principal
while otro_pedido==1:
    #Dar la bienvenida al usuario
    print("Bienvenido, selecciona el roll que deseas comprar: ")
    #Iniciar bucle para mostrar menú mientras quiera agregar otro
    while agregar_otro==1:
        
        print("1) Pikachu Roll $4.500")
        print("2) Otaku Roll $5.000")
        print("3) Pulpo venenoso Roll $5.200")
        print("4) Anguila Eléctrica Roll $4.800")
        #Seleccionar Roll
        rolls_sushi=int(input("Opcion 1-4: "))
        #Preguntar si desea agregar otro roll
        agregar_otro=int(input("Deseas agregar otro roll? 1=Si 0=No \nOpcion: "))
        #Calculo de precios y cantidades
        if rolls_sushi==1:
            precio1=precio1+4500
            contador1=contador1+1
        elif rolls_sushi==2:
            precio2=precio2+5000
            contador2=contador2+1
        elif rolls_sushi==3:
            precio3=precio3+5200
            contador3=contador3+1
        elif rolls_sushi==4:
            precio4=precio4+4800
            contador4=contador4+1
        #Calculo total de precio y cantidades
        precio_total=precio1+precio2+precio3+precio4
        cantidad_total=contador1+contador2+contador3+contador4
    #Preguntar si tiene codigo de descuento
    codigo_descuento=int(input("Tienes algun codigo de descuento? 1=si 0=no \nOpción: "))
    if codigo_descuento==1:
                #Validar codigo
                while codigo==False:
                    try:
                        codigo=input("Ingresa tu codigo: ")
                        if codigo=="soyotaku":
                            codigo=True
                            precio_final=precio_total-(round(precio_total*0.1))
                        else:
                            ("Codigo erroneo, intenta otra vez o vuelve al menu apretando X \nOpcion: ")
                            codigo=False
                            
                    except ValueError:
                        print("Codigo invalido")
    else:
         precio_final=precio_total
                             

    #Imprimir detalle de compra
    print("*"*40)
    print(f"TOTAL PRODUCTOS {cantidad_total}")
    print("*"*40)
    print(f"Pikachu Roll: {contador1}")
    print(f"Otaku Roll: {contador2}")
    print(f"Pulpo venenoso Roll: {contador3}")
    print(f"Anguila electrica Roll: {contador4}")
    print("")
    print("*"*40)
    print(f"Subtotal por pagar: {precio_total}")
    if codigo==True:
        print(f"Descuento por codigo: {(round(precio_total*0.1))}")
    else:
        print("Descuento por codigo: 0")
    print(f"Total: {precio_final} ")
    print("")
    #Preguntar si desea agregar otro pedido
    otro_pedido=int(input("Desea agregar otro pedido? 1=si 0=no \nOpcion: "))
    #Limpiar variables para iniciar bucle principal nuevamente si así lo desea el usuario
    agregar_otro=1
    codigo=False
    



        

            
    
        