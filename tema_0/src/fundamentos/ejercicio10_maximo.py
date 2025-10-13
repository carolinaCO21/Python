from utils import input_float

def maximo(a, b):
    return a if a > b else b

def main():
    a = input_float("Primer número: ")
    b = input_float("Segundo número: ")
    print(f"El máximo es: {maximo(a, b)}")

if __name__ == "__main__":
    main()
