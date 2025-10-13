from utils import input_str

def main():
    texto = input_str("Introduce un texto: "). lower()
    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        palabra_limpia = palabra.strip(' ., !?; :')
        frecuencia[palabra_limpia] = frecuencia.get(palabra_limpia, 0) + 1

    print("Frecuencia de palabras:")
    for palabra, count in frecuencia. items():
        print(f"'{palabra}': {count}")

if __name__ == "__main__":
    main()