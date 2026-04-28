#TP final primera parte de: Bruno Cardoso, Jeremias Papadopulos y Lautaro Bulaich.

usuario_pre = "pepe"
contra_pre = "gitano"

acceso = "logueo"
acceso_concedido = False

while acceso_concedido != True:
    match acceso:
        case "logueo":
            print("Inicio de sesión")

            usuario_in = input("Ingrese el usuario: ")
            contra_in = input("Ingrese la contraseña: ")

            if usuario_in == usuario_pre and contra_in == contra_pre:
                print(f"Acceso concedido, Bienvenido {usuario_pre}")
                acceso_concedido = True
            else:
                res = input("Datos incorrectos, ¿desea registrarse? (si/no): ")

                if res.lower() == "si":
                    acceso = "registro"
                else:
                    acceso = "salir"

        case "registro":
            print("Registro de usuario")

            usuario_pre = input("Cree un usuario: ")
            contra_pre = input("Cree una contraseña: ")

            print("Usuario registrado correctamente")
            acceso = "logueo"   # vuelve al login

        case "salir":
            print("Saliendo del sistema...")
            break

print ("Menu de opciones: ")
print ("A- Proyectos.")
print ("B- Tablas.")
print ("C- Variables.")        
print ("D- Mostrar.")
print ("E- Estadistica.")
print ("F- Salir.")

menu_opciones= input ("Seleccione una de las opciones: ").lower()

match menu_opciones:
    case "a":
        print ("Entrando al menu de proyectos.")
    case "b":
        print ("Entrando al menu de tablas.")
    case "c":
        print ("Entrando al menu de variables.")
    case "d":
        print ("Entrando al menu de mostrar.")
    case "e":
        print ("Entrando al menu de estadistica.")
    case "f":
        print ("Saliendo del programa.")
    case _:
        print ("Opcion invalida, ingrese una de las letras antes mencionadas.")                        
