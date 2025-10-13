from utils import input_int

def mostrar_rango(a, b):
    inicio, fin = min(a, b), max(a, b)
    print(f"Números entre {a} y {b}: ", end="")
    for i in range(inicio + 1, fin):
        print(i, end=" ")
    print()

def main():
    a = input_int("Primer número: ")
    b = input_int("Segundo número: ")
    mostrar_rango(a, b)

if __name__ == "__main__":
    main()
