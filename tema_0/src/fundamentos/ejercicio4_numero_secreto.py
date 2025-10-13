import random
from utils import input_int

def main():
    secreto = random.randint(1, 100)
    intentos = 0
    
    print("Adivina el número secreto (1-100). Introduce -1 para rendirte")
    
    while True:
        intento = input_int("Tu intento: ", min_val=-1, max_val=100)
        intentos += 1
        
        if intento == -1:
            print(f"Te rendiste. El número era {secreto}")
            break
        elif intento == secreto:
            print(f"¡Correcto! Acertaste en {intentos} intentos")
            break
        else:
            print("MAYOR" if intento < secreto else "MENOR")

if __name__ == "__main__":
    main()
