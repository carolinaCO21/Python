from utils import input_float, input_int

def calculadora(a, b, operacion):
    operaciones = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x * y,
        4: lambda x, y: x / y if y != 0 else "Error: División por cero"
    }
    return operaciones.get(operacion, lambda x, y: "Operación no válida")(a, b)

def main():
    a = input_float("Primer número: ")
    b = input_float("Segundo número: ")
    
    print("Operaciones: 1=Suma, 2=Resta, 3=Multiplicación, 4=División")
    op = input_int("Operación (1-4): ", min_val=1, max_val=4)
    
    resultado = calculadora(a, b, op)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
