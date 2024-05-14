import os
#Inicializar variables
clean="cls"
nombre=False
telefono=False
cantidad_camiones=False
valor1=0
kilos_cilindros=0
cantidad_cilindros=False
kilos_gas=0
otro_cilindro=1
otra_cotizacion=1
cantidad_camiones_opcion2=0
#bucle principal de la cotizacion
while otra_cotizacion==1:
        
    #Solicitar los datos del clientes y validarlos
    #Validar nombre
    while nombre==False:
        nombre=input("Ingrese Nombre del cliente: ")
        try:
            if len(str(nombre)) <3:
                print("El nombre debe poseer al menos 3 letras")
                nombre=False
            else:
                nombre=True
        except ValueError:
            print("El nombre debe poseer al menos 3 caracteres")

    #Validar telefono
    while telefono==False:
        telefono=int(input("Ingrese teléfono de contacto: "))
        try:
            if len(str(telefono))>8 and len(str(telefono))>9:
                print("Telefono incorrecto, debe poseer entre 8 y 9 números")
                telefono=False
            else:
                nombre=True
        except ValueError:
            print("Telefono incorrecto, debe poseer entre 8 y 9 numeros ")

    os.system(clean)
    #Comenzar menu principal indicando las opciones
    print("Seleccione la opcion (1-3) que desea cotizar: ")
    print("1) Compra entrega Camión estándar")
    print("2) Compra entrega carga específica")
    print("3) Imprimir boleta y cerrar pedido")
    opcion=int(input("Opcion: "))

    #Opcion 1:
    if opcion==1:
        print("Indique cantidad de camiones")
        while cantidad_camiones<1:
            cantidad_camiones=int(input("Cantidad: "))
            try:
                if cantidad_camiones<1:
                    print("Debe seleccionar al menos 1 camion")
                    cantidad_camiones=False
                else:
                    print(f"Has seleccionado {cantidad_camiones} camiones ")
                    valor_1=765000*cantidad_camiones
                    break

            except ValueError:
                print("Debes seleccionar al menos 1 camion")
        valor1=765000*cantidad_camiones

    #Opcion 2:
    elif opcion==2:
        while otro_cilindro==1:            
            print("Indique los kilos del cilindro (5 kg- 15 kg- 45 kg): ")
            while kilos_cilindros<1:
                    kilos_cilindros=int(input("kilos: "))  
                    kilos_gas=kilos_cilindros
                    try:
                        if kilos_cilindros<1:
                            print("Debe ser 5, 15 o  45")
                            kilos_cilindros=kilos_cilindros
                            
                        else:
                            print("")
                            break
                    except ValueError:
                        print("Solo puede ingresar: 5 kg, 15kg o 45kg")
            while cantidad_cilindros==False:
                        cantidad_cilindros=int(input("Ingresa la cantidad de cilindros: "))
                        try:
                            if cantidad_cilindros<1:
                                print("Debes seleccionar al menos un cilindro")
                                cantidad_cilindros=False
                            else:
                                print(" ")
                                break
                        except ValueError:
                            print("Debes seleccionar al menos un cilindro")
            otro_cilindro=int(input("Deseas agregar otro tipo de cilindro? 1=si 2=no"))
        
            kilos_cilindros=False
            cantidad_cilindros=False
            

    #Opcion 3:
    elif opcion==3:
        print("Aun no has seleccionado nada...")
        print(f"Cliente: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Cantidad de kilos {kilos_cilindros}")
        print(f"Camiones: {cantidad_camiones}")
        print(f"Valor Total: {valor1}")
    #Imprimir boleta
    os.system(clean)
    if opcion==1:
        print(f"Cliente: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Cantidad de kilos: camion estandar")
        print(f"Camiones: {cantidad_camiones}")
        print(f"Valor Total: {valor1}")
    elif opcion==2:
        print(f"Cliente: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Cantidad de kilos {kilos_cilindros}")
        #Calcular cuantos camiones necesitara y el valor:
        cantidad_camiones2=kilos_cilindros//450
        residuo=kilos_cilindros%450
        if residuo>0:
            valor2=((residuo*1700)+100000)+(cantidad_camiones2*765000)
            cantidad_camiones2+=1
        else:
            cantidad_camiones2=cantidad_camiones2
            valor2=cantidad_camiones2*765000
        print(f"Camiones: {cantidad_camiones2}")
        print(f"Valor Total: {valor2}")
   

    

    print("Desea realizar otra cotizacion 1=si 2=no, salir del programa")
    otra_cotizacion=int(input("Opción: "))
    #limpiar variables para realizar otra cotizacion
    nombre=False
    telefono=False
    cantidad_camiones=False
    valor1=0
    kilos_cilindros=0
    cantidad_cilindros=False
    kilos_gas=0
    otro_cilindro=1
    otra_cotizacion=1
    cantidad_camiones_opcion2=0
    otra_cotizacion=1
    nombre=False
    telefono=False
    os.system(clean)

            
        











        



