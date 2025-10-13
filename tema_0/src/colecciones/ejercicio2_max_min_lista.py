from utils import input_float

def main():
    numeros = [input_float(f"Numero {i+1}: ") for i in range(10)]
    print(f"Maximo: {max(numeros)}, Minimo: {min(numeros)}")

if __name__== "__main __ ":
    main()