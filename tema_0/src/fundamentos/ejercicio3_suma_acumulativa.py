from utils import input_int

def main():
    suma = 0
    print("Introduce números positivos (negativo para terminar):")
    
    while True:
        numero = input_int("Número: ")
        if numero < 0:
            break
        suma += numero
        print(f"Suma acumulada: {suma}")
    
    print(f"Suma total: {suma}")

if __name__ == "__main__":
    main()
