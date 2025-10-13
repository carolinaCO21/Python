
from utils import input_str, input_int, validar_telefono
def mostrar_menu():
    print("\n === AGENDA === ")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar todos")
    print("5. Salir")

def main():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input_int("Opción (1-5): ", min_val=1, max_val=5)

        if opcion == 1:
            nombre = input_str("Nombre: ")
            while True:
                telefono = input_str("Telefono: ")
                if validar_telefono(telefono):
                    break
                print("Error: Telefono debe tener solo numeros y al menos 7 dígitos")

            agenda[nombre] = telefono
            print("Contacto agregado")

        elif opcion == 2:
            nombre = input_str("Nombre a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado")
            else:
                print("Contacto no encontrado")

        elif opcion == 3:
            nombre = input_str("Nombre a buscar: ")
            print(f"Teléfono: {agenda.get(nombre, 'No encontrado')}")

        elif opcion == 4:
            if agenda:
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("Agenda vacía")

        elif opcion == 5:
            print("¡Hasta luego!")
            break


# Ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    main()