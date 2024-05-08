#variables
valor=0
precio=0
precio1=0
precio2=0
precio3=0
precio4=0
codigo=""

valor_final=0
valor_final_condescuento=0
otro_pedido=1
agregar_otro=1
#dar bienvenida al usuario
while otro_pedido==1:
    #Mostrar menu
    print("Bienvenido, selecciona el roll que deseas comprar")

    while agregar_otro==1:
        
        print("1) Pikachu Roll $4.500")
        print("2) Otaku Roll $5.000")
        print("3) Pulpo venenoso Roll $5.200")
        print("4) Anguila Eléctrica Roll $4.800")
        #seleccionar roll
        rolls_sushi=int(input("Opcion 1-4: "))
        #Calculo de precios
        if rolls_sushi==1:
            precio1=precio1+4500
        elif rolls_sushi==2:
            precio2=precio2+5000
        elif rolls_sushi==3:
            precio3=precio3+5200
        elif rolls_sushi==4:
            precio4=precio4+4800
        #Calculo total
        valor_final=precio1+precio2+precio3+precio4
        
        #Agregar otro roll
        agregar_otro=int(input("Deseas agregar otro roll? 1=Si 0=No"))
        
   
        
        #solicitar codigo de descuento

    codigo_descuento=int(input("Posee un codigo de descuento? 1=si 0=no"))
    if codigo_descuento==1:
        codigo=input("ingrese codigo de descuento: ")
            
        if codigo=="soyotaku":
            valor_final_condescuento=valor_final-(valor_final*0.1)
            print(f"El valor de su compra es: {valor_final_condescuento}")
    elif codigo_descuento==0:
        print(f"El valor final de su compra sin descuento es: {valor_final}")
        
                
                #preguntar si desea otro pedido
    otro_pedido=int(input("Deseas agregar otro pedido 1=si 0=no"))
            



    

