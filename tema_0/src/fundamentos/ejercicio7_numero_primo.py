import math

from utils import input_int

def es_primo(n):
    if n < 2: # Los números primos son mayores o iguales a 2.
        return False
    for i in range(2, int(math.sqrt(n)) + 1): # 2 hasta √n (raíz cuadrada de n)
        if n % i == 0:
            return False
    return True

def main():
    numero = input_int("Número para verificar primo: ", min_val=0)
    print(f"{numero} {'ES' if es_primo(numero) else 'NO ES'} primo")

if __name__ == "__main__":
    main()
