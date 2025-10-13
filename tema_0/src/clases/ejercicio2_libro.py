from utils import input_int, input_str

from utils import input_int, input_str

class Libro:
    def __init__(self, titulo: str, autor: str, ejemplares: int, prestados: int = 0):
        if ejemplares < 0 or prestados < 0:
            raise ValueError("Los ejemplares y prestados no pueden ser negativos")
        if prestados > ejemplares:
            raise ValueError("Los prestados no pueden ser mayores que los ejemplares totales")
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = prestados

    def prestamo(self) -> bool:
        if self.prestados < self.ejemplares:
            self.prestados += 1
            return True
        return False

    def devolucion(self) -> bool:
        if self.prestados > 0:
            self.prestados -= 1
            return True
        return False

    def __str__(self) -> str:
        return f"'{self.titulo}' por {self.autor} - {self.ejemplares - self.prestados}/{self.ejemplares} disponibles"

    def __repr__(self) -> str:
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', disponibles={self.ejemplares - self.prestados})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Libro) and self.titulo == other.titulo and self.autor == other.autor

    def __lt__(self, other) -> bool:
        return isinstance(other, Libro) and self.autor < other.autor


def buscar_por_texto(biblioteca: list[Libro], texto: str) -> list[Libro]:
    texto = texto.strip().lower()
    return [libro for libro in biblioteca if texto in libro.titulo.lower() or texto in libro.autor.lower()]


def main():
    biblioteca: list[Libro] = []

    while True:
        print("\n1. Añadir libro")
        print("2. Buscar y gestionar libro")
        print("3. Salir")
        opcion = input_str("Opción (1-3): ", opciones_validas=['1', '2', '3'])

        if opcion == '1':
            try:
                titulo = input_str("Título: ").strip()
                autor = input_str("Autor: ").strip()
                ejemplares = input_int("Ejemplares totales: ", min_val=1)
                libro = Libro(titulo, autor, ejemplares)
                biblioteca.append(libro)
                print(f"Libro agregado: {libro}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            if not biblioteca:
                print("No hay libros en la biblioteca.")
                continue
            texto = input_str("Texto de búsqueda (título o autor): ").strip()
            resultados = buscar_por_texto(biblioteca, texto)
            if not resultados:
                print("No se encontraron coincidencias")
                continue

            print("Libros encontrados:")
            for idx, libro in enumerate(resultados, 1):
                print(f"{idx}. {libro}")

            seleccion = input_int("Selecciona un libro por número: ", min_val=1, max_val=len(resultados))
            libro = resultados[seleccion - 1]

            while True:
                print(f"\nHas seleccionado: {libro}")
                print("1. Prestar")
                print("2. Devolver")
                print("3. Ver estado")
                print("4. Volver al menú principal")
                sub_op = input_str("Opción (1-4): ", opciones_validas=['1', '2', '3', '4'])
                if sub_op == '1':
                    print("Préstamo realizado" if libro.prestamo() else "No hay ejemplares disponibles")
                elif sub_op == '2':
                    print("Devolución realizada" if libro.devolucion() else "No hay ejemplares prestados")
                elif sub_op == '3':
                    print(libro)
                elif sub_op == '4':
                    break

        elif opcion == '3':
            print("Hasta luego")
            break


if __name__ == "__main__":
    main()




