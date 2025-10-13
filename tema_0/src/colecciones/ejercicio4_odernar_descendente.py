from utils import input_float

def main():
    numeros = [input_float(f"Numero {i+1}: ") for i in range(10)]
    ordenados = sorted(numeros, reverse=True)
    print(f"Ordenados descendente: {ordenados}")

if __name__ == "__main __ ":
    main()

