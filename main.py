from autenticacion import Autenticacion

def mostrar_menu():
    print("\n------------------------------")
    print("   SISTEMA DE AUTENTICACION    ")
    print("------------------------------")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar datos de usuario")
    print("4. Cambiar contraseña")
    print("5. Cerrar sesión")
    print("6. Salir")

def main():
    
    sistema = Autenticacion()
    
    usuario_actual = None
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registro ---")

            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            password = input("Contraseña (mínimo 8 caracteres): ")

            sistema.registrar_usuario(nombre, correo, password)

        elif opcion == "2":
            if usuario_actual is not None:
                print("Ya existe una sesión activa.")
                continue
            print("\n--- Inicio de sesión ---")
            correo = input("Correo: ").strip()
            password = input("Contraseña: ")

            usuario_actual = sistema.iniciar_sesion(correo, password)

        elif opcion == "3":
            if usuario_actual is not None:
                usuario_actual.mostrar_datos()
            else:
                print("Primero debes iniciar sesión.")

        elif opcion == "4":
            if usuario_actual is None:
                print("Primero debes iniciar sesión.")
                continue
            print("\n--- Cambiar contraseña ---")
            actual = input("Contraseña actual: ")
            nueva = input("Nueva contraseña (mínimo 8 caracteres): ")

            sistema.cambiar_password(usuario_actual, actual, nueva)

        elif opcion == "5":
            if usuario_actual is not None:
                usuario_actual = None
                print("Sesión cerrada exitosamente.")
            else:
                print("No existe una sesión activa.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()