while True:
    # menu principal
    print("1.Registrar nuevo usuario")
    intentos_1 = int(0)
    print("2.Usuario registrado")
    print("3.Configuración avanzada")
    print("4.Salir")
    opcion = int(input())
    if opcion == 1: # opcion para registrase como nuevo usuario
            while intentos_1 < 3: # numero de intentos para ingresar cedula correcta
                cedula = input("Ingrese su cedula\nLa cedula debe constar de 9 numeros\n")#solicitud de cedula
                if cedula.__len__() == 9: #cedula correcta
                    intentos_1 = 3
                    print("Cedula aceptada")
                    nombre = str(input("Ingrese primer nombre\n"))
                    apellido1 = str(input("Ingrese primer apellido\n"))
                    apellido2 = str(input("Ingrese segundo apellido\n"))
                    while True:
                        import getpass
                        pin = getpass.getpass("Ingrese un PIN de 4 caracteres")
                        if pin.__len__() == 4:
                            
                            print("Pin aceptado")
                            while True:
                                pinConfirmacion = getpass.getpass("Confirme su PIN")
                                if pin==pinConfirmacion:
                                    print("Su usuario ha sido registrado con exito")
                                    break
                                   
                                else:
                                    pin != pinConfirmacion
                                    print("PIN no coincide")
                            break
                        else:
                            print("Error")
                            print("El PIN debe constar de 4 numeros")
                        

                else: # no se cumple con requerimientos de cedula
                    print("Error, no se digitaron la cantidad de caracteres requeridos")
                    intentos_1 = intentos_1 + 1
                    if intentos_1 == 3:
                        print("""Se excedió el máximo de intentos
para ingresar un numero de cedula valido, 
volviendo al menú principal""")
    else:
        break