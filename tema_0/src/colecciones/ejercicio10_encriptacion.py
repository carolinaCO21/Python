from utils import input_str

def main():
    clave = {
    'e': 'p', 'i': 'v', 'k': 'i', 'm': 'u', 'p': 'm',
    'q': 't', 'r': 'e', 's': 'r', 't': 'k', 'u': 'q', 'v': 's'
    }

    frase = input_str("Frase a encriptar: ")
    encriptada = "".join(clave.get(caracter, caracter) for caracter in frase)
    print(f"Frase encriptada: {encriptada}")

if __name__ == "__main__":
    main()