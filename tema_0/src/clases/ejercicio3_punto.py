import math
from utils import input_int


class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def desplaza(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, otro):
        """Devuelve la distancia entre este punto y otro."""
        return math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)

    def __str__(self):
        """Representación en cadena del punto."""
        return f"({self.x}, {self.y})"


def main():
    # Crear los dos puntos iniciales
    x1 = input_int("Coordenada X del punto 1: ")
    y1 = input_int("Coordenada Y del punto 1: ")
    p1 = Punto(x1, y1)

    x2 = input_int("Coordenada X del punto 2: ")
    y2 = input_int("Coordenada Y del punto 2: ")
    p2 = Punto(x2, y2)

    # Menú interactivo
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar puntos")
        print("2. Calcular distancia entre puntos")
        print("3. Desplazar un punto")
        print("4. Modificar coordenadas de un punto")
        print("0. Salir")

        opcion = input_int("Elige una opción: ")

        if opcion == 1:
            print(f"Punto 1: {p1}")
            print(f"Punto 2: {p2}")

        elif opcion == 2:
            print(f"Distancia entre puntos: {p1.distancia(p2):.2f}")

        elif opcion == 3:
            num_punto = input_int("¿Qué punto deseas desplazar? (1 o 2): ")
            dx = input_int("Desplazamiento X: ")
            dy = input_int("Desplazamiento Y: ")

            if num_punto == 1:
                p1.desplaza(dx, dy)
                print(f"Punto 1 desplazado: {p1}")
            elif num_punto == 2:
                p2.desplaza(dx, dy)
                print(f"Punto 2 desplazado: {p2}")
            else:
                print("Opción no válida.")

        elif opcion == 4:
            num_punto = input_int("¿Qué punto deseas modificar? (1 o 2): ")
            x = input_int("Nueva coordenada X: ")
            y = input_int("Nueva coordenada Y: ")

            if num_punto == 1:
                p1.setXY(x, y)
                print(f"Punto 1 modificado: {p1}")
            elif num_punto == 2:
                p2.setXY(x, y)
                print(f"Punto 2 modificado: {p2}")
            else:
                print("Opción no válida.")

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
