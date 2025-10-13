import random
from utils import input_int

def main():
    lista = [random.randint(1, 10) for _ in range(100)]
    n = input_int("Numero a buscar (1-10): ", min_val=1, max_val=10)
    print(f"El numero {n} aparece {lista.count(n)} veces")



if __name__ == "__main__":
    main()