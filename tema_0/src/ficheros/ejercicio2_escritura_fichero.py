import os
from utils import input_str  # tu función de input

def main():
    # Carpeta donde está el script
    carpeta_script = os.path.dirname(os.path.abspath(__file__))

    # Subimos niveles hasta 'tema_0'
    carpeta_proyecto = os.path.abspath(os.path.join(carpeta_script, "..", ".."))

    carpeta_data = os.path.join(carpeta_proyecto, "data")
    os.makedirs(carpeta_data, exist_ok=True)  # crea la carpeta si no existe

    
    nombre_archivo = input_str("Nombre del archivo (sin extensión): ").strip() + ".txt"
    ruta_archivo = os.path.join(carpeta_data, nombre_archivo)

    print("Escribe líneas (escribe 'fin' para terminar):")

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        while True:
            linea = input_str("> ")
            if linea.lower() == "fin":
                break
            archivo.write(linea + "\n")

    print(f"Archivo '{nombre_archivo}' guardado correctamente en '{carpeta_data}'")

if __name__ == "__main__":
    main()
