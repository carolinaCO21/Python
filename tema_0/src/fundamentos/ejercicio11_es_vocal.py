from utils import input_str

def es_vocal(caracter):
    return caracter.lower() in 'aeiouáéíóú'

def main():
    letra = input_str("Introduce un carácter: ", min_len=1)
    print(f"'{letra}' {'ES' if es_vocal(letra) else 'NO ES'} vocal")

if __name__ == "__main__":
    main()
