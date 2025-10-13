from utils import input_int

def main():
    numeros = [input_int(f"Numero {i+1}: ") for i in range(8)]
    for num in numeros:
        print(f"{num} - {'PAR' if num % 2 == 0 else 'IMPAR'}")

if __name__ == "__main__ ":
    main()