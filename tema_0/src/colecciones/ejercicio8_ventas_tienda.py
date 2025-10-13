from utils import input_int, input_str

def mostrar_menu():
    print("\n === VENTAS TIENDA === ")
    print("1. Agregar venta")
    print("2. Total por producto")
    print("3. Salir")

def main():
    ventas ={}

    while True:
        mostrar_menu()
        opcion = input_int("Opcion (1-3): ", min_val=1, max_val=3)

        if opcion == 1:
            producto = input_str("Producto:")
            cantidad = input_int("Cantidad vendida: ", min_val=1)
            ventas[producto] = ventas.get(producto, 0) + cantidad
            print("Venta registrada")
        elif opcion == 2:
            producto = input_str("Producto: ")
            print(f"Total vendido: {ventas.get(producto, 0)}")

        elif opcion == 3:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()