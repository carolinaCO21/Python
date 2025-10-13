from utils import input_float

def main():
    a = input_float("Primer número: ")
    b = input_float("Segundo número: ")
    ordenados = sorted([a, b])
    print(f"Ordenados: {ordenados[0]}, {ordenados[1]}")

if __name__ == "__main__":
    main()
