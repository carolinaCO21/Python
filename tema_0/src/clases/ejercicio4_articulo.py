from utils import input_float, input_int, input_str

class Articulo:
    def __init__(self, nombre, precio, cuantosQuedan, iva=21):
        if precio < 0 or cuantosQuedan < 0:
            raise ValueError("Precio y cantidad no pueden ser negativos")
        self.nombre = nombre
        self.precio = precio
        self.iva = iva
        self.cuantosQuedan = cuantosQuedan

    def getPVP(self):
        """ precio de venta al público (con IVA)."""
        return self.precio * (1 + self.iva / 100)

    def getPVPDescuento(self, descuento):
        """ PVP con un descuento"""
        if not (0 <= descuento <= 100):
            raise ValueError("El descuento debe estar entre 0 y 100")
        return self.getPVP() * (1 - descuento / 100)

    def vender(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser positiva")
        if cantidad <= self.cuantosQuedan:
            self.cuantosQuedan -= cantidad
            return True
        return False

    def almacenar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a almacenar debe ser positiva")
        self.cuantosQuedan += cantidad

    def __str__(self):
        return f"{self.nombre} - {self.getPVP():.2f}€ - Stock: {self.cuantosQuedan}"

    def __eq__(self, other):
        """ iguales si tienen el mismo nombre."""
        if not isinstance(other, Articulo):
            return NotImplemented
        return self.nombre == other.nombre

    def __lt__(self, other):
        """alfabéticamente por nombre."""
        if not isinstance(other, Articulo):
            return NotImplemented
        return self.nombre < other.nombre


def main():
    try:
        nombre = input_str("Nombre del artículo: ")
        precio = input_float("Precio (sin IVA): ", min_val=0)
        stock = input_int("Stock inicial: ", min_val=0)

        articulo = Articulo(nombre, precio, stock)
        print(f"\nArtículo creado: {articulo}")

        while True:
            print("\n--- MENÚ ---")
            print("1. Ver PVP")
            print("2. PVP con descuento")
            print("3. Vender")
            print("4. Almacenar")
            print("5. Ver información")
            print("6. Salir")

            opcion = input_str("Opción (1-6): ", opciones_validas=['1', '2', '3', '4', '5', '6'])

            if opcion == '1':
                print(f"PVP: {articulo.getPVP():.2f}€")

            elif opcion == '2':
                descuento = input_float("Porcentaje de descuento: ", min_val=0, max_val=100)
                print(f"PVP con descuento: {articulo.getPVPDescuento(descuento):.2f}€")

            elif opcion == '3':
                cantidad = input_int("Cantidad a vender: ", min_val=1)
                if articulo.vender(cantidad):
                    print("Venta realizada correctamente.")
                else:
                    print("Stock insuficiente.")

            elif opcion == '4':
                cantidad = input_int("Cantidad a almacenar: ", min_val=1)
                articulo.almacenar(cantidad)
                print("Almacenamiento realizado correctamente.")

            elif opcion == '5':
                print(articulo)

            elif opcion == '6':
                print("Saliendo del programa...")
                break

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
