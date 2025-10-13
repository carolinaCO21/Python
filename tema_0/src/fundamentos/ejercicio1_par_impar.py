from utils import input_int

def main():
    numero = input_int("Introduce un número: ")
    print(f"El número {numero} es {'PAR' if numero % 2 == 0 else 'IMPAR'}")

if __name__ == "__main__":
    main()
